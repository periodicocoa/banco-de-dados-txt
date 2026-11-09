#####  Trabalho de Engenharia de Software  #####


### Tema: Loja Virtual ###


# Nome: Felipe Vieira dos Santos
# Nome: Pedro Henrique Lourenço Dias
# Nome: Wesley Matheus dos Santos roque

############ As informações de login estão no arquivo "cadastros.txt", nome e senha ######################
# Bibliotecas
import os
import bib as bib

# Menus
tit = """SISTEMA LOJA DE ROUPA''
Selecione uma opção
[1] Adicionar um Item ao Catalogo
[2] Verificar o Catalogo
[3] Apagar Item do Catalogo
[4] Salvar
[5] Trocar de perfil
"""
titadm = """SISTEMA ADMINISTRADOR
Selecione uma opção
[1] Adicionar perfil
[2] Remover perfil
[3] Ver Perfis
[4] Trocar de perfil
[5] Salvar alterações"""
vercat = """pesquisa por id ou todos os produtos?
[1]Todos os produtos
[2]Pesquisa por id    """
des = "LOJA DE ROUPA"
dados = {}
L1 = {}
historico = []
dados = bib.rd("dados.txt")
vali = False
opt = 0
optadm = 0
carg="null"

# Parte do Cadastrto do Usuario

