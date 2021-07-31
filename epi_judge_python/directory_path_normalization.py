from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    equivalent_path = []
    absolute = path[0] == '/'
    for section in path.split('/'):
        if section == '':
            continue
        elif section == '.':
            continue
        elif section == '..':
            if not absolute and (not equivalent_path or equivalent_path[-1] == '..'):
                equivalent_path.append('..')
            elif equivalent_path:
                equivalent_path.pop()
        else:
            equivalent_path.append(section)

    file_path = '/'.join(equivalent_path)
    return '/' + file_path if absolute else file_path


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
