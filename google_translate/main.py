import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import requests
import json
import execjs
import os
import tornado.autoreload
from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)



class Py4Js(object):
    def __init__(self):
        self.ctx = execjs.compile(""" 
        function TL(a) { 
        var k = ""; 
        var b = 406644; 
        var b1 = 3293161072; 

        var jd = "."; 
        var $b = "+-a^+6"; 
        var Zb = "+-3^+b+-f"; 

        for (var e = [], f = 0, g = 0; g < a.length; g++) { 
            var m = a.charCodeAt(g); 
            128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023), 
            e[f++] = m >> 18 | 240, 
            e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224, 
            e[f++] = m >> 6 & 63 | 128), 
            e[f++] = m & 63 | 128) 
        } 
        a = b; 
        for (f = 0; f < e.length; f++) a += e[f], 
        a = RL(a, $b); 
        a = RL(a, Zb); 
        a ^= b1 || 0; 
        0 > a && (a = (a & 2147483647) + 2147483648); 
        a %= 1E6; 
        return a.toString() + jd + (a ^ b) 
    }; 

    function RL(a, b) { 
        var t = "a"; 
        var Yb = "+"; 
        for (var c = 0; c < b.length - 2; c += 3) { 
            var d = b.charAt(c + 2), 
            d = d >= t ? d.charCodeAt(0) - 87 : Number(d), 
            d = b.charAt(c + 1) == Yb ? a >>> d: a << d; 
            a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d 
        } 
        return a 
    } 
    """)

    def getTk(self, text):
        return self.ctx.call("TL", text)

en2ch = "translate_a/single?client=t&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1&srcrom=0&ssel=0&tsel=0&kc=2"
ch2en = "/translate_a/single?client=t&sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&swap=1&source=btn&ssel=5&tsel=5&kc=0"


def translate(tk, content, translate_type):
    if len(content) > 10000:
        print("翻译的长度超过限制！！！")
        return

    param = {'tk': tk, 'q': content}

    result = requests.get("http://translate.google.cn/{}".format(translate_type), params=param)

    # 返回的结果为Json，解析为一个嵌套列表
    # pprint.pprint(result.json())
    result = result.json()
    ch_sentence = []
    for part in result[0][:-1]:
        ch_sentence.append([part[0].strip(), part[1].strip()])
    return ch_sentence


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', en_sentence="", ch_sentence="")

    def post(self):
        en_sentence = self.get_argument("en_sentence")
        en_sentence = str.replace(en_sentence, "\r\n", " ")
        js = Py4Js()
        ch_sentence = translate(js.getTk(en_sentence), en_sentence, en2ch)
        self.render('index.html', en_sentence=en_sentence, ch_sentence=ch_sentence)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)],
                                  template_path=os.path.join(os.path.dirname(__file__), "templates"),
                                  static_path=os.path.join(os.path.dirname(__file__), "static"),
                                  debug=True
                                  )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print("server started at http://127.0.0.1:8000")
    tornado.ioloop.IOLoop.instance().start()