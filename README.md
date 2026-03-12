[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/HYC1dWeQ)
# Week 2 README Template

## Summary
This assignment is about working with lists in Python.
The functions help find items in a list, count how many times something appears, and get parts of the list.
It also checks the first and last items in the list.
The stretch function adds an urgent item to the front of the list without changing the original list.
## Approach
Use bullets to explain how each function works.

- `mission_snapshot`: This function returns the first and last items of the list. If the list is empty, it returns (None, None).
- `cargo_window`:This function returns some items from the list starting at a certain index.
- `first_supply_index`:This function goes through the list and finds the first place where the target item appears. If it is not found, it returns -1.
- `supply_report`:This function counts how many times the target item appears in the list and also returns the first index where it appears.
- `priority_load` (stretch):This function creates a new list with the urgent item added at the front. It does not change the original list.

## Complexity reasoning

| Function | Time complexity | Why |
|---|---|---|
| `mission_snapshot` |O(1)  |It only checks the first and last items.  |
| `cargo_window` |  O(k)| It returns part of the list. |
| `first_supply_index` |  O(n)| It may need to check every item in the list. |
| `supply_report` | O(n) |It loops through the whole list to count items.  |
| `priority_load` (stretch) | O(n) |It copies all items into a new list.  |

## Edge-case checklist
Mark the cases you tested.

- [x] empty list
- [x] one-item list
- [x] target missing
- [x] repeated values
- [x] slice goes past end
- [x] size is zero
- [x] size is negative
- [x] original list unchanged in `priority_load`

## Assistance / Sources
List any help you used and what kind of help it gave.

- Person / tool / website:ChatGPT
  - Help received:It helped me to properly document and rate the code in advance.

- Person / tool / website:w3schools
  - Help received:Information about the `try` and `expect`,