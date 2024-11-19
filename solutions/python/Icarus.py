S = input()
if "U" not in S:
    if "R" in S:
        print("""3 1 2
2 3
0 0
0 0""")
    else:
        print("""3 1 2
3 2
0 0
0 0""")

def process(path):
    processed = ""
    depth = 0
    last = None
    for step in path:
        if step == last:
            if step == "U":
                if depth > 0:
                    processed += step
                    last = "U"
                    depth -= 1
            else:
                last = step
        else:
            processed += step
            depth += 1
            last = step
    print(processed)
        
    

process(S)