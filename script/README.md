# filter_combined.py
いずれもPython3.8 で実行されている。また、Python 標準の正規表現モジュールであるreを利用している。
## 1 かな漢字が少なすぎる行を削除
かな漢字が少なすぎるテキストにFalse を返す。
```python:isGoodJapaneseRate
def isGoodJapaneseRate(line):
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
```

## 2.括弧を含む行を削除
括弧を含む文にFalseを返す。
```python:isNotContainParenthesis
def isNotContainParenthesis(line):
    p_parenthesis = re.compile(".*（.*?）.*")
    if p_parenthesis.match(line): return False
    return True
```

## 3.URLを含む行を削除
httpsを含むテキストにFalseを返す。
```python:isNotContainURL
def isNotContainURL(line):
    p_http = re.compile(".*ｈｔｔｐ.*")
    if p_http.match(line): return False
    return True
```

## 4.指定終端文字で終わらない行を削除
。！？．」で終わらない文にFalseを返す。
```python:isFinPunctation
def isFinPunctation(line):
    p_punctation = re.compile(".*[。！？．」]")
    if p_punctation.fullmatch(line): return True
    return False
```

## 5.【】を含む行を削除
【】を含む文にFalseを返す。
```python:isNotContainECommerce
def isNotContainECommerce(line):
    p_parren = re.compile(".*【.*】.*")
    if p_parren.match(line): return False
    return True
```

## 6.長音の規格化
チルダ含む長音の繰り返しをなくして長音一つに規格化。
```python:NormalizeProlong
def NormalizeProlong(line):
    p_prolong = re.compile("[﹣－ｰ—―─━ー~∼∾〜〰～]+")
    line = p_prolong.sub("ー", line)
    return line
```
## 7.スペースを削除
```python:DelSpace
def DelSpace(line):
    p_space = re.compile("　")
    line = p_space.sub("", line)
    return line
```