cre = bib.rd("cadastros.txt")
while True:
    while not vali:
        os.system("cls")
        print("Bem-vindo(a) Faça o login para continuar")

        cd = input("digite o usuario: ")
        cs = input("digite a senha: ")

        try:
            if cre[cd][0] == cs:
                if cre[cd][1] == "1":
                    cargo = "adm"
                    vali = True
                    break
                elif cre[cd][1] == "2":
                    cargo = "estoque"
                    vali = True
                    break
                elif cre[cd][1] == "3":
                    cargo = "vendedor"
                    vali = True
                break
            else:
                print("error")
        except:
            print("error")
        input("Enter para continuar")
    ##programa Usuario
    while cargo == "estoque":
        os.system("cls")
        print(tit)
        try:
            opt = int(input("digite:"))
            if not opt in range(1, 6):
                print("numero não valido")
                input("Enter para continuar")
        except:
            print("opção invalida")
            input("Enter para continuar")

        if opt == 1:
            try:
                a = input("insira o Nome do Produto: ")
            except:
                print("comanado invalido ")
                input("enter para continuar")
                continue
            try:
                b = input("insira o Preço do Produto: ")
            except:
                print("comando invalido")
                input("enter para continuar")
                continue
            try:
                c = input("insira a Quantidade do produto: ")
            except:
                print("comando invalido")
                input("enter para continuar")
                continue
            dados[a] = b, c
            bib.wr("dados.txt", dados)

            # Verificar catalogo
        elif opt == 2:
            os.system("cls")
            pid = input(f"{vercat:<}\nDigite: ")
            if pid == "1":
                for i in dados:
                    print(f"Nome: {i}, Preço: {dados[i][0]}, Quantidade: {dados[i][1]}")
                input("Enter para continuar")
                continue

            elif pid == "2":
                idd = input("Insira o ID desejado: ")
                try:
                    print(
                        f"ID:{idd}, preço:{dados[idd][0]}, quantidade:{dados[idd][1]} "
                    )
                    input("Enter para continuar")
                except:

                    print("Id invalido")
                    input("Enter para continuar")
                    continue

                # Apagar itens do catalogo
        elif opt == 3:
            cdel = input("Digite o codigo do item a ser deletado")
            try:
                print(
                    f"Atenção, o seguinte produto será deletado: id:{cdel} preço:{dados[cdel][0]}"
                )
                confdel = input("deseja apagar mesmo assim?\n[1]sim\n[2]não\nDigite: ")
                if confdel == "1":
                    del dados[cdel]
                    print("Deletedo")
                    input("enter para continuar")
                    continue
            except:
                print("ID invalido")
                input("Enter para continuar")
                continue
            else:
                continue

        elif opt == 4:
            ex = input("Deseja salvar as alteraçoes?\n[1]sim\n[2]não\nDigite: ")
            if ex == "1":
                bib.wr("dados.txt", dados)
                print("Salvo com sucesso")
                input("Enter para continuar")
                continue
            else:
                print("Dados não salvos")
                input("Enter para continuar")
                continue

        elif opt == 5:
            vali = False
            cargo = "null"
        else:
            print("Numero não valido")
            input("Enter para continuar")
            continue
    ##Programa Administrador
    while cargo == "adm":
        optadm=0
        os.system("cls")
        print(titadm)
        try:
            optadm = int(input("digite:"))
        except:
            print("opção invalida")
            input("Enter para continuar")
        if not optadm in range(1, 6):
            print("numero não valido")
            input("Enter para continuar")
        os.system("cls")
        if optadm == 1:
            np = input(f"Nome do perfil: ")
            sp = input("Senha do perfil: ")
            try: 
                ap = input("Qual a função do usuario? \n [1]Adm \n [2]Estoquista \n [3]Vendedor \n Digite: ")
                if ap not in range(1, 4):
                    raise ValueError
            except:
                print("Cargo não reconhecido")
                input("Enter para continuar")
                break
            cre[np] = sp, ap
            print("usuario criado")
            input("Enter para continuar")
        elif optadm == 2:
            dp = input("Nome do perfil a ser apagado: ")
            if dp in cre:
                confd = int(
                    input(
                        f"o seguinte perfil {dp} sera apagado, tem certeza? \n[1]sim \n[2]não\nDigite: "
                    )
                )
                if confd == 1:
                    del cre[dp]
                    print("Apagado")
                    input("Enter para continuar")
                else:
                    print("Não apagado")
                    input("Enter para continuar")
        elif optadm == 3:
            for i in cre:
                if cre[i][1] == "1":
                    carg = "ADM"
                elif cre[i][1] == "2":
                    carg = "Estoquista"
                elif cre[i][1] == "3":
                    carg = "Vendedor"
                    
                print(f"Nome:{i} Senha: {cre[i][0]} Cargo:{carg}")
            input("Enter para continuar")
        elif optadm == 4:
            vali = False
            break
        elif optadm == 5:   
            ex = input("Deseja salvar as alteraçoes?\n[1]sim\n[2]não\nDigite: ")
            if ex == "1":
                bib.wr("cadastros.txt", cre)
                print("Salvo com sucesso")
                input("Enter para continuar")
                continue
        else:
            print("Numero não valido")
            input("Enter para continuar")
            continue
    ##Programa Vendedor
    while cargo == "vendedor":
        os.system("cls")
        print(f"""
        =========================================
        {des.center(45)}
         =========================================
        """)
        print("""
        1-consultar produtos da loja
        2-comprar produtos
        3-minhas compras
        4-alterar perfil
        
        """)
        op = input("Opção: ")
        if op == "1":

            with open("dados.txt", "r") as arquivo:
                for linha in arquivo:
                    nome, preco, estoque = linha.strip().split(",")
                    print(f"{nome} | R$ {float(preco):.2f} | Estoque: {estoque}")
                input("Enter para continuar")

        elif op == "2":
            produtos = []

            with open("dados.txt", "r") as arq:
                for linha in arq:
                    produtos.append(linha.strip().split(","))

            for p in produtos:
                print(f"{p[0]} | R$ {float(p[1]):.2f} | Estoque: {p[2]}")
            nome = input("\nProduto: ")
            qtd = int(input("Quantidade: "))
            encontrado = False
            for p in produtos:
                if p[0].lower() == nome.lower():
                    encontrado = True

                    estoque = int(p[2])

                    if qtd > estoque:
                        print("Estoque insuficiente.")
                        input("Enter para continuar")
                        break

                    total = float(p[1]) * qtd
                    print(f"Total: R$ {total:.2f}")

                    print("\n1 - Dinheiro")
                    print("2 - Cartão")
                    pag = input("Pagamento: ")

                    if pag == "1":
                        valor = float(input("Valor recebido: R$ "))
                        troco = valor - total

                        if troco < 0:
                            print("Valor insuficiente.")
                            break

                        print(f"Troco: R$ {troco:.2f}")
                        input("Enter para continuar")

                    elif pag == "2":
                        parcelas = int(input("Parcelas: "))

                        if parcelas <= 3:
                            print(f"{parcelas}x de R$ {(total / parcelas):.2f}")
                            input("Enter para continuar")
                        else:
                            total = total * 1.10
                            print(f"{parcelas}x de R$ {(total / parcelas):.2f}")

                    p[2] = str(estoque - qtd)

                    historico.append(f"{nome} - {qtd} unidade(s) - R$ {total:.2f}")

                    with open("dados.txt", "w") as arq:
                        for item in produtos:
                            arq.write(",".join(item) + "\n")

                    print("Compra realizada!")
                    input("Enter para continuar")
                    break

            if not encontrado:
                print("Produto não encontrado.")
                input("Enter para continuar")
        elif op == "3":
            print("\n=== HISTÓRICO ===")
            if len(historico) == 0:
                print("Nenhuma compra realizada.")
            for compra in historico:
                print(compra)
                input("Enter para continuar")

        elif op == "4":
            vali = False
            cargo = "null"
            input("Enter para continuar")
            break
        elif op == "5":
            ex = input("Deseja salvar as alteraçoes?\n[1]sim\n[2]não\nDigite: ")
            if ex == "1":
                bib.wr("dados.txt", dados)
                print("Salvo com sucesso")
                input("Enter para continuar")
                continue
            
        else:
            print("Opção inválida.")
            input("Enter para continuar")
