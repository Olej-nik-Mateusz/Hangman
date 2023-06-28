



def visualization(lives):
    mistakes = ["none","|", "O","/|\ ", "/ \ ", "   YOU LOST!" ]
    mistake = ["none", ' ',' ',' ', ' ', ' ' ]
    if lives < 4:
        mistake[1] = mistakes[1]
        if lives <3:
            mistake[1] = mistakes[1]
            mistake[2] = mistakes[2]
            if lives < 2:
                mistake[1] = mistakes[1]
                mistake[2] = mistakes[2]
                mistake[3] = mistakes[3]
                if lives < 1:
                    mistake[1] = mistakes[1]
                    mistake[2] = mistakes[2]
                    mistake[3] = mistakes[3]
                    mistake[4] = mistakes[4]
                    mistake[5] = mistakes[5]

    print("   -----")
    print("  |     "+ mistake[1])
    print("  |     "+ mistake[2])
    print("  |    "+ mistake[3]+mistake[5])
    print("  |    "+mistake[4])
    print("-----")

def visualizationWin():
    print("   -----       YOU WON!")
    print("  |     |")
    print("  |              \O/")
    print("  |               |")
    print("  |              / \ ")
    print("-----")

if __name__ == "__main__":
    visualization(4)
    visualizationWin()
