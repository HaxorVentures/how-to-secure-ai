import unicodedata

def normalize_text(text: str) -> str:
  """Normalize Unicode text to NFKC form."""
  return unicodedata.normalize('NFKC', text)

# Example
malicious_input = "executе('malicious code')".replace('e', 'е') # Using Cyrillic 'е'
normalized_input = normalize_text(malicious_input)
print(f"Original: {malicious_input}")
print(f"Normalized: {normalized_input}")

# Now apply your security checks on 'normalized_input'
if "execute(" in normalized_input:
    print("Potential code injection detected after normalization!")