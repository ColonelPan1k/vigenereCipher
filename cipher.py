def encrypt(inputStr, shift):
    outputStr = ''
    for i in range(len(inputStr)):
        chrNum = ((ord(inputStr[i]) + shift - 97) % 26) + 97
        outputStr += chr(chrNum)
    return outputStr

def decrypt(inputStr, shift):
    outputStr = ''
    for i in range(len(inputStr)):
        chrNum = ((ord(inputStr[i]) - shift - 97) % 26) + 97
        outputStr += chr(chrNum)
    return outputStr

def vignereEncrypt(message, codeList):
    storeMessage = list(message)
    finalMessage = ''
    for j in range(len(message)):
        storeMessage[j] = encrypt(storeMessage[j], codeList[(j % len(codeList))])
        finalMessage += storeMessage[j]
    return finalMessage

def vignereDecrypt(message, codeList):
    decryptList = list(codeList)
    storeDec = list(message)
    finalDec = ''
    # storeDec[0] = decrypt(message,codeList[0])
    for j in range(len(storeDec)):
        storeDec[j] = decrypt(storeDec[j], codeList[(j % len(codeList))])
        finalDec += storeDec[j]
    return finalDec.upper()

def charTonum(word):
    keyList = []
    for i in range(len(word)):
        keyList.append(ord(word[i]) - 97)
    return keyList

input_message = input("Enter your message to encrypt (No Spaces): ")
encOrDec = input("Would you like to Encrypt or decrypt your message? [e/d]: ")
# key = [int(x) for x in input("Enter your secret key: ").split()]
key = charTonum(input('Enter your key: '))
print(input_message)

if encOrDec == 'e':
    vignere = vignereEncrypt(input_message, key)
    print(vignere)
if encOrDec == 'd':
    vignereDec = vignereDecrypt(input_message, key)
    print(vignereDec)

