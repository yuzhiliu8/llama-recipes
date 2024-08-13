from transformers import LlamaTokenizer
extended_tokenizer = LlamaTokenizer.from_pretrained('./tokenizers/my_extended_tokenizer')
llama_tokenizer = LlamaTokenizer.from_pretrained('meta-llama/Llama-2-7b-chat-hf')

text='သငျသညျအတွက်ပျံသန်းနိုင်သည်အနီးဆုံးလေဆိပ်'
print(llama_tokenizer.tokenize(text))
print(extended_tokenizer.tokenize(text))