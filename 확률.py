import random 
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

bn = 1000 # 버튼개수
pslst = [0]*100 # 어느 퍼센트변수가 가장 많이 수익을 실현하는 저장하기위한 배열
blst  = [0]*bn # 버튼의 펴센트를 저장하기위한 배열
rept = 1000 # 반복횟수

# 반복하는 코드
for x in range(rept):

    #버튼의 퍼센트를 난수로 저장하는 코드
    for j in range(bn):
        blst[j] = random.randint(0,100)

    # 퍼센트변수 값 저장하기위한 배열
    plst = [100.0]*100
    
    for i in range(0,100):
        for y in range(bn):

            # i+1값(퍼센트변수 값)보다 blst[y]값이 크면 blst[y]의 확률로 수익을 얻거나 수익을 잃는 코드
            if(i+1<=blst[y]):
                rint = random.randint(1,100)
                if(rint<=blst[y]):
                    # plst[i] = plst[i] * (1+((101-blst[y])/100))
                    I = random.randint(1,100)/100
                    plst[i] = plst[i] * (1+I)
                else:
                    # plst[i] = plst[i] * (1-(blst[y]/100))
                    K = random.randint(1,100)/100
                    plst[i] = plst[i]*(1-(K))

    idx = plst.index(max(plst)) # pslt(퍼센트변수의 값을 저장한 배열)배열에 가장 큰 값의 인덱스를 저장하는 변수
    # pslst배열의 인덱스가 idx인 요소에 1을 더하는 코드
    pslst[idx] += 1 
    # print(max(plst))
    # print(plst)
# pslst배열의 가장 큰 값에 1을 더한 값 출력(인덱스는 0부터 시작하기 떄문에 1을 더함)
print(pslst.index(max(pslst))+1)
print(pslst)

# x축의 값을 저장
x1 = [i+1 for i in range(100)]
# y축의 값을 저장
y1 = [x for x in pslst]
# print(y1, len(y1))
# print(len(x1), print(len(y1)))

#그래프 크기 지정
plt.figure(figsize=(100, 20))
# x에 대응하는 y값을 보여주는 코드
for i in range(len(x1)):
    height = y1[i]
    plt.text(x1[i], height + 0.01, '%.1f' %height, ha='center', va='bottom', size = 12)

# x축의 눈금 값의 크기 지정(1부터 100까지 2간격으로 보여줌)
plt.xticks(np.arange(1,101,2), fontsize = 15)
# x축의 눈금 값의 기울기를 지정(세로로)
plt.xticks(rotation=90)

# 그래프 그리기
plt.plot(x1, y1, color='red', marker='o')
#제목
plt.title("가장 높은 확률", fontsize = 30)
# x축 
plt.xlabel("확률", fontsize = 15)
# y축
plt.ylabel("개수", fontsize = 15)
# 그래프 보여주기
plt.show()

# 가장 큰 값이 중복되면 가장 처음 값의 인덱스가 저장된다