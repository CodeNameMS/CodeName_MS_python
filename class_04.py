# print("기본 값 :%d" % 123) #기본값 출력
# print("설정 값 :%5d" % 123) #왼쪽부터 5칸을 확보하고 출력
# print("설정 값 :%05d" % 123) #왼쪽부터 5칸을 확보하고 빈자리는 0으로 출력
# print("설정 값 :%5d%5d" % (123,123)) #좌측정렬 2개 숫자 출력
# print("설정 값 :%-5d%-5d" % (123,123))#우측정렬 2개 숫자 출력

# print("기본 값 :%f" % 123.45678)
# print("설정 값 : %10.3f" % 123.45678)
# print("설정 값 :%2.1f" % 123.45678)
# print("설정 값 :%.2f" % 123.45678) #가장 많이 쓰임,

# print("12345678901234567890123456789012345678901234567890")
# print("%10s%10s"%("대한민국","만세"))
# print("기본 값 :%s" % "python test")
# print("설정 값 :%20.4s" % "python test")

#===============================================
# print("========== 출력 결과 ==========")
# print("%s"%("이름\t:"),"%s"%("홍길동"))
# print("%s"%("나이\t:"),"%d"%20)
# print("%s"%("tel\t:"),"%03d"%10,print(""),"%0.0f"%(1234),int("%s",%1234))
#================================================
# print("==========출력 결과==========")
# print("이름 \t: %s"%"홍길동")
# print("%-5s %-10s"% ("이름",': 홍길동'))
# print("나이 \t: %d"%20)
# print("나이 \t: %s"%"20")
# print("Tel \t: %s"%"010-1234-1234")
# print("Tel \t: 0%d-%d-%d"%(10,1234,1234))
# print("Tel \t: %03d-%d-%d"% (10,1234,1234))
# print("키 \t: %.1f"%178.5)
# print("몸무게 \t: %d"%75)
# print("혈액형 \t: %s"%"O")

#  변수의 이름은 알파벳, 숫자, 언더바(_)로 구성
#  대소문자 구분
#  변수의 이름은 숫자로 시작할 수 없음
#  키워드(예약어)는 변수이름으로 사용 불가능
#  공백이나 특수 기호는 포함될 수 없음
#  예약어
#  프로그래밍 언어 중에서 의미가 고정되어 있고, 사용자가 작성하는
# 프로그램 상태에 따라서 의미를 변경할 수 없는 단어
# 변수명 작명요령 (절대규칙 아님)
# 1) 변수명은 프로그램 내에서 어떤 내용이 담기는지 또는
#    어떤 역할을 하는지 누가봐도 쉽게 연상할 수 있도록 
#    지어주는것이 바람직하다.
# 2) 한글변수는 사용가능하다, 하지만 프로그램 작성시 
#    가급적 사용하지 않는것이 바람직하다.

# num = 10
# print("정수 형 변수 사용 : %d" %num)
# print("정수 형 변수 사용 : ",num)

# num = 5
# print("변경 전 num : ",num)
# num = num + 10
# print("변경 후 num : ",num)

# num1 = 5
# num2 = 10
# sum_ = num1+num2
# print("id num1 : ",id(num1)) #id = 메모리에 할당된 주소, C언어의 포인터와는 다름
# print("id num2 : ",id(num2))
# print("id sum : ",id(sum_))

# num1 = 10
# num2 = 20
# sum_ = num1 + num2
# print("num1(%d) + num2(%d) = %d" %(num1,num2,sum_))
# print("num1(",num1,")+num2(",num2,")=",num1+num2) #문자열 구분을 위해 사이에 ,(콘마)를 사용

# num1 = 7
# num2 = 5
# sum_ = num1 + num2
# avg = num1 / num2
# gap = num1 - num2
# double = num1*num2
# print("num1(%d) + num2(%d) = %d" %(num1,num2,sum_))
# print("num1(%d) / num2(%d) = %.2f" %(num1,num2,avg))
# print("num1(%d) - num2(%d) = %d" %(num1,num2,gap))
# print("num1(%d) * num2(%d) = %d" %(num1,num2,double))

# gum = 100
# age = 27
# python = 100
# C = 95
# Java = 85
# avg = (python+C+Java)/3
# print("파이썬 %d점" %gum)
# print("나는 %d살이다."%age)
# print("파이썬 %d점 + C언어 %d점 + Java %d점 = 평균 %.2f\n"%(python,C,Java,avg))

# J = 11
# T = 37
# avg = T / J
# print("한 개의 지하철을 지나는데 평균 %.2f분이 걸렸다" %avg)