def print_matrix(m: list[list[int]]):
    for row in m:
        print("".join(map(lambda el: str(el).ljust(3), row)))

def print_path(d: list[float], p: list[int|None], start: int, end: int):
    tmp = end
    path = [] 
    while(tmp != None):
        path.append(str(tmp))
        tmp = p[tmp]
    path.reverse()
    print(f"d({end})\t= {d[end]}\t ==> [{" - ".join(path)}]")
