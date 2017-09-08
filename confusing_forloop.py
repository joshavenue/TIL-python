# you divide it in 3 parts: the _yielding_ part is the first `Word` , 
# then you have the _loop_ `for Word in WORD_TOKENS` and lastly,
# you have the _condition_ `if not Word in STOP_WORDS`

FILTERED_SENTENCE = [Word for Word in WORD_TOKENS if not Word in STOP_WORDS]

# IS THE SAME AS BELOW

for Word in WORD_TOKENS:
    if Word not in STOP_WORDS:
        yield Word
        
