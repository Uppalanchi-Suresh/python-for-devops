import re

text = "The quick brown fox jumps over the lazy brown dog"
pattern = "brown"

replacement = "dark blue"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)
