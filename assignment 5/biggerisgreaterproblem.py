# 3. Bigger is Greater
# Given a word w, rearrange the letters of w to construct another word s in such a way that s is
# lexicographically greater than w.
# Input Format:
# The first line of inputs contains t, number of test cases. Each of the next t lines contains w.
# Constraints:
# 1 <= t <= 105
# 1 <= |w| <= 100
# w will contain only lower-case English letters and its length will not exceed 100.
# Output Format:
# For each test case, output a string lexicographically bigger than w in a separate line. In case of
# multiple possible answers print the lexicographically smallest one and if no answer exists, print
# no answer.
# Sample Input:
# 3
# ab
# bb
# hefg
# Sample Output:
# ba
# no answer
# hegf

# Explanation:
# Testcase 1: There exists only one string greater than ab which can be built by rearranging ab. That
# is ba.
# Testcase 2: Not possible to rearrange bb and get a lexicographically greater string.
# Testcase 3: hegt is the next string (lexicographically greater) to hefg.
def next_permutation(s):
    s = list(s)
    i = len(s) - 2
    while i >= 0 and s[i] >= s[i + 1]:
        i -= 1
    if i == -1:
        return "no answer"
    j = len(s) - 1
    while s[j] <= s[i]:
        j -= 1
    s[i], s[j] = s[j], s[i]
    s = s[:i + 1] + sorted(s[i + 1:])
    return ''.join(s)

def bigger_is_greater():
    t = int(input())
    results = []
    for _ in range(t):
        w = input().strip()
        results.append(next_permutation(w))
    print("\n".join(results))

if __name__ == "__main__":
    bigger_is_greater()