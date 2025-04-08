import subprocess as s, threading as t, sys as y

p = []

def f(x, i, size):
    q = s.Popen(["ping", x, "-t", "-l", str(size)], stdout=s.PIPE, stderr=s.PIPE, universal_newlines=True)
    p.append(q)
    try:
        for l in q.stdout:
            print(f"[T{i}] {l}", end="")
    except Exception as e:
        print(f"E {i}: {e}")

def m():
    x = input("Target: ").strip()
    if not x:
        print("No target. Exiting.")
        y.exit(1)
    
    n = input("Threads (default 1): ").strip()
    try:
        c = int(n) if n else 1
    except ValueError:
        print("Invalid. Using 1.")
        c = 1
    
    s = input("Packet size (max 65500): ").strip()
    try:
        size = int(s) if s else 65500
        if size > 65500:
            print("Size too large. Using 65500.")
            size = 65500
    except ValueError:
        print("Invalid size. Using 65500.")
        size = 65500

    z = []
    for i in range(c):
        d = t.Thread(target=f, args=(x, i + 1, size), daemon=True)
        d.start()
        z.append(d)

    print(f"\n{c} thread(s) -> {x} with packet size {size}")
    print("Ctrl+C to stop.\n")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nStopping...")
        for q in p:
            q.kill()
        y.exit(0)

if __name__ == "__main__":
    m()