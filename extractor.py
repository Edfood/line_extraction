import re

input_file = 'input.txt'
output_file = 'output.txt'
quotation_mark = r'「.+?」'        # 英文用 r'\".+?\"'
encoding = 'utf-8'
is_translate = True              # 台詞内の文字変換
translate_symbols = str.maketrans({
    # '変換元の文字列': '変換先の文字列',
    '。': '。\n',
    '!': '!\n',
    '?': '?\n'
})


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
                    m = m.translate(translate_symbols)

                if m[:-1] != '\n':
                    newline = '\n'

                fw.write(m + newline)


if __name__ == '__main__':
    main()
