from curtsies.fmtfuncs import red, green, yellow, blue
from tokenizers.implementations import ByteLevelBPETokenizer
from transformers import GPT2Config, GPT2LMHeadModel, GPT2Tokenizer, DataCollatorForLanguageModeling
from datasets import load_dataset
from transformers import Trainer, TrainingArguments

# TRAIN_BASE = True
# paths = ['python_code_text_data.txt']
#
# if TRAIN_BASE:
#     tokenizer = ByteLevelBPETokenizer()
#     tokenizer.train(files=paths, vocab_size=52_000, min_frequency=2, special_tokens=[
#         "<s>",
#         "<pad>",
#         "</s>",
#         "<unk>",
#         "<mask>",
#     ])
#
#     tokenizer.save_model('tokenizer')

tokenizer = GPT2Tokenizer.from_pretrained('../tokenizer')
tokenizer.add_special_tokens({
    "eos_token": "</s>",
    "bos_token": "<s>",
    "unk_token": "<unk>",
    "pad_token": "<pad>",
    "mask_token": "<mask>"
})

model = GPT2LMHeadModel.from_pretrained("GPyT").to('cuda')
while True:
    inp = input(">>> ")
    input_ids = tokenizer.encode(inp, return_tensors='pt').to("cuda")
    beam_output = model.generate(
        input_ids,
        max_length=512,
        num_beams=10,
        temperature=0.7,
        no_repeat_ngram_size=5,
        num_return_sequences=1)

    for beam in beam_output:
        out = tokenizer.decode(beam)
        fout = out.replace("<N>", "\n")

        print(green(str(fout)))
