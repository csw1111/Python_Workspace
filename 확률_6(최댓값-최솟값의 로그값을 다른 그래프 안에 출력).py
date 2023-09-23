import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import random
import pandas as pd
import copy

plt.rc('font', family='Malgun Gothic')

bn = 10 # 버튼개수
pslst = [0]*100 # 어느 퍼센트변수가 가장 많이 수익을 실현하는 저장하기위한 배열
plst2 = [0.0]*100 # 1부터 100퍼센트 변수들 반복 값들 모두 저장하는 배열
blst  = [0]*bn # 버튼의 펴센트를 저장하기위한 배열
rept = 100000 # 반복횟수
mnlst = [[0] * 100 for _ in range(rept)] # 1부터 100퍼센트 변수들이 모든 버튼을 누르고 난 후의 값들을 모두 저장하는 배열(반복해서 나온 결과들도 모두)([[1부터 100퍼센트 값들 저장]*반복 횟수])
delnum = 10 # mnlst의 최댓값과 최솟값들의 개수를 제거하는 변수
minlst = [0]*100
maxlst = [0]*100
rlst = [0]*100

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
        # plst2[i] += plst[i]/rept
        mnlst[x][i] = plst[i]
        
    idx = plst.index(max(plst)) # pslt(퍼센트변수의 값을 저장한 배열)배열에 가장 큰 값의 인덱스를 저장하는 변수
    # pslst배열의 인덱스가 idx인 요소에 1을 더하는 코드
    pslst[idx] += 1 
    # print(max(plst))
    # print(plst)
# pslst배열의 가장 큰 값에 1을 더한 값 출력(인덱스는 0부터 시작하기 떄문에 1을 더함)
# print(pslst.index(max(pslst))+1)
# print(pslst)
# plst2배열의 가장 큰 값에 1을 더한 값 출력
# print(plst2.index(max(plst2))+1)
# print(plst2)


mnlst = np.array(mnlst).T # 행열 변환([[1퍼센트 값들]*100])
mnlst1 = copy.deepcopy(mnlst) # mnlst 깊은 복사복사
# # 각 요소들 정렬
for row in mnlst:
    row.sort()

mnlst = mnlst.tolist() # 리스트로 형변환
for x in range(100):
    for y in range(delnum):
        del mnlst[x][0]
        del mnlst[x][-1]

for x in range(100):
    plst2[x] = sum(mnlst[x])/(rept-delnum*2)

mnlst1 = mnlst1.tolist() # 리스트로 형변환
for x in range(100):
    try:
        mnlst1[x].remove(0)
    except:
        pass

for x in range(100):
    # for y in range(delnum):
    #     del mnlst[x][0]
    #     del mnlst[x][-1]
    minlst[x] = min(mnlst[x])
    maxlst[x] = max(mnlst[x])
    rlst[x] = maxlst[x] - minlst[x]
    print(minlst[x], maxlst[x], rlst[x])

# ################그래프 그리기################


# x축의 값을 저장
x1 = [i+1 for i in range(100)]
x1 = np.array(x1)
# y축의 값을 저장


# 데이터 생성
# x = [i+1 for i in range(100)]
y1 = [x for x in minlst]
y1 = np.array(y1)
y2 = [x for x in pslst]
y2 = np.array(y2)
y3 = [x for x in maxlst]
y3 = np.array(y3)
y4 = [x for x in rlst]
# y4 = np.log10(y4)
y4 = np.array(y4)

# 데이터 정렬 및 상위 10% 추출
y1_sorted = np.sort(y1)
y2_sorted = np.sort(y2)
y3_sorted = np.sort(y3)
y4_sorted = np.sort(y4)
top_10_percent = int(0.03 * len(x1)) # 몇 개의 y값 레이블을 보여주는 변수

# 첫 번째 그래프 생성
fig, ax1 = plt.subplots(figsize=(8, 4))

