"""
Dataset module
"""

## Imports
import numpy as np 
import pandas as pd
from transformers import AutoTokenizer

import os 

tokenizer = AutoTokenizer('')

def tokenize_labelize(essay,tokenizer,predictionstring=None,labels=None):
    """Tokenize an essay and match each token with the corresponding label.

    Args:
        essay (str): Text to tokenize
        predictionstring (pandas.Series | numpy.array, optional): As a string, list of 
        index position of words with a label. Must be provided with labels. Defaults to None.
        labels (pandas.Series | numpy.array, optional): As a string, list of 
        labels of each word. Must be provided with labels. Defaults to None.
        tokenizer (tokenizer): [description].

    Returns:
        [type]: [description]
    """
    
    tokens = tokenizer(essay,
                       return_attention_mask = True,
                       return_token_type_ids = False,
                       padding = 'max_length',
                       max_length = 1024,
                       truncation = True,
                       return_tensors='np'
                      )
    
    word_ids=tokens.word_ids()
    
    labels_mapping = {'B-Lead' : 0,
                  'B-Position' : 1,
                  'B-Evidence' : 2,
                  'B-Claim' : 3,
                  'B-Concluding_Statement' : 4,
                  'B-Counterclaim' : 5,
                  'B-Rebuttal' : 6,
                  'I-Lead' : 7,
                  'I-Position' : 8,
                  'I-Evidence' : 9,
                  'I-Claim' : 10,
                  'I-Concluding_Statement' : 11,
                  'I-Counterclaim' : 12,
                  'I-Rebuttal': 13}
    
    if not labels:
        match = {p:labels_mapping[l] for p,l in zip(predictionstring,labels)}
        labels_matched = [-100 if (w==None or w==word_ids[i-1]) \
                            else match.get(str(w),14) \
                            for i,w in enumerate(word_ids)]
        
        return {
        'input_ids' : tokens['input_ids'][0],
        'attention_mask' : tokens['attention_mask'][0],
        'labels': np.array(labels_matched)
        }
    
    return {
        'input_ids' : tokens['input_ids'][0],
        'attention_mask' : tokens['attention_mask'][0],
        }