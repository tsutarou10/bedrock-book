from ai21_tokenizer import Tokenizer

tokenizer = Tokenizer.get_tokenizer()

text = "Amazon Bedrock は AWS の生成AIサービスです。"

encoded_text = tokenizer.encode(text)
tokens = tokenizer.convert_ids_to_tokens(encoded_text)

print(tokens)
