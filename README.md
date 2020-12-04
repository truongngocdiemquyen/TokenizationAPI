# TOKENIZATION TEXT
### Overview
This repo is to tokenize the text in these supported languages.
> ```list_language_supported``` = [English ('en'), Korean ('ko'), Indonesia ('id'), Malay ('ms'), Spanish ('es'), Portuguese ('pt'), Swedish ('sv'), Hindi ('hi'), Benlagi ('bn'), German ('de'), Vietnamese ('vi'), Thai ('th'), Chinese ('zh_cn'), Taiwan ('zh_tw'), Japanese ('ja'), Arabic ('ar'), French ('fr'), Russian ('ru')]
                            
- Input: Text AND Language
- Output: A list of tokens OR a string which combined by a list of tokens

```Example output:``` 
- Input: (Text = Tôi yêu Việt Nam) AND (Language = vi)
- Output: 
    - Text tokenization to list: ["Tôi", "yêu", "Việt_Nam"]
    - Text tokenization to string: "Tôi yêu Việt_Nam"


### Installation
##### Install libraries
Use pip3 to install all neccesary libraries.
```
pip3 install -r requirement.txt
```
##### Download twkorean model from github
The twkorean model supports Korean tokenization.
```
git clone https://github.com/jaepil/twkorean
cd twkorean
python3 setup.py install
```
### Run the code
Use python3 (python 3.8) to run the code.
```
python3 API_Tokenize.py
```
  ```Example request:```
##### Text tokenization to list:
```
http://0.0.0.0:3000/tokenize?text=Tôi yêu Việt Nam&language=vi
```
- Output: 
> {"success": true, "input": {"text": "Tôi yêu Việt Nam", "language": "vi"}, "output": ["Tôi", "yêu", "Việt_Nam"]}
##### Text tokenization to string:
```
http://0.0.0.0:3000/tokenize_join?text=Tôi yêu Việt Nam&language=vi
```
- Output:
> {"success": true, "input": {"text": "Tôi yêu Việt Nam", "language": "vi"}, "output": "Tôi yêu Việt_Nam"}
### Note
1. If the text input is empty, the default text is " ". So there is no output, only there is a message: "Please input the text".
2. If the language is empty, the default language is English (en). So the text is tokenized by white space.
3. If the language is not in the list of the supported languages, the result is none, only there is a message: "This language is not supported".