# for i in range(len(x1)):
#     height = y1[i]
#     ax1.text(x1[i], height + 0.01, '%.1f' %height, ha='center', va='bottom', size = 12, color = "blue")

ax1.plot(x1, y2, label='가장 큰 수익을 가진 퍼센트 개수', color='blue', linestyle='--')
ax1.set_xlabel('x')
ax1.set_ylabel('가장 큰 수익을 가진 퍼센트 개수', color='black')
ax1.tick_params(axis='y', labelcolor='black')
# x 축 범위를 설정합니다.
ax1.set_xlim(1, 100)

# x 축에 주 눈금을 설정합니다. (2 간격)
ax1.set_xticks(range(1, 101, 2))


# 두 번째 그래프 및 보조 축 생성
ax2 = ax1.twinx()

# for i in range(len(x1)):
#     height = y2[i]
#     ax2.text(x1[i], height + 0.01, '%.1f' %height, ha='center', va='bottom', size = 12, color = "red")

ax2.plot(x1, y1, label='최소 수익', color='red', linestyle='-')
ax2.set_ylabel('최소 수익', color='black')
ax2.tick_params(axis='y', labelcolor='black')              

ax2.plot(x1, y3, label='최대 수익', color='black', linestyle='-')
ax2.set_ylabel('최대/최소 수익', color='black')
ax2.tick_params(axis='y', labelcolor='black')

y2_ticks = np.linspace(minlst[0],maxlst[0], 1000)

# 상위 10% 값 레이블 추가
for i in range(top_10_percent):
    ax1.annotate(f'{y1_sorted[-(i+1)]:.2f}', xy=(x1[np.where(y1 == y1_sorted[-(i+1)])][0], y1_sorted[-(i+1)]),
                 xytext=(x1[np.where(y1 == y1_sorted[-(i+1)])][0] + 0.2, y1_sorted[-(i+1)]),
                 arrowprops=dict(arrowstyle='->', color='blue'),
                 fontsize=10, color='blue')

    ax2.annotate(f'{y2_sorted[-(i+1)]:.2f}', xy=(x1[np.where(y2 == y2_sorted[-(i+1)])][0], y2_sorted[-(i+1)]),
                 xytext=(x1[np.where(y2 == y2_sorted[-(i+1)])][0] + 0.2, y2_sorted[-(i+1)]),
                 arrowprops=dict(arrowstyle='->', color='red'),
                 fontsize=10, color='red')

    ax2.annotate(f'{y3_sorted[-(i+1)]:.2f}', xy=(x1[np.where(y3 == y3_sorted[-(i+1)])][0], y3_sorted[-(i+1)]),
                 xytext=(x1[np.where(y3 == y3_sorted[-(i+1)])][0] + 0.2, y3_sorted[-(i+1)]),
                 arrowprops=dict(arrowstyle='->', color='black'),
                 fontsize=10, color='black')
    

# 그래프 제목과 범례 설정
fig.suptitle('최소선택확률의 결과')
fig.legend(loc='upper right')

plt.figure(figsize=(8, 4))
plt.plot(x1, y4, label='최댓값-최솟값의 로그값', color='black', linestyle='-')

for i in range(top_10_percent):
    plt.annotate(f'{y4_sorted[-(i+1)]:.2f}', xy=(x1[np.where(y4 == y4_sorted[-(i+1)])][0], y4_sorted[-(i+1)]),
                 xytext=(x1[np.where(y4 == y4_sorted[-(i+1)])][0] + 0.2, y4_sorted[-(i+1)]),
                 arrowprops=dict(arrowstyle='->', color='black'),
                 fontsize=10, color='black')
plt.xlabel('확률')
plt.ylabel('최댓값-최솟값의 로그값', color='black')
plt.tick_params(axis='y', labelcolor='black')
plt.title('최댓값-최솟값의 로그값')
plt.legend(loc='upper left')


# 그래프 표시
plt.show()

