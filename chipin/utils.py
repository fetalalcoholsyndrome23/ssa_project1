import re

def censor_message(message):
    """
    Replaces censored words in the message with asterisks.
    """
    for word in CENSORED_WORDS:
        # Use regex to match whole words only (case-insensitive)
        pattern = r'\b' + re.escape(word) + r'\b'
        replacement = '*' * len(word)
        message = re.sub(pattern, replacement, message, flags=re.IGNORECASE)
    return message



CENSORED_WORDS = [
    "badword1",
    "badword2",
    "offensivephrase",
]