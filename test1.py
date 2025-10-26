import re


def lex_analyzer(source_code):
    """
    词法分析器主函数
    :param source_code: 待分析的源代码字符串
    :return: 词法分析结果列表，每个元素为(单词类别, 单词值)
    """
    # 定义关键字集合
    keywords = {'begin', 'if', 'then', 'while', 'do', 'end'}

    # 定义运算符和界符
    operators_delimiters = {
        '+', '-', '*', '/', '=', '<', '>', ':', ';', ',', '(', ')', '{', '}', '[', ']',
        '==', ':=', '<=', '>=', '!='
    }

    # 定义正则表达式模式
    # 顺序很重要，长运算符需要放在短运算符前面
    pattern = r'''
        (:=)|(==)|(<=)|(>=)|(!=)|  # 双字符运算符
        [+\-*/=<>;:(),{}[\]]|     # 单字符运算符和界符
        [a-zA-Z][a-zA-Z0-9]*|     # 标识符
        [0-9]+|                    # 数字
        \s+                        # 空白字符
    '''
    token_specs = re.compile(pattern, re.VERBOSE)

    tokens = []
    line_num = 1
    line_start = 0

    for mo in token_specs.finditer(source_code):
        kind = mo.group()
        start = mo.start()
        end = mo.end()

        # 计算当前所在行号
        line_num += source_code[line_start:start].count('\n')
        line_start = end

        # 跳过空白字符
        if kind.isspace():
            continue

        # 识别关键字和标识符
        elif kind[0].isalpha():
            if kind in keywords:
                tokens.append(('KEYWORD', kind))
            else:
                tokens.append(('ID', kind))

        # 识别数字
        elif kind[0].isdigit():
            tokens.append(('NUM', kind))

        # 识别运算符和界符
        elif kind in operators_delimiters:
            tokens.append(('OPERATOR/DELIMITER', kind))

        # 无法识别的字符
        else:
            tokens.append(('ERROR', f"无法识别的字符: {kind}"))

    return tokens


def main():
    """主函数，读取输入并展示分析结果"""
    print("词法分析器")
    print("支持的关键字: begin, if, then, while, do, end")
    print("支持的运算符和界符: +, -, *, /, =, <, >, :, ;, , , (, ), {, }, [, ], ==, :=, <=, >=, !=")
    print("请输入要分析的代码(输入空行结束):")

    # 读取多行输入
    source_lines = []
    while True:
        line = input()
        if not line:
            break
        source_lines.append(line)
    source_code = '\n'.join(source_lines)

    # 进行词法分析
    result = lex_analyzer(source_code)

    # 输出结果
    print("\n词法分析结果:")
    print(f"{'类别':<20} 单词值")
    print("-" * 30)
    for token in result:
        print(f"{token[0]:<20} {token[1]}")


if __name__ == "__main__":
    main()