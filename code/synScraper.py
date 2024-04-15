import sys 

if __name__ == "__main__":
    nqFile = open(sys.argv[1], "r")

    quadruple = nqFile.readlines()

    count = 0
    for line in quadruple: 
        print(line)
        if "synset" in line:
           
            print(count , line)
            count += 1

    nqFile.close()