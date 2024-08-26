from typing import NamedTuple, Any


class Match(NamedTuple):
    items: list
    label: Any


def matchslice(somelist, conditions):
    """Match des segments de liste.

    Args:
        somelist (list[Any])
        conditions(list[Callable])

    Returns (list[Any])
    """

    matches = []
    for n, i in enumerate(somelist):
        if conditions[0](i):
            s = somelist[n : n + len(conditions)]
            if len(s) < len(conditions):
                continue
            if all([fn(item) for fn, item in zip(conditions, s)]):
                matches.append(s)
    return matches


def matchmany(somelist, patterns):
    """Match des segments de listes.

    Args:
        somelist (list[Any])
        conditions(list[list[Callable]])

    Returns (list[Any])
    """

    matches = []
    for p in patterns:
        matches.extend(matchslice(somelist, p))
    return matches


def matchmanylabeled(somelist, patterns):
    matches = []
    for p, label in patterns:
        m = [Match(i, label) for i in matchslice(somelist, p)]
        matches.extend(m)
    return matches
