import os

def find_single_occurrence(nums):
    result = 0

    for num in nums:
        result ^= num

    return result


def count_chars(text):
    char_count = {}

    for char in text:
        char_count[char] = char_count.get(char, 0) + 1

    return char_count


def first_non_repeating_char(text):
    char_count = count_chars(text)

    for char in text:
        if char_count[char] == 1:
            return char

    return None


def is_anagram(text1, text2):
    if len(text1) != len(text2):
        return False

    char_count = {}

    for char in text1:
        char_count[char] = char_count.get(char, 0) + 1

    for char in text2:
        if char not in char_count:
            return False

        char_count[char] -= 1

        if char_count[char] < 0:
            return False

    return True


def get_first_duplicate_in_list(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return num

        seen.add(num)

    return None


def get_all_duplicates(nums):
    seen = set()
    added = set()
    duplicates = []

    for num in nums:
        if num in seen and num not in added:
            duplicates.append(num)
            added.add(num)

        seen.add(num)

    return duplicates


def get_unique_values(nums):
    seen = set()
    unique = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            unique.append(num)

    return unique


def find_intersection_of_list(a, b):
    b_set = set(b)
    added = set()
    intersection = []

    for num in a:
        if num in b_set and num not in added:
            intersection.append(num)
            added.add(num)

    return intersection


def union_lists(a, b):
    seen = set()
    result = []

    for num in a:
        if num not in seen:
            seen.add(num)
            result.append(num)

    for num in b:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result


def max_sum_subarray(arr, k):
    if k <= 0:
        raise ValueError("k must be greater than 0")

    if len(arr) < k:
        return None

    window_sum = 0

    for i in range(k):
        window_sum += arr[i]

    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


def longest_unique_substr(text):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(text)):
        while text[right] in seen:
            seen.remove(text[left])
            left += 1

        seen.add(text[right])
        max_len = max(max_len, right - left + 1)

    return max_len
