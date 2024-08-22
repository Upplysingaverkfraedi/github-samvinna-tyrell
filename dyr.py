import sys

def default():
    print('halló hæ')
def kottur():
    print('Mjá Mjá')
def main():
    if sys.argv[1]== 'kottur':
        kottur()
    else:
        default()

if __name__ == '__main__':
    main()
