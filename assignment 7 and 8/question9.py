# Create a tokenizer for your own language (mother tongue you speak). The tokenizer should
# tokenize punctuations, dates, urls, emails, numbers (in all different forms such as “33.15”,

# “3,22,243”, “313/77”), social media usernames/user handles. Use regular expressions to design
# this. [Hint: Use unicode blocks for your language, check wikipedia pages]
import re

def custom_tokenizer(text):
    # Define regex patterns
    patterns = {
        'punctuations': r'[.,!?;:"\'()]',
        'dates': r'\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b',
        'urls': r'https?://[^\s]+',
        'emails': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        'numbers': r'\b\d{1,3}(,\d{3})*(\.\d+)?\b',
        'usernames': r'@\w+',
        'unicode_words': r'[\u0900-\u097F]+'  # Example for Hindi Unicode block
    }

    tokens = []
    for name, pattern in patterns.items():
        matches = re.findall(pattern, text)
        tokens.extend(matches)

    return tokens

# Example usage
text = "Visit https://example.com or email me at test@example.com. My handle is @user123. Date: 12/10/2023. Number: 3,22,243."
print(custom_tokenizer(text))