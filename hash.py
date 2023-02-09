
tabuleiro=[1,2,3,4,5,6,7,8,9]
empate=0
jogador=str(input("Digite X ou ● para iniciar a partida:")).upper()
simbolo=jogador 
contador=0

while True:
    if jogador=="X":
        print(f"\n{tabuleiro[0]} {tabuleiro[1]} {tabuleiro[2]}\n{tabuleiro[3]} {tabuleiro[4]} {tabuleiro[5]}\n{tabuleiro[6]} {tabuleiro[7]} {tabuleiro[8]}\n")
        casa=int(input(f"Em qual casa de 1 a 9 você deseja marcar jogador {simbolo}?"))
        simbolo="●"
        if tabuleiro[casa-1]=="●":
            print("A casa está ocupada,escolha novamente!")
            simbolo="X"
            continue
        if tabuleiro[casa-1]=="X":
            print("A casa está ocupada,escolha novamente!")
            simbolo="X"
            continue
        else:
            tabuleiro[casa-1]="X"
            jogador=simbolo
            contador+=1
    elif jogador=="●":
        print(f"\n{tabuleiro[0]} {tabuleiro[1]} {tabuleiro[2]}\n{tabuleiro[3]} {tabuleiro[4]} {tabuleiro[5]}\n{tabuleiro[6]} {tabuleiro[7]} {tabuleiro[8]}\n")
        casa=int(input(f"Em qual casa de 1 a 9 você deseja marcar jogador {simbolo}?"))
        simbolo="X"
        if tabuleiro[casa-1]=="X":
                print("A casa está ocupada escolha novamente!")
                simbolo="●"
                continue
        if tabuleiro[casa-1]=="●":
            print("A casa está ocupada,escolha novamente!")
            simbolo="●"
            continue
        else:
            tabuleiro[casa-1]="●"               
            jogador=simbolo
            contador+=1
                
    if (tabuleiro[0] == tabuleiro[3] and tabuleiro[3] == tabuleiro[6]) or (tabuleiro[1] == tabuleiro[4] and tabuleiro[4] == tabuleiro[7]) or (tabuleiro[2] == tabuleiro[5] and tabuleiro[5] == tabuleiro[8]):
                 if jogador=="●":
                     print("O jogador X venceu a partida!")
                     break
                 if jogador=="X":
                     print("O jogador ● venceu a partida!")
                     break
    if (tabuleiro[0] == tabuleiro[1] and tabuleiro[1] == tabuleiro[2]) or (tabuleiro[3] == tabuleiro[4] and tabuleiro[4] == tabuleiro[5]) or (tabuleiro[6] == tabuleiro[7] and tabuleiro[7] == tabuleiro[8]):
                if jogador=="X":
                    print("O jogador ● venceu a partida!")
                    break
    if (tabuleiro[0] == tabuleiro[4] and tabuleiro[4] == tabuleiro[8]) or (tabuleiro[2] == tabuleiro[4] and tabuleiro[4] == tabuleiro[6]):
                if jogador=="●":
                    print("O jogador X venceu a partida!")
                    break
                if jogador=="X":
                    print("O jogador ● venceu a partida!")
                    break
                
    if contador==9:
                    print("Empate")
                    break
print(f"\n{tabuleiro[0]} {tabuleiro[1]} {tabuleiro[2]}\n{ tabuleiro[3]} {tabuleiro[4]} {tabuleiro[5]}\n{tabuleiro[6]} {tabuleiro[7]} {tabuleiro[8]}\n")