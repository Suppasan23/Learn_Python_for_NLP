from pythainlp.tokenize import word_tokenize

# Thai sentence for testing
text = "ฉันรักภาษาไทยและการประมวลผลภาษาธรรมชาติ"

# Available engines to compare
engines = ["newmm", "longest", "icu", "deepcut"]

print(f"Original text:\n{text}\n")

for engine in engines:
    try:
        tokens = word_tokenize(text, engine=engine)
        print(f"Engine: {engine}")
        print(tokens)
        print()
    except Exception as e:
        print(f"Engine: {engine} ❌ Error: {e}")
        print()