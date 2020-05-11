import re

# ---------------------------------------------------
input_file = 'input.txt'
output_file = 'output.txt'
encoding = 'utf-8'
quotation_mark = r'「.+?」' # 英文用 r'\".+?\"'

# 台詞内の文字変換
is_translate = True
replace_symbols = {
    '。': '\n',
    '!': '!\n',
    '?': '?\n',
    '……': '...',
    'ーーー': ''
}
# ---------------------------------------------------


def main():
    # 台詞の読み込み
    with open(input_file, 'r', encoding=encoding) as fr:
        s = fr.read()
        match = re.findall(quotation_mark, s)

        # 台詞の書き込み
        with open(output_file, 'w', encoding=encoding) as fw:
            for m in match:
                m = m[1:-1]
                newline = ''

                if is_translate:
                    for key, value in replace_symbols.items():
                        m = m.replace(key, value)

                if m[:-1] != '\n':
                    newline = '\n'

                fw.write(m + newline)


if __name__ == '__main__':
    main()
