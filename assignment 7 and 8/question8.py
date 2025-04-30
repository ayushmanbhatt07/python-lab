# Decode the message:
# A message containing the letters from A-Z can be encoded into the numbers using the mapping
# A-> 1, B-> 2, C-> 3, ..., Z-> 26. To decode an encoded message, you need to group the digits
# and do the reverse mapping. You are required to display all the possible decoded messages.
# For example: "11106" can be decoded into:
# a. "AAJF" with the grouping (1 1 10 6)
# b. "KJF" with the grouping (11 10 6)
def decode_message(encoded_message):
    def decode_helper(index, path, results):
        if index == len(encoded_message):
            results.append("".join(path))
            return
        if encoded_message[index] == '0':
            return
        # Single digit decoding
        num = int(encoded_message[index])
        if 1 <= num <= 9:
            decode_helper(index + 1, path + [chr(num + 64)], results)
        # Two digit decoding
        if index + 1 < len(encoded_message):
            num = int(encoded_message[index:index + 2])
            if 10 <= num <= 26:
                decode_helper(index + 2, path + [chr(num + 64)], results)

    results = []
    decode_helper(0, [], results)
    return results


# Example usage
encoded_message = "11106"
decoded_messages = decode_message(encoded_message)
print("Possible decoded messages:")
for message in decoded_messages:
    print(message)