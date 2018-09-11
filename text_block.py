"""
利用python将文本文件进行渲染，转换成html格式的文件进行输出:
注意点:1.字符串方法strip：不仅会消除两端的空格，还会消除两端的换行符\n
       2.标准输入源：sys.stdin
       3.标准输出源：sys.stdout,print、input中出现的语句将出现在标准输出源中
       4.正则表达式的使用，替换功能：re.sub(r'', r'\1', string),其中\1为分组的角标，表示第一个分组，即使用第一个分组中的内容替换
                                   匹配的内容
       5.运行程序即可生成html文件：python3 text_block.py <file> test_output.html
       6.正则表达式re模块的sub方法，第二个参数可以接受一个函数，把匹配对象传递给函数执行
"""
import sys
import re


def lines(file):
    for line in file:
        yield line
    yield '\n'  # 文本末尾添加一个换行，否则无法收集到最后一个block


def blocks(file):
    """
    文本块生成器，将文本按照段落进行分离，使用生成器来实现
    """
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []


if __name__ == '__main__':
    print('<html><head><title>Big exercise</title></head><body>')

    title = True
    for block in blocks(sys.stdin):
        block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
        if title:
            print('<h1>')
            print(block)
            print('</h1>')
            title = False
        else:
            print('<p>')
            print(block)
            print('</p>')

    print('</body></html>')
