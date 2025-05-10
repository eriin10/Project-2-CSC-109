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
    # start
    current = ['S']
    steps.append(' '.join(current))

    # S → A C B
    current = ['A','C','B']
    steps.append(' '.join(current))

    # Expand A → aa A, (n−1) times
    for _ in range(n-1):
        i = current.index('A')
        current = current[:i] + ['aa','A'] + current[i+1:]
        steps.append(' '.join(current))
    # Last A → aa
    i = current.index('A')
    current = current[:i] + ['aa'] + current[i+1:]
    steps.append(' '.join(current))

    # C → cc
    i = current.index('C')
    current = current[:i] + ['cc'] + current[i+1:]
    steps.append(' '.join(current))

    # Expand B → B bb, (m−1) times
    for _ in range(m-1):
        i = current.index('B')
        current = current[:i] + ['B','bb'] + current[i+1:]
        steps.append(' '.join(current))
    # Last B → bb
    i = current.index('B')
    current = current[:i] + ['bb'] + current[i+1:]
    steps.append(' '.join(current))

    return steps

def rightmost_derivation(n, m):
    """Return list of sentential forms in a rightmost derivation for given n, m."""
    steps = []
    current = ['S']
    steps.append(' '.join(current))

    # S → A C B
    current = ['A','C','B']
    steps.append(' '.join(current))

    # Expand B → B bb, (m−1) times
    for _ in range(m-1):
        # rightmost non-terminal is B at end
        current = current[:-1] + ['B','bb']
        steps.append(' '.join(current))
    # Last B → bb
    current = current[:-1] + ['bb']
    steps.append(' '.join(current))

    # C → cc  (now rightmost NT is C)
    # find C
    j = current.index('C')
    current = current[:j] + ['cc'] + current[j+1:]
    steps.append(' '.join(current))

    # Expand A → aa A, (n−1) times, but always the rightmost A
    for _ in range(n-1):
        # find rightmost A
        j = max(i for i,symbol in enumerate(current) if symbol=='A')
        current = current[:j] + ['aa','A'] + current[j+1:]
        steps.append(' '.join(current))
    # Last A → aa
    j = current.index('A')
    current = current[:j] + ['aa'] + current[j+1:]
    steps.append(' '.join(current))

    return steps

def print_steps(label, steps):
    print(f"\n=== {label} ===")
    for i, form in enumerate(steps):
        print(f"{i:2d}: {form}")

if __name__ == "__main__":
    # Example: n=2 (two 'aa's), m=2 (two 'bb's) → string = "aaaa cc bbbb"
    n, m = 2, 2

    lm = leftmost_derivation(n, m)
    rm = rightmost_derivation(n, m)

    print_steps("Leftmost Derivation", lm)
    print_steps("Rightmost Derivation", rm)
