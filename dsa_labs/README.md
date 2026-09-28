# DSA Utilities

Algorithmic techniques used by the utilities in `src/dsa_utils.py`:

- `find_single_occurrence` -> XOR, O(n) time / O(1) space
- `count_chars` -> frequency map
- `first_non_repeating_char` -> two-pass frequency-map pattern
- `is_anagram` -> single-dictionary counting
- `get_first_duplicate_in_list` -> set membership and early return
- `get_all_duplicates` -> preserving duplicate discovery order without O(n^2) list membership
- `get_unique_values` -> preserve first-occurrence order
- `find_intersection_of_list` -> O(n + m) average using sets
- `union_lists` -> order-preserving union
- `max_sum_subarray` -> fixed-size sliding window
- `longest_unique_substr` -> variable-size sliding window