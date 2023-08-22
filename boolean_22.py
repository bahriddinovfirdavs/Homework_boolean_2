def main(a):
    return (99<a<1000) and ((a//100)>(a//10)%10 and (a//100)>(a%10) and (a//10)%10>(a%10)) or ((a//100)<(a//10)%10 and (a//100)<(a%10) and (a//10)%10<(a%10))
print(main(int(input())))