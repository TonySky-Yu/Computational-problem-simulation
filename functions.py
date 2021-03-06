from random import choice,randint
from time import time

def my_choice(seq):
    return seq.pop(randint(0, len(seq)-1))

def write(question_list, file_name = "test.tex", mode = "w", title = "中考计算精炼", spacenum = 8):
    with open(file_name, mode) as f:
        f.write(r"\documentclass{ctexart}"\
+ "\n" + r"\title{" +title + "}" +\
r"""
\begin{document}
    \maketitle
""")
        for index, question in enumerate(question_list, 1):
            f.write(f"({index}). "+f"${question}$" + r"\\"*spacenum + "\n")
        f.write("\n"+r"\end{document}")


def question_maker(a, b, n, kd_list, if_logging = False):
    string = "" #最终返回的题目储存器
    question_list = [my_choice(kd_list) for i in range(n)]
    if if_logging:
        with open("Loggings.log", "a") as l:
            l.write(f": {[kd.__doc__ for kd in question_list]}\n")
    question_list = [i(a, b) for i in question_list]

    for question in question_list:
        string = question + choice(["+", "-"]) + string
    return string[:-1]

if __name__ == "__main__":
    a = question_maker(2, 3, 4, False)
    print(a)