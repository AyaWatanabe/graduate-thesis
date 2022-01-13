# %%
def isGoodJapaneseRate(line):
    #かな漢字が少なすぎるテキストにFalseを返す
    limite = len(line) * 0.3
    count = 0
    for c in line[:-1]:
        #それぞれかな、漢字の範囲
        if (ord(c) <= 12538 and ord(c) >= 12353) or (ord(c) <= 40959 and ord(c) >= 13312):
            pass
        else:
            count += 1
            if count > limite:
                return False
    return True
# %%
def NormalizeProlong(line):
    #チルダ含む長音の繰り返しをなくして長音一つに規格化
    #参考：https://github.com/neologd/mecab-ipadic-neologd/wiki/Regexp.ja
    p_prolong = re.compile("[﹣－ｰ—―─━ー~∼∾〜〰～]+")
    line = p_prolong.sub("ー", line)
    return line
# %%
def DelSpace(line):
    #スペースを削除
    p_space = re.compile("　")
    line = p_space.sub("", line)
    return line
# %%
def isNotContainParenthesis(line):
    #括弧を含む文にFalseを返す
    p_parenthesis = re.compile(".*（.*?）.*")
    if p_parenthesis.match(line): return False
    return True
# %%
def isNotContainECommerce(line):
    #【】を含む文にFalseを返す
    p_parren = re.compile(".*【.*】.*")
    if p_parren.match(line): return False
    return True
# %%
def isNotContainURL(line):
    #httpsを含むテキストにFalseを返す
    p_http = re.compile(".*ｈｔｔｐ.*")
    if p_http.match(line): return False
    return True
# %%
def isFinPunctation(line):
    #。！？．」で終わらない文にFalseを返す
    p_punctation = re.compile(".*[。！？．」]")
    if p_punctation.fullmatch(line): return True
    return False
# %%
import gzip
import json
import sys
from tqdm import tqdm
import zenhan
import re
# %%
args = sys.argv
path = args[1]
output = args[2]
f = gzip.open(path, "rt")
o = open(output, "a")
# %%
for line in tqdm(f):
    text = zenhan.h2z(json.loads(line)['text'])
    T = text.split("\n")
    text_filtered = ""
    for t in T:
        if not isGoodJapaneseRate(t): continue
        if not isFinPunctation(t): continue
        if not isNotContainParenthesis(t): continue
        if not isNotContainECommerce(t): continue
        if not isNotContainURL(t): continue
        t = NormalizeProlong(t)
        t = DelSpace(t)
        text_filtered += t
    if text_filtered:
        o.write(text_filtered + "\n")
f.close()
o.close()
# %%
