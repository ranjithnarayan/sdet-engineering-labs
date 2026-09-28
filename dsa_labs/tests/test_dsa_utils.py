import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.dsa_utils import (
    count_chars,
    find_intersection_of_list,
    find_single_occurrence,
    first_non_repeating_char,
    get_all_duplicates,
    get_first_duplicate_in_list,
    get_unique_values,
    is_anagram,
    longest_unique_substr,
    max_sum_subarray,
    union_lists,
)


def test_find_single_occurrence_positive_values():
    assert find_single_occurrence([2, 3, 2]) == 3


def test_find_single_occurrence_positive_larger_input():
    assert find_single_occurrence([4, 1, 4, 7, 1]) == 7


def test_find_single_occurrence_negative_values():
    assert find_single_occurrence([-3, 2, 2]) == -3


def test_find_single_occurrence_without_single_value():
    assert find_single_occurrence([5, 5, 8, 8]) == 0


def test_find_single_occurrence_empty_input_boundary():
    assert find_single_occurrence([]) == 0


def test_count_chars_positive_text():
    assert count_chars("banana") == {"b": 1, "a": 3, "n": 2}


def test_count_chars_positive_mixed_characters():
    assert count_chars("A a!") == {"A": 1, " ": 1, "a": 1, "!": 1}


def test_count_chars_case_sensitive_negative_case():
    assert count_chars("Aa") != {"a": 2}


def test_count_chars_missing_character_negative_case():
    assert "z" not in count_chars("hello")


def test_count_chars_empty_input_boundary():
    assert count_chars("") == {}


def test_first_non_repeating_char_positive():
    assert first_non_repeating_char("swiss") == "w"


def test_first_non_repeating_char_positive_first_character():
    assert first_non_repeating_char("abcd") == "a"


def test_first_non_repeating_char_without_unique_character():
    assert first_non_repeating_char("aabb") is None


def test_first_non_repeating_char_repeated_prefix_negative_case():
    assert first_non_repeating_char("aabbaa") is None


def test_first_non_repeating_char_empty_input_boundary():
    assert first_non_repeating_char("") is None


def test_is_anagram_positive():
    assert is_anagram("listen", "silent") is True


def test_is_anagram_positive_with_repeated_characters():
    assert is_anagram("aabbcc", "abcabc") is True


def test_is_anagram_different_lengths_negative():
    assert is_anagram("cat", "cats") is False


def test_is_anagram_different_character_counts_negative():
    assert is_anagram("aab", "abb") is False


def test_is_anagram_empty_strings_boundary():
    assert is_anagram("", "") is True


def test_get_first_duplicate_in_list_positive():
    assert get_first_duplicate_in_list([2, 1, 3, 2]) == 2


def test_get_first_duplicate_in_list_positive_duplicate_at_end():
    assert get_first_duplicate_in_list([1, 2, 3, 4, 4]) == 4


def test_get_first_duplicate_in_list_without_duplicate():
    assert get_first_duplicate_in_list([1, 2, 3]) is None


def test_get_first_duplicate_in_list_empty_input_negative_case():
    assert get_first_duplicate_in_list([]) is None


def test_get_first_duplicate_in_list_single_item_boundary():
    assert get_first_duplicate_in_list([9]) is None


def test_get_all_duplicates_positive():
    assert get_all_duplicates([1, 2, 1, 3, 2]) == [1, 2]


def test_get_all_duplicates_positive_multiple_repetitions():
    assert get_all_duplicates([4, 4, 4, 5, 5, 6]) == [4, 5]


def test_get_all_duplicates_without_duplicates():
    assert get_all_duplicates([1, 2, 3]) == []


def test_get_all_duplicates_empty_input_negative_case():
    assert get_all_duplicates([]) == []


def test_get_all_duplicates_single_item_boundary():
    assert get_all_duplicates([1]) == []


def test_get_unique_values_positive():
    assert get_unique_values([1, 2, 1, 3, 2]) == [1, 2, 3]


def test_get_unique_values_preserves_first_occurrence():
    assert get_unique_values([3, 1, 3, 2, 1]) == [3, 1, 2]


def test_get_unique_values_all_duplicates_negative_case():
    assert get_unique_values([7, 7, 7]) == [7]


def test_get_unique_values_empty_input_negative_case():
    assert get_unique_values([]) == []


def test_get_unique_values_single_item_boundary():
    assert get_unique_values([42]) == [42]


def test_find_intersection_of_list_positive():
    assert find_intersection_of_list([1, 2, 3], [2, 3, 4]) == [2, 3]


def test_find_intersection_of_list_positive_with_duplicates():
    assert find_intersection_of_list([1, 2, 2, 3], [2, 3, 3]) == [2, 3]


def test_find_intersection_of_list_without_overlap():
    assert find_intersection_of_list([1, 2], [3, 4]) == []


def test_find_intersection_of_list_empty_first_input_negative_case():
    assert find_intersection_of_list([], [1, 2]) == []


def test_find_intersection_of_list_both_empty_boundary():
    assert find_intersection_of_list([], []) == []


def test_union_lists_positive():
    assert union_lists([1, 2], [3, 4]) == [1, 2, 3, 4]


def test_union_lists_positive_with_overlap():
    assert union_lists([1, 2, 2], [2, 3, 1]) == [1, 2, 3]


def test_union_lists_duplicate_only_negative_case():
    assert union_lists([5, 5], [5]) == [5]


def test_union_lists_empty_first_input_negative_case():
    assert union_lists([], [1, 2]) == [1, 2]


def test_union_lists_both_empty_boundary():
    assert union_lists([], []) == []


def test_max_sum_subarray_positive():
    assert max_sum_subarray([2, 1, 5, 1, 3, 2], 3) == 9


def test_max_sum_subarray_positive_negative_numbers():
    assert max_sum_subarray([-2, 4, -1, 3], 2) == 3


def test_max_sum_subarray_zero_k_negative():
    with pytest.raises(ValueError, match="k must be greater than 0"):
        max_sum_subarray([1, 2], 0)


def test_max_sum_subarray_k_larger_than_input_negative():
    assert max_sum_subarray([1, 2], 3) is None


def test_max_sum_subarray_window_of_one_boundary():
    assert max_sum_subarray([4, -1, 7], 1) == 7


def test_longest_unique_substr_positive():
    assert longest_unique_substr("abcabcbb") == 3


def test_longest_unique_substr_positive_all_unique():
    assert longest_unique_substr("abcdef") == 6


def test_longest_unique_substr_repeated_character_negative_case():
    assert longest_unique_substr("aaaa") == 1


def test_longest_unique_substr_empty_input_negative_case():
    assert longest_unique_substr("") == 0


def test_longest_unique_substr_single_character_boundary():
    assert longest_unique_substr("x") == 1