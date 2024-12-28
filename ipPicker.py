import random
availableProxy = {1:{"ip":"45.32.86.6","port":"31280"},2:{"ip":"45.32.231.36","port":"31280"},3:{"ip":"199.247.13.177","port":"31280"},4:{"ip":"136.68.111.53","port":"31280"},5:{"ip":"128.199.36.195","port":"31280"},6:{"ip":"45.63.75.212","port":"31280"}}
def pick():
    randIndex = random.randint(1,6)
    return (f'{availableProxy[randIndex]["ip"]}:{availableProxy[randIndex]["port"]}')

def main():
    pick()
    
if __name__ == "__main__":
    main()