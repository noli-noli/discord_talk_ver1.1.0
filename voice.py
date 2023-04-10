import subprocess
import re
import pickle

def remove_emoji(text):
    pattern = r'<:[a-zA-Z0-9_]+:[0-9]+>' 
    return re.sub(pattern,'',text)

def url_skip(text):
    pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
    return re.sub(pattern,"urlを省略",text)

def wara(text):
    pattern = "w"
    return re.sub(pattern,"わら",text)

def remove_symbol(text):
    with open("sample.pkl","rb") as f:
        list = pickle.load(f)
    for a in list:
        text = re.sub(a,"",text)
    return text
    #return re.sub("\n","",text)

def creat_voice(voice):
    pattern_text = remove_emoji(voice)
    pattern_text = url_skip(pattern_text)
    pattern_text = wara(pattern_text)
    pattern_text = remove_symbol(pattern_text)
    subprocess.run(f'echo {pattern_text} | open_jtalk -m /usr/share/hts-voice/mei/mei_normal.htsvoice -x /var/lib/mecab/dic/open-jtalk/naist-jdic -ow ./output.wav -g 15',shell=True)

def test():
    print("test")