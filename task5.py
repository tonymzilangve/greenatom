def version_comparison(v1: str, v2: str) -> int:
    return -1 if v1 < v2 else 0 if v1 == v2 else 1


if __name__ == '__main__':
    v1 = input()
    v2 = input()

    print(version_comparison(v1, v2))
