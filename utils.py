import pymorphy2

INDEX_ENTRY_SEPARATOR = ': '
INDEX_FILE_NAME = 'index.txt'


def write_index(run_path: str, index: dict):
    with open('{}/index.txt'.format(run_path), 'w') as file:
        for i, item in enumerate(sorted(index.items())):
            entry = '{}{}{}'.format(item[0], INDEX_ENTRY_SEPARATOR, item[1])
            file.write(entry)
            if i != len(index) - 1:
                file.write('\n')


def read_text(dir_path: str, file_name: str) -> str:
    file_path = '{}/{}'.format(dir_path, file_name)
    print('Read text from file {}...'.format(file_path))
    return open(file_path, 'r').read()


morph = pymorphy2.MorphAnalyzer()


def lemmatize(text: str) -> str:
    return morph.parse(text)[0].normal_form


def pos(word):
    return morph.parse(word)[0].tag.POS
