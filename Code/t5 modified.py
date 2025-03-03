from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import re
import nltk
from nltk.tokenize import sent_tokenize


tokenizer = AutoTokenizer.from_pretrained('google-t5/t5-small')
model = AutoModelForSeq2SeqLM.from_pretrained('google-t5/t5-small')

with open('/Users/vigneshram/Documents/code/transcription.txt', 'r') as f:
    sequence = f.read()


chunk_size = 4000
chunks = [sequence[i:i + chunk_size] for i in range(0, len(sequence), chunk_size)]

summaries = []
for chunk in chunks:
    sub_chunk_size = 2000
    sub_chunks = [chunk[i:i + sub_chunk_size] for i in range(0, len(chunk), sub_chunk_size)]

    sub_summaries = []
    for sub_chunk in sub_chunks:
       
        inputs = tokenizer.encode("summarize the content :" + sub_chunk, return_tensors='pt', max_length=1024, truncation=True)
        output = model.generate(inputs, min_length=50, max_length=80)
        summary = tokenizer.decode(output[0])

        
        summary = summary.replace("<pad>", "").replace("<s>", "").replace("</s>", "")
        summary = re.sub(r'[^\x00-\x7F]+', '', summary)
        summary = re.sub(r'\s+', ' ', summary).strip()

        
        sentences = sent_tokenize(summary)

        
        unique_sentences = list(set(sentences))

        
        summary = '\n'.join(unique_sentences)

        sub_summaries.append(summary)

    
    chunk_summary = '\n\n'.join(sub_summaries)
    summaries.append(chunk_summary)


final_summary = '\n\n'.join(summaries)


with open('summary.txt', 'w') as f:
    f.write(final_summary)

print("Summary saved to summary.txt")
del model
del tokenizer