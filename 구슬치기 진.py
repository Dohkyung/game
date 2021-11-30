while True:
    print("=============================================")
    print()
    print("구슬치기-홀짝게임")
    print()
    print("시작:any number key, 종료:press any key except number")
    START = int(input("숫자를 입력하시오: "))
    print("=============================================")

    t = 0
    print()
    import random

    x = input("1번 플레이어 이름을 입력하시오: ")
    y = input("2번 플레이어 이름을 입력하시오: ")

    preemptive_strike = random.randint(1, 2)
    OK = int(input("\n'1'을 누르면 시작"))
    print()
    if OK == 1:
        if preemptive_strike == 1:
            print(x, " 이(가) 선공입니다.")
    if preemptive_strike == 2:
        print(y, " 이(가) 선공입니다.")

    while True:
        t = t + 1
        print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
        print()
        print("%d번째 라운드입니다." % t)
        if preemptive_strike % 2 != 0:
            print(x, " 의 공격차례입니다.")
        else:
            print(y, " 의 공격차례입니다.")
        p1 = int(input("\n공격자의 구슬"))
        p2 = int(input("수비자의 구슬"))
        ball = int(input("\n수비자가 걸 구슬(5개 이하)"))
        if ball % 2 == 0:
            print("짝수\n\n(홀수/짝수)")
        else:
            print("홀수\n\n(홀수/짝수)")

        ans = input("")
        if ans == "짝수" and ball % 2 == 0:
            p1 = p1 + ball
            p2 = p2 - ball
            print("\n공격 성공")
        elif ans == "홀수" and ball % 2 != 0:
            p1 = p1 + ball
            p2 = p2 - ball
            print("\n공격 성공")
        else:
            print("\n공격 실패")
            p1 = p1 - ball
            p2 = p2 + ball

        if ans == "짝수" and ball % 2 == 0 or ans == "홀수" and ball % 2 != 0:
            preemptive_strike = preemptive_strike + 1
            print("공격", p1, "개", "수비", p2, "개")
        else:
            preemptive_strike = preemptive_strike + 1
            print("공격", p1, "개", "수비", p2, "개")

        if p1 <= 0:
            print("\n게임오버")
            print("%d라운드 끝에 승부가 결정되었습니다" % t)
            break
        elif p2 <= 0:
            print("\n게임오버")
            print("%d라운드 끝에 승부가 결정되었습니다" % t)
            break
        else:
            print("\n다음 라운드 \n공수 교대\n")