from anthropic import Anthropic

client = Anthropic()

tokens = client.count_tokens("Amazon Bedrock は AWS の生成 AI サービスです。")
print(tokens)

tokens = client.count_tokens("Amazon Bedrock is an AWS generative AI service")
print(tokens)
