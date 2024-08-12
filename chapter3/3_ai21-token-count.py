from ai21_tokenizer import Tokenizer

tokenizer = Tokenizer.get_tokenizer()

encoded_text = tokenizer.encode("Amazon Bedrock は AWS の生成AIサービスです。")
print(len(encoded_text))

encoded_text = tokenizer.encode("Amazon Bedrock is an AWS generative AI service")
print(len(encoded_text))
