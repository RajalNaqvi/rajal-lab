"""
    Problem statement-:  
        We know sentences are terminated with certain punctuations like ‘.’,’!’,’?’, 
        whereas there are several punctuations which don’t terminate the punctuations.
        Given for a paragraph, write a code to find out how many sentences are there.
        
    Note that, ‘…’,’,’,’-‘ these don’t terminate a sentence.
    
    Constraints: 
        Number of words in the paragraph<=10^8
    
    Input Format:
        Paragraph ended with an enter.
    

    Output Format:
        Single Integer denoting number of sentences.
    
    Sample Input:
        Hello! How are you? Last time I saw you… you were nervous.

    Sample Output:
        3

    Explanation:
        The three sentences are:
        hello!
        How are you?
        Last time I saw you… you were nervous.
"""


import re

def count_sentences(paragraph):
    pattern = r"(?<!\.)[.!?](?=\s|$)"
    sentences = re.findall(pattern, paragraph)
    return len(sentences)

# Input paragraph (read until newline)
paragraph = input().strip()

# Output the count of sentences
print(count_sentences(paragraph))
