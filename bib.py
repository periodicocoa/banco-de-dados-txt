def rd(dado):
    
    y = {}

    with open(dado, "r") as RS:
        for linha in RS:
            linha = linha.strip()
            if linha == "":
                continue
            dados = [x.strip() for x in linha.split(",")]
            y[dados[0]] = (dados[1], dados[2])

    return y
def wr(dado, x):
    vx=[]
    for i,a in x.items():
        vx.append(f"{i}, {a[0]}, {a[1]}")
    with open(dado, "w") as A:
        for i in vx:
            A.write(str(i)+"\n")
