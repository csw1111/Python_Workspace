import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import random

plt.rc('font', family='Malgun Gothic')

bn = 10 # 버튼개수
pslst = [0]*100 # 어느 퍼센트변수가 가장 많이 수익을 실현하는 저장하기위한 배열
plst2 = [0.0]*100 # 1부터 100퍼센트 변수들 반복 값들 모두 저장하는 배열
blst  = [0]*bn # 버튼의 펴센트를 저장하기위한 배열
rept = 10 # 반복횟수

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
                    plst[i] = plst[i] * (1+((101-blst[y])/100))
                    # I = random.randint(1,100)/100
                    # plst[i] = plst[i] * (1+I)
                else:
                    plst[i] = plst[i] * (1-(blst[y]/100))
                    # K = random.randint(1,100)/100
                    # plst[i] = plst[i]*(1-(K))
        plst2[i] += plst[i]/rept
        
    idx = plst.index(max(plst)) # pslt(퍼센트변수의 값을 저장한 배열)배열에 가장 큰 값의 인덱스를 저장하는 변수
    # pslst배열의 인덱스가 idx인 요소에 1을 더하는 코드
    pslst[idx] += 1 
    # print(max(plst))
    # print(plst)
# pslst배열의 가장 큰 값에 1을 더한 값 출력(인덱스는 0부터 시작하기 떄문에 1을 더함)
print(pslst.index(max(pslst))+1)
print(pslst)
# plst2배열의 가장 큰 값에 1을 더한 값 출력
print(plst2.index(max(plst2))+1)
print(plst2)

# x축의 값을 저장
x1 = [i+1 for i in range(100)]
# y축의 값을 저장


# 데이터 생성
y1 = [x for x in plst2]
y2 = [x for x in pslst]

# 첫 번째 그래프 생성
fig, ax1 = plt.subplots(figsize=(8, 4))

for i in range(len(x1)):
    height = y1[i]
    ax1.text(x1[i], height + 0.01, '%.1f' %height, ha='center', va='bottom', size = 12, color = "blue")

ax1.plot(x1, y1, label='수익', color='blue', linestyle='--')
ax1.set_xlabel('x')
ax1.set_ylabel('수익', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
# x 축 범위를 설정합니다.
ax1.set_xlim(1, 100)

# x 축에 주 눈금을 설정합니다. (2 간격)
ax1.set_xticks(range(1, 101, 2))


# 두 번째 그래프 및 보조 축 생성
ax2 = ax1.twinx()

for i in range(len(x1)):
    height = y2[i]
    ax2.text(x1[i], height + 0.01, '%.1f' %height, ha='center', va='bottom', size = 12, color = "red")

ax2.plot(x1, y2, label='가장 큰 수익을 가진 퍼센트 개수', color='red', linestyle='-')
ax2.set_ylabel('가장 큰 수익을 가진 퍼센트 개수', color='red')
ax2.tick_params(axis='y', labelcolor='red')


# 그래프 제목과 범례 설정
fig.suptitle('최소선택확률의 결과')
fig.legend(loc='upper right')

# 그래프 표시
plt.show()