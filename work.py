# Segment a
def segment_a():
    a = 1
    b = 2
    c = 5
    while a < c:
        a += 1
        b += c
    print("Segment a output:", a, b, c)

# Segment b
def segment_b():
    d = 4
    e = 6
    f = 7
    while d > f:
        d += 1
        e -= 1
    print("Segment b output:", d, e, f)

# Segment c
def segment_c():
    g = 4
    h = 6
    while g < h:
        g += 1
    print("Segment c output:", g, h)

# Segment d
def segment_d():
    j = 2
    k = 5
    n = 9
    while j < k:
        m = 6
        while m < n:
            print("Goodbye")
            m += 1
        j += 1

# Segment e
def segment_e():
    j = 2
    k = 5
    while j < k:
        m = 6  # Move this line inside the outer loop
        n = 9
        while m < n:
            print("Hello")
            m += 1
        j += 1

# Segment f
def segment_f():
    p = 2
    q = 4
    while p < q:
        print("Adios")
        r = 1  # Move this line inside the outer loop
        while r < q:
            print("Adios")
            r += 1
        p += 1

# Running the segments
segment_a()
segment_b()
segment_c()
segment_d()
segment_e()
segment_f()
