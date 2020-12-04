#Support Chinese
import jieba
#Support Janpanese
import MeCab
#Support Thai
import pythainlp
#Support VietNamese
from pyvi import ViTokenizer
#Support Araby
import pyarabic.araby as araby
#Support Korean 
from twkorean import TwitterKoreanProcessor

import chardet    
from config import *

ko_tokenizer = TwitterKoreanProcessor()
ja_tagger = MeCab.Tagger() # no additional dict, for local debug purpose

def tokenize(text, language):
    """ Tokenize text based on language """

    if language in SPACE_SEPARATED_LANGUAGES:
        return text.split()
    elif language == 'vi':
        temp = ViTokenizer.tokenize(text)
        temp = temp.split()
        return temp
    elif language == 'th':
        return pythainlp.tokenize.word_tokenize(text)
    elif language == 'zh_tw' or language == 'zh_cn':
        return list(jieba.cut(text, HMM=False))
    elif language == 'ja':
        token = []
        string_ = ja_tagger.parse(text)
        for line in string_.split("\n"):
            if line.split()[0] == "EOS":
                break
            token.append(line.split()[0])
        token = [x for x in token]
        return token
    elif language == 'ar':
        return araby.tokenize(text)
    elif language == 'ko':
        result_temp = ko_tokenizer.tokenize_to_strings(text)
        result = []
        for word in result_temp:
            result.append(str(word))
        return result
    return None

def tokenize_join(text, language):
    tokenize_list = tokenize(text,language)
    result = ' '.join(tokenize_list)
    if type(result) is bytes:
        if chardet.detect(result)['encoding'] == 'UTF-16':
            result = result.decode('utf-16')
        elif chardet.detect(result)['encoding'] == 'cp1252':
            result = result.decode('cp1252')
        else:
            result = result.decode('utf-8')
    return result        
