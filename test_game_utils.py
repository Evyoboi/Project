from game_utils import calculate_score

def test_calculate_score():
    assert calculate_score(3, 1, 1) == 8
    assert calculate_score(0, 0, 3) == 3
    assert calculate_score(2, 2, 0) == 4
