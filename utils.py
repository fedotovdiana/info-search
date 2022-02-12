INDEX_ENTRY_SEPARATOR = ': '


def write_index(run_path: str, index: dict):
    with open('{}/index.txt'.format(run_path), 'w') as file:
        for i, item in enumerate(sorted(index.items())):
            entry = '{}{}{}'.format(item[0], INDEX_ENTRY_SEPARATOR, item[1])
            file.write(entry)
            if i != len(index) - 1:
                file.write('\n')