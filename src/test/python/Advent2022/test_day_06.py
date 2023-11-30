from src.main.python.Advent2022.day_06 import part_one, part_two


def _input_part_one():
    return dict(
        mjqjpqmgbljsphdztnvjfqwrcgsmlb=7,
        bvwbjplbgvbhsrlpgdmjqwftvncz=5,
        nppdvjthqldpwncqszvftbrmjlhg=6,
        nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg=10,
        zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw=11,
    )


def _input_part_two():
    return dict(
        mjqjpqmgbljsphdztnvjfqwrcgsmlb=19,
        bvwbjplbgvbhsrlpgdmjqwftvncz=23,
        nppdvjthqldpwncqszvftbrmjlhg=23,
        nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg=29,
        zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw=26,
    )


def test_part_one():
    test_list = list()
    for k, v in _input_part_one().items():
        test_list.append(v == part_one(k))

    assert all(test_list)


def test_part_two():
    test_list = list()
    for k, v in _input_part_two().items():
        test_list.append(v == part_two(k))

    assert all(test_list)
