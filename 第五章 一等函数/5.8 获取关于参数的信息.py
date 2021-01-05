import bobo

@bobo.query('/')
def hello(person):
    return 'Hello %s!' % person

#在指定长度附近截断字符串的函数
def clip(text, max_len=80):
    """在max_len前面或后面的第一个空格处截断文本"""
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None: #没找到空格
        end = len(text)
    return text[:end].rstrip()

clip.__defaults__
clip.__code__
clip.__code__.co_varnames
clip.__code__.co_argcount

from inspect import signature
sig = signature(clip)
sig
str(sig)
for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)




