def main(a):
    # 639
    return (a//100)>(a//10)%10 and (a//100)>(a%10) and (a//10)%10>(a%10)
print(main(int(input())))