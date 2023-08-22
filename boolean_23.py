def main(a):
    return (999<a<10000) and (a//1000)==(a%10) and (a//100)%10==(a//10)%10
print(main(int(input())))