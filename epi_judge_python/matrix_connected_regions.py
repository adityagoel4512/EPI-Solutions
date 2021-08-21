from typing import List

from test_framework import generic_test


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:

    def inside_image(cur_x, cur_y):
        return 0 <= cur_x < len(image[0]) and 0 <= cur_y < len(image)

    def dfs(cur_x, cur_y):
        if inside_image(cur_x, cur_y) and image[cur_x][cur_y] == colour:
            image[cur_x][cur_y] = not colour
            for new_x, new_y in ((cur_x, cur_y+1), (cur_x, cur_y-1), (cur_x-1, cur_y), (cur_x+1, cur_y)):
                dfs(new_x, new_y)

    colour = image[x][y]
    dfs(x, y)

def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
