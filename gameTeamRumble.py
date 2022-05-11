def pedirInput(msg):
    inputRetur = str(input(msg))
    return inputRetur


def main():
    totalV = 0
    totalF = 0
    output = ''
    equipoV = pedirInput('')
    equipoF = pedirInput('')
    reloj = pedirInput('')
    for j in reloj:
        if j in equipoV:
            totalV += 1
        if j in equipoF:
            totalF += 1
        if totalV > totalF:
            output = output + 'V'
        elif totalF > totalV:
            output = output + 'F'
        elif totalV == totalF:
            output = output + '≈'
    print(output)


main()
