def run():
    pass
#   squares=[]
#   for i in range(1,101):
#       if i % 3 != 0:
#           squares.append(i**2)
# the next line it's the same of the three lines above
    squares=[i**2 for i in range(1,101) if i % 3 != 0]
    nums=[i for i in range (1,9999)if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(squares)
    print("====================================")
    print(nums)

if __name__ == '__main__':
    run()
