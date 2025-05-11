# Just remove it entirely (safe for Windows)
"""
Generate leftmost and rightmost derivations for
L = { (aa)^n  cc  (bb)^m  | n ≥ 1, m ≥ 1 }

Grammar:
  S → A C B
  A → aa A | aa
  C → cc
  B → B bb | bb
"""

def leftmost_derivation(n, m):
    """Return list of sentential forms in a leftmost derivation for given n, m."""
    steps = []

    # Start with the start symbol
    current = ['S']
    steps.append(' '.join(current))

    # S → A C B
    current = ['A', 'C', 'B']
    steps.append(' '.join(current))

    # Expand A → aa A (n-1) times using leftmost rule
    for _ in range(n - 1):
        i = current.index('A')  # always expand the leftmost A
        current = current[:i] + ['aa', 'A'] + current[i + 1:]
        steps.append(' '.join(current))

    # Last A → aa
    i = current.index('A')
    current = current[:i] + ['aa'] + current[i + 1:]
    steps.append(' '.join(current))

    # C → cc
    i = current.index('C')
    current = current[:i] + ['cc'] + current[i + 1:]
    steps.append(' '.join(current))

    # Expand B → B bb (m-1) times using leftmost rule
    for _ in range(m - 1):
        i = current.index('B')
        current = current[:i] + ['B', 'bb'] + current[i + 1:]
        steps.append(' '.join(current))

    # Last B → bb
    i = current.index('B')
    current = current[:i] + ['bb'] + current[i + 1:]
    steps.append(' '.join(current))

    return steps

def rightmost_derivation(n, m):
    """Return list of sentential forms in a rightmost derivation for given n, m."""
    steps = []

    # Start with the start symbol
    current = ['S']
    steps.append(' '.join(current))

    # S → A C B
    current = ['A', 'C', 'B']
    steps.append(' '.join(current))

    # Expand B → B bb (m-1) times using rightmost rule
    for _ in range(m - 1):
        current = current[:-1] + ['B', 'bb']  # replace rightmost B
        steps.append(' '.join(current))

    # Last B → bb
    current = current[:-1] + ['bb']
    steps.append(' '.join(current))

    # C → cc (C is now the rightmost non-terminal)
    j = current.index('C')
    current = current[:j] + ['cc'] + current[j + 1:]
    steps.append(' '.join(current))

    # Expand A → aa A (n-1) times using rightmost rule
    for _ in range(n - 1):
        j = max(i for i, symbol in enumerate(current) if symbol == 'A')  # rightmost A
        current = current[:j] + ['aa', 'A'] + current[j + 1:]
        steps.append(' '.join(current))

    # Last A → aa
    j = current.index('A')
    current = current[:j] + ['aa'] + current[j + 1:]
    steps.append(' '.join(current))

    return steps

def print_steps(label, steps):
    """Prints the derivation steps with a label."""
    print(f"\n=== {label} ===")
    for i, form in enumerate(steps):
        print(f"{i:2d}: {form}")

if __name__ == "__main__":
    # Example 1: n = 2, m = 2 → Expected string: aaaa cc bbbb
    n1, m1 = 2, 2
    lm1 = leftmost_derivation(n1, m1)
    rm1 = rightmost_derivation(n1, m1)

    print_steps("Leftmost Derivation (n=2, m=2)", lm1)
    print_steps("Rightmost Derivation (n=2, m=2)", rm1)

    # Example 2: n = 3, m = 1 → Expected string: aaaaaa cc bb
    n2, m2 = 3, 1
    lm2 = leftmost_derivation(n2, m2)
    rm2 = rightmost_derivation(n2, m2)

    print_steps("Leftmost Derivation (n=3, m=1)", lm2)
    print_steps("Rightmost Derivation (n=3, m=1)", rm2)
