"""旨在清楚文本中的不明字符
将相同含义的字符统一映射到常用字符
"""

import unicodedata
from zhconv import convert
import re

num_english = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'ELEVEN', 'TWELVE',
               'THIRTEEN', 'FOURTEEN', 'FIFTEEN', 'SIXTEEN', 'SEVENTEEN', 'EIGHTEEN', 'NINETEEN', 'TWENTY']
num_convert = {x: str(i) for i, x in enumerate(num_english, start=1)}


def convert_to_unicode(text):
    """Converts `text` to Unicode (if it's not already), assuming utf-8 input."""
    if isinstance(text, str):
        return text
    elif isinstance(text, bytes):
        return text.decode("utf-8", "ignore")
    else:
        raise ValueError("Unsupported string type: %s" % (type(text)))


def is_chinese(char):
    """判断一个字符是否是中文
    """
    return unicodedata.name(char).startswith('CJK')


def clean_text(text: str):
    """
    清除无意义字符
        1. Zl, Separator, line
        2. Zp, Separator, paragraph
        3. Cc, Cf, Cs, Co, Cn
        4. So，examples: ☜ ☝ ☟  ㈪ ㈫ ㈬ ㈭  ㎠ ㎤ ｍ ㎡ ㎥ ⒜ ⒝ ⒞ ⒟ ⒠  ┣ ┳ ┫ ┻ ╋ ㍾ ㍽ ㍼ ㍻
        5. Sc，货币符号  example： ￥ $ ￥ ＄ ¢ £
        6. Lm, 修饰字母
        7. P 标点都去掉算了  因为 + = 这些可能有含义的是Sm类型，不会被去掉  额外保留 .号
    将空白符归一化
        1. Zs -> ' '
        2. 其他数字 转为 阿拉伯数字
    """
    text = convert_to_unicode(text)
    output = []
    for char in text:
        if char == '.':
            output.append(char)
            continue
        cat = unicodedata.category(char)
        if cat in {'Zl', 'Zp', 'Cc', 'Cf', 'Cs', 'Co', 'Cn', 'So', 'Sc', 'Lm'} or cat.startswith('P'):
            continue
        if cat == 'Zs':
            output.append(' ')
        else:
            # 数字归一化到阿拉伯数字
            match = re.search(
                r"ELEVEN|TWELVE|THIRTEEN|FOURTEEN|FIFTEEN|SIXTEEN|SEVENTEEN|EIGHTEEN|NINETEEN|TWENTY|ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN",
                unicodedata.name(char))
            if match:
                char = num_convert[match.group()]
            output.append(char)

    text = "".join(output)
    # 繁体转简体
    text = convert(text, 'zh-cn')
    # 字母大写转小写
    text = text.lower()
    return text


if __name__ == '__main__':
    text = "我幹什麼不干你事,打我电话⒈ ⒉  ⑪ ⑫ ⑬  ⒍ ⒎ ⒏ ⒐ W,X 记起来, asdhuaiwe465124381%……@#&*……￥#）——I_) +I ======= +v：waf809asd"
    print(clean_text(text))

