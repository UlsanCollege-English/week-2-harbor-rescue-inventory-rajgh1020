
"""Week 2 starter code for Harbor Rescue Inventory."""

from __future__ import annotations

from subprocess import check_output


def mission_snapshot(items: list[object]) -> tuple[object | None, object | None]:
    """Return the first and last items in the list.

    Return (None, None) if the list is empty.
    """
    try:
        return (items[0], items[-1])

    except IndexError:
        return(None, None)

    raise NotImplementedError


def cargo_window(items: list[object], start: int, size: int) -> list[object]:
    """Return up to ``size`` items starting at index ``start``.

    Return an empty list if ``start`` is out of range or if ``size <= 0``.

    """
    if start < 0 or start >= len(items) or size <= 0:
        return []

    return items[start:start + size]
    raise NotImplementedError


def first_supply_index(items: list[object], target: object) -> int:
    """Return the index of the first occurrence of ``target``.

    Return -1 if the target is not found.
    Do not use ``items.index(...)`` for this challenge.
    """
    idx = 0

    for item in items:
        if item == target:
            return idx
        idx += 1
    return -1

    raise NotImplementedError


def supply_report(items: list[object], target: object) -> tuple[int, int]:
    """Return (count, first_index) for ``target`` in ``items``.

    Return (0, -1) if the target does not appear.
    """
    count = 0
    idx = 0
    first_index = -1

    for item in items:
        if item == target:
            count += 1
            if first_index == -1:
                first_index = idx
        idx += 1

    return (count, first_index)
    raise NotImplementedError


def priority_load(items: list[object], urgent_item: object) -> list[object]:
    """Return a new list with ``urgent_item`` added at the front.

    Do not mutate the original input list.
    This is a stretch challenge.
    """
    new_list = [urgent_item]
    for item in items:
        new_list.append(item)
    return new_list
    raise NotImplementedError