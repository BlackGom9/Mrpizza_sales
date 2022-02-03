import pandas as pd

mrpi_d = pd.read_excel("C:/Users/Kimkangmin/Desktop/mrpi/상계20년 1월 영업일보.xlsx", sheet_name = '영업일보 일일매출') 
# 데이터를 변수에 저장

mrpi_d 
# 데이터 확인 

mrpi_d = mrpi_d.T 
# 행열 전환

mrpi_d = mrpi_d.reset_index() 
# 열 인덱스에 있는 데이터 데이터프레임에 포함 

mrpi_d = mrpi_d.rename(columns = {'index' : 'day', 0 : 'dayw', 1 : 'T_s', 2 : 'd_s', 3 : 'v_s', 4 : 'wea', 5 : 'T_l', 6 : 'T_r', 7 : 'B_p', 8 : 'B_l', 9 : 'B_r'})
# 날짜 = day, 요일 = dayw(day of week), 총 매출 = T_s(total sales), 배달총매출 = d_s(delivery sales), 내점 = v_s(visit sales), 날씨 = weather(wea), 총 사용한 라지 = T_l(total large), 총 사용한 레귤러 = T_r(total regular), 총 뷔페인원 = B_p(buffet people), 뷔페L = B_l(buffet large), 뷔페R = B_r(buffet regualr) 

mrpi_d = mrpi_d.drop(0, axis = 0) 
# 첫 행 제거

mrpi_d 
# 변환 되었는지 확인

def change_df(x):
    x = x.transpose()
    x = x.reset_index()
    x = x.rename(columns = {'index' : 'day', 0 : 'dayw', 1 : 'T_s', 2 : 'd_s', 3 : 'v_s', 4 : 'wea', 5 : 'T_l', 6 : 'T_r', 7 : 'B_p', 8 : 'B_l', 9 : 'B_r'})
    x = x.drop(0, axis = 0)
    return x
# 데이터프레임 변환 함수

mrpi_d = pd.read_excel("C:/Users/Kimkangmin/Desktop/mrpi/상계20년 1월 영업일보.xlsx", sheet_name = '영업일보 일일매출') 
mrpi_d = change_df(mrpi_d) 
mrpi_d 
# 테스트

mrpi_d1 = pd.read_excel("C:/Users/Kimkangmin/Desktop/mrpi/상계20년 1월 영업일보.xlsx", sheet_name = '영업일보 일일매출')  
mrpi_d2 = pd.read_excel("C:/Users/Kimkangmin/Desktop/mrpi/상계20년 2월 영업일보.xlsx", sheet_name = '영업일보 일일매출')
mrpi_d3 = pd.read_excel("C:/Users/Kimkangmin/Desktop/mrpi/상계20년 3월 영업일보.xlsx", sheet_name = '영업일보 일일매출')
mrpi_d4 = pd.read_excel("C:/Users/Kimkangmin/Desktop/mrpi/상계20년 4월 영업일보.xlsx", sheet_name = '영업일보 일일매출')
mrpi_d5 = pd.read_excel("C:/Users/Kimkangmin/Desktop/mrpi/상계20년 5월 영업일보.xlsx", sheet_name = '영업일보 일일매출')
mrpi_d6 = pd.read_excel("C:/Users/Kimkangmin/Desktop/mrpi/상계20년 6월 영업일보.xlsx", sheet_name = '영업일보 일일매출')
mrpi_d7 = pd.read_excel("C:/Users/Kimkangmin/Desktop/mrpi/상계20년 7월 영업일보.xlsx", sheet_name = '영업일보 일일매출')
mrpi_d8 = pd.read_excel("C:/Users/Kimkangmin/Desktop/mrpi/상계20년 8월 영업일보.xlsx", sheet_name = '영업일보 일일매출')
mrpi_d9 = pd.read_excel("C:/Users/Kimkangmin/Desktop/mrpi/상계20년 9월 영업일보.xlsx", sheet_name = '영업일보 일일매출')
mrpi_d10 = pd.read_excel("C:/Users/Kimkangmin/Desktop/mrpi/상계20년 10월 영업일보.xlsx", sheet_name = '영업일보 일일매출')
mrpi_d11 = pd.read_excel("C:/Users/Kimkangmin/Desktop/mrpi/상계20년 11월 영업일보.xlsx", sheet_name = '영업일보 일일매출')
mrpi_d12 = pd.read_excel("C:/Users/Kimkangmin/Desktop/mrpi/상계20년 12월 영업일보.xlsx", sheet_name = '영업일보 일일매출')

mrpi_d1 = change_df(mrpi_d1)
mrpi_d2 = change_df(mrpi_d2)
mrpi_d3 = change_df(mrpi_d3)
mrpi_d4 = change_df(mrpi_d4)
mrpi_d5 = change_df(mrpi_d5)
mrpi_d6 = change_df(mrpi_d6)
mrpi_d7 = change_df(mrpi_d7)
mrpi_d8 = change_df(mrpi_d8)
mrpi_d9 = change_df(mrpi_d9)
mrpi_d10 = change_df(mrpi_d10)
mrpi_d11 = change_df(mrpi_d11)
mrpi_d12 = change_df(mrpi_d12)

mrpi_d = pd.concat([mrpi_d1, mrpi_d2, mrpi_d3, mrpi_d4, mrpi_d5, mrpi_d6, mrpi_d7, mrpi_d8, mrpi_d9, mrpi_d10, mrpi_d11, mrpi_d12]) # 2020년 총 매출정보

mrpi_d

mrpi_d.dtypes # 데이터 타입 확인

mrpi_d['day'] = pd.to_datetime(mrpi_d['day']) # day의 데이터 타입 변경

mrpi_d = mrpi_d.astype({'T_s' : 'int'}) 
mrpi_d = mrpi_d.astype({'d_s' : 'int'}) 
mrpi_d = mrpi_d.astype({'v_s' : 'int'}) 
mrpi_d = mrpi_d.astype({'T_l' : 'int'}) 
mrpi_d = mrpi_d.astype({'T_r' : 'int'}) 
mrpi_d = mrpi_d.astype({'B_p' : 'int'}) 
mrpi_d = mrpi_d.astype({'B_l' : 'int'}) 
mrpi_d = mrpi_d.astype({'B_r' : 'int'}) 

mT_s = [sum(mrpi_d1['T_s']), sum(mrpi_d2['T_s']), sum(mrpi_d3['T_s']), sum(mrpi_d4['T_s']), sum(mrpi_d5['T_s']), sum(mrpi_d6['T_s']), sum(mrpi_d7['T_s']), sum(mrpi_d8['T_s']), sum(mrpi_d9['T_s']), sum(mrpi_d10['T_s']), sum(mrpi_d11['T_s']), sum(mrpi_d12['T_s'])] # 월별 총 매출 합
m_k = ['1월', '2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']

plt.rc('font', family='Malgun Gothic')
plt.figure(figsize = (10, 3))
plt.plot(m_k, mT_s) # 월별 총 매출 그래프

plt.rc('font', family='Malgun Gothic')
plt.figure(figsize = (25, 10))
sns.lineplot(data = mrpi_d, x = 'day', y = 'T_s', ci = None)

day_o = ["월", "화", "수", "목", "금", "토", "일"]
plt.figure(figsize = (15, 10))
sns.boxplot(data = mrpi_d, x = 'dayw', y = 'T_s', order = day_o)

def monthl_T_s(sd, ed):
    sd = datetime.strptime(sd, "%Y/%m/%d")
    ed = datetime.strptime(ed, "%Y/%m/%d")
    e = mrpi_d[(mrpi_d['day'] >= sd) & (mrpi_d['day'] <= ed)]
    plt.figure(figsize = (10, 3))
    f = sns.lineplot(data = e, x = 'day', y = 'T_s',ci = None)
    return f

def monthb_T_s(sd, ed):
    sd = datetime.strptime(sd, "%Y/%m/%d")
    ed = datetime.strptime(ed, "%Y/%m/%d")
    e = mrpi_d[(mrpi_d['day'] >= sd) & (mrpi_d['day'] <= ed)]
    plt.figure(figsize = (10, 3))
    f = sns.boxplot(data = e, x = 'dayw', y = 'T_s', order = day_o)
    return f

monthl_T_s('2020/1/1', '2020/2/1')
monthb_T_s('2020/1/1', '2020/2/1') # 1월 총매출 변화량

monthl_T_s('2020/2/1', '2020/3/1')
monthb_T_s('2020/2/1', '2020/3/1') # 2월 총매출 변화량

monthl_T_s('2020/3/1', '2020/4/1')
monthb_T_s('2020/3/1', '2020/4/1') # 3월 총매출 변화량

monthl_T_s('2020/4/1', '2020/5/1')
monthb_T_s('2020/4/1', '2020/5/1') # 4월 총매출 변화량

monthl_T_s('2020/5/1', '2020/6/1')
monthb_T_s('2020/5/1', '2020/6/1') # 5월 총매출 변화량

monthl_T_s('2020/6/1', '2020/7/1')
monthb_T_s('2020/6/1', '2020/7/1') # 6월 총매출 변화량

monthl_T_s('2020/7/1', '2020/8/1')
monthb_T_s('2020/7/1', '2020/8/1') # 7월 총매출 변화량

monthl_T_s('2020/8/1', '2020/9/1')
monthb_T_s('2020/8/1', '2020/9/1') # 8월 총매출 변화량

monthl_T_s('2020/9/1', '2020/10/1')
monthb_T_s('2020/9/1', '2020/10/1') # 9월 총매출 변화량

monthl_T_s('2020/10/1', '2020/11/1')
monthb_T_s('2020/10/1', '2020/11/1') # 10월 총매출 변화량

monthl_T_s('2020/11/1', '2020/12/1')
monthb_T_s('2020/11/1', '2020/12/1') # 11월 총매출 변화량

monthl_T_s('2020/12/1', '2021/12/31')
monthb_T_s('2020/12/1', '2021/12/31') # 12월 총매출 변화량

mrpi_d['p_Tv'] = mrpi_d['v_s'] / mrpi_d['T_s'] # 총 매출에서 내점 매출의 비율

mv_s = [sum(mrpi_d1['v_s']), sum(mrpi_d2['v_s']), sum(mrpi_d3['v_s']), sum(mrpi_d4['v_s']), sum(mrpi_d5['v_s']), sum(mrpi_d6['v_s']), sum(mrpi_d7['v_s']), sum(mrpi_d8['v_s']), sum(mrpi_d9['v_s']), sum(mrpi_d10['v_s']), sum(mrpi_d11['v_s']), sum(mrpi_d12['v_s'])] 

for i in range(0,12):
    global m_p_Tv
    m_p_Tv[i] = mv_s[i] / mT_s[i]
    
plt.rc('font', family='Malgun Gothic')
plt.figure(figsize = (10, 3))
plt.plot(m_k, m_p_Tv) # 월별 총 매출에서 내점 매출의 비율

plt.rc('font', family='Malgun Gothic')
plt.figure(figsize = (25, 10))
sns.lineplot(data = mrpi_d, x = 'day', y = 'p_Tv', ci = None) # 일별 총 매출에서 내점 매출의 비율

day_o = ["월", "화", "수", "목", "금", "토", "일"]
plt.figure(figsize = (10, 5))
sns.boxplot(data = mrpi_d, x = 'dayw', y = 'p_Tv', order = day_o)

ms_d = mrpi_d.sort_values(by = 'd_s', ascending = False)
ms_d.head(15) 
# 4/29 ~ 4/30 T데이 할인
# 7/22 ~ 7/23 T데이 할인

ms_v = mrpi_d.sort_values(by = 'v_s', ascending = False)
ms_v.head(15)
# 1/24 ~ 1/27 설날

s_B_p = [sum(mrpi_d1['B_p']), sum(mrpi_d2['B_p']), sum(mrpi_d3['B_p']), sum(mrpi_d4['B_p']), sum(mrpi_d5['B_p']), sum(mrpi_d6['B_p']), sum(mrpi_d7['B_p']), sum(mrpi_d8['B_p']), sum(mrpi_d9['B_p']), sum(mrpi_d10['B_p']), sum(mrpi_d11['B_p']), sum(mrpi_d12['B_p'])] # 월별 총 매출 합

s_B_p

s_B_p[8] = (s_B_p[7] + s_B_p[9])/2 # 9월의 값이 누락 되었으므로 전월과 그 다음월의 평균값으로 대체

plt.rc('font', family='Malgun Gothic')
plt.figure(figsize = (10, 3))
plt.plot(m_k, s_B_p) # 월별 총 뷔페 인원

mrpi_dp = mrpi_d[mrpi_d['B_p'] != 0] # 뷔페인원 0인 행 제거

plt.rc('font', family='Malgun Gothic')
plt.figure(figsize = (25, 10))
sns.lineplot(data = mrpi_dp, x = 'day', y = 'B_p', ci = None) # 일별 뷔페인원 

plt.figure(figsize = (10, 5))
sns.boxplot(data = mrpi_dp, x = 'dayw', y = 'B_p', order = day_o) 

mrpi_dp = mrpi_dp[(mrpi_dp['B_l'] != 0)] # 뷔페에 사용한 라지가 0인 경우 제거

mrpi_dp['B_e1'] = mrpi_dp['B_l']*2 + mrpi_dp['B_r'] # 라지 1판이 레귤러 2판이라고 가정

mrpi_dp['B_e2'] = mrpi_dp['B_l']*((35**2) / (28**2)) + mrpi_dp['B_r'] # 실제 크기로 차이 비교

mrpi_dp['B_e3'] = mrpi_dp['B_l']*(1.5) + mrpi_dp['B_r'] # 조각 수 차이로 비교

mrpi_dp['d_p1'] = abs(mrpi_dp['B_p'] - mrpi_dp['B_e1'])
mrpi_dp['d_p2'] = abs(mrpi_dp['B_p'] - mrpi_dp['B_e2'])
mrpi_dp['d_p3'] = abs(mrpi_dp['B_p'] - mrpi_dp['B_e3'])

plt.rc('font', family='Malgun Gothic')
plt.figure(figsize = (25, 10))
sns.lineplot(data = mrpi_dp, x = 'day', y = mrpi_dp['d_p2'], ci = None)

plt.figure(figsize = (25, 10))
sns.lineplot(data = mrpi_dp, x = 'day', y = mrpi_dp['d_p3'], ci = None)

plt.figure(figsize = (25, 10))
sns.lineplot(data = mrpi_dp, x = 'day', y = mrpi_dp['d_p4'], ci = None)

from statsmodels.formula.api import ols

d_p1r = ols(formula = 'B_p ~ B_e1', data = mrpi_dp).fit()
d_p1r.summary()

fig = plt.figure(figsize=(8,8))
font_size = 15
plt.scatter(mrpi_dp['B_p'],mrpi_dp['B_e1']) # 원 데이터 분포도
plt.plot(mrpi_dp['B_e1'], d_p1r.fittedvalues,color='red') # 회귀직선 추가
plt.show()

d_p2r = ols(formula = 'B_p ~ B_e2', data = mrpi_dp).fit()
d_p2r.summary()

fig = plt.figure(figsize=(8,8))
font_size = 15
plt.scatter(mrpi_dp['B_p'],mrpi_dp['B_e2']) # 원 데이터 분포도
plt.plot(mrpi_dp['B_e2'], d_p2r.fittedvalues,color='red') # 회귀직선 추가
plt.show()

d_p3r = ols(formula = 'B_p ~ B_e3', data = mrpi_dp).fit()
d_p3r.summary()

fig = plt.figure(figsize=(8,8))
font_size = 15
plt.scatter(mrpi_dp['B_p'],mrpi_dp['B_e3']) # 원 데이터 분포도
plt.plot(mrpi_dp['B_e3'], d_p3r.fittedvalues,color='red') # 회귀직선 추가
plt.show()


# #### sklearn linearregression 방법

from sklearn.linear_model import LinearRegression

a = np.arange(0, 200, 0.1)

def B_ep(x, y):
    B_e = LinearRegression()
    B_e.fit(mrpi_dp['B_p'].values.reshape(-1,1), mrpi_dp[x])
    z = B_e.predict([[y]])
    print('인원이' , y, '명일 경우 레귤러 사이즈 피자가', z ,'판 필요합니다.')
 
    global xx
    
    if x == 'B_e1':
        xx = 2
    elif x == 'B_e2':
        xx = (35**2) / (28**2)
    elif x == 'B_e3':
        xx = 1.5
    
    print('라지 사이즈 피자만 사용한다고 가정한다면 ', z/xx, '판 필요합니다.')
# 뷔페 비율별 인원당 필요한 레귤러 예측량과 단순선형회귀직선

def B_ef(x):   
    B_e = LinearRegression()
    B_e.fit(mrpi_dp['B_p'].values.reshape(-1,1), mrpi_dp[x])   
    fig = plt.figure(figsize=(8,8))
    font_size = 15
    plt.scatter(mrpi_dp['B_p'],mrpi_dp[x]) # 원 데이터 분포도
    plt.plot(a, B_e.coef_*a + B_e.intercept_, color = 'red') # 회귀직선

def B_erf(x):
    y = mrpi_dp['B_p'].values.reshape(-1,1)
    z = mrpi_dp[x]
    B_e = LinearRegression()
    B_e.fit(mrpi_dp['B_p'].values.reshape(-1,1), mrpi_dp[x])
    resid = z - B_e.predict(y)
    
    fig = plt.figure(figsize=(8,8))
    plt.title(x)
    plt.scatter(y,resid) ## 잔차도 출력
    plt.show()

def B_er(x):
    y = mrpi_dp['B_p'].values.reshape(-1,1)
    z = mrpi_dp[x]
    B_e = LinearRegression()
    B_e.fit(mrpi_dp['B_p'].values.reshape(-1,1), mrpi_dp[x])
    resid = z - B_e.predict(y)
    return resid

plt.rcParams['axes.unicode_minus'] = False

B_ep('B_e1', 50)
B_ef('B_e1')
B_erf('B_e1')

B_ep('B_e2', 50)
B_ef('B_e2')
B_erf('B_e2')

B_ep('B_e3', 50)
B_ef('B_e3')
B_erf('B_e3')

B_erf('B_e1')

B_erf('B_e2')

B_erf('B_e3')

fig = plt.figure(figsize=(8,8))
plt.boxplot([B_er('B_e1'), B_er('B_e2'), B_er('B_e3')])
plt.show()

mrpi_d1['d_l'] = mrpi_d1['T_l'] - mrpi_d1['B_l'] 
mrpi_d2['d_l'] = mrpi_d2['T_l'] - mrpi_d2['B_l'] 
mrpi_d3['d_l'] = mrpi_d3['T_l'] - mrpi_d3['B_l'] 
mrpi_d4['d_l'] = mrpi_d4['T_l'] - mrpi_d4['B_l'] 
mrpi_d5['d_l'] = mrpi_d5['T_l'] - mrpi_d5['B_l'] 
mrpi_d6['d_l'] = mrpi_d6['T_l'] - mrpi_d6['B_l'] 
mrpi_d7['d_l'] = mrpi_d7['T_l'] - mrpi_d7['B_l'] 
mrpi_d8['d_l'] = mrpi_d8['T_l'] - mrpi_d8['B_l'] 
mrpi_d9['d_l'] = mrpi_d9['T_l'] - mrpi_d9['B_l'] 
mrpi_d10['d_l'] = mrpi_d10['T_l'] - mrpi_d10['B_l'] 
mrpi_d11['d_l'] = mrpi_d11['T_l'] - mrpi_d11['B_l'] 
mrpi_d12['d_l'] = mrpi_d12['T_l'] - mrpi_d12['B_l'] 
# 월별 배달로 나간 라지 사이즈 개수

mrpi_d1['d_r'] = mrpi_d1['T_r'] - mrpi_d1['B_r'] 
mrpi_d2['d_r'] = mrpi_d2['T_r'] - mrpi_d2['B_r'] 
mrpi_d3['d_r'] = mrpi_d3['T_r'] - mrpi_d3['B_r'] 
mrpi_d4['d_r'] = mrpi_d4['T_r'] - mrpi_d4['B_r'] 
mrpi_d5['d_r'] = mrpi_d5['T_r'] - mrpi_d5['B_r'] 
mrpi_d6['d_r'] = mrpi_d6['T_r'] - mrpi_d6['B_r'] 
mrpi_d7['d_r'] = mrpi_d7['T_r'] - mrpi_d7['B_r'] 
mrpi_d8['d_r'] = mrpi_d8['T_r'] - mrpi_d8['B_r'] 
mrpi_d9['d_r'] = mrpi_d9['T_r'] - mrpi_d9['B_r'] 
mrpi_d10['d_r'] = mrpi_d10['T_r'] - mrpi_d10['B_r'] 
mrpi_d11['d_r'] = mrpi_d11['T_r'] - mrpi_d11['B_r'] 
mrpi_d12['d_r'] = mrpi_d12['T_r'] - mrpi_d12['B_r'] 
# 월별 배달로 나간 레귤러 사이즈 개수

mrpi_d1

mrpi_d1 = mrpi_d1[(mrpi_d1['d_l'] > 0) & (mrpi_d1['d_r'] >= 0)] 
mrpi_d2 = mrpi_d2[(mrpi_d2['d_l'] > 0) & (mrpi_d2['d_r'] >= 0)] 
mrpi_d3 = mrpi_d3[(mrpi_d3['d_l'] > 0) & (mrpi_d3['d_r'] >= 0)] 
mrpi_d4 = mrpi_d4[(mrpi_d4['d_l'] > 0) & (mrpi_d4['d_r'] >= 0)] 
mrpi_d5 = mrpi_d5[(mrpi_d5['d_l'] > 0) & (mrpi_d5['d_r'] >= 0)] 
mrpi_d6 = mrpi_d6[(mrpi_d6['d_l'] > 0) & (mrpi_d6['d_r'] >= 0)] 
mrpi_d7 = mrpi_d7[(mrpi_d7['d_l'] > 0) & (mrpi_d7['d_r'] >= 0)] 
mrpi_d8 = mrpi_d8[(mrpi_d8['d_l'] > 0) & (mrpi_d8['d_r'] >= 0)] 
mrpi_d9 = mrpi_d9[(mrpi_d9['d_l'] > 0) & (mrpi_d9['d_r'] >= 0)] 
mrpi_d10 = mrpi_d10[(mrpi_d10['d_l'] > 0) & (mrpi_d10['d_r'] >= 0)] 
mrpi_d11 = mrpi_d11[(mrpi_d11['d_l'] > 0) & (mrpi_d11['d_r'] >= 0)] 
mrpi_d12 = mrpi_d12[(mrpi_d12['d_l'] > 0) & (mrpi_d12['d_r'] >= 0)] 
# 배달로 나간 라지 사이즈 개수 중 0 이하 제거 및 배달로 나간 레귤러 사이즈 개수 중 음수 제거
# 뷔페로 나간 레귤러 사이즈가 없을 수도 있으므로 음수만 제거

mrpi_d1['d_t'] = mrpi_d1['d_l']*(1.5) + mrpi_d1['d_r'] 
mrpi_d2['d_t'] = mrpi_d2['d_l']*(1.5) + mrpi_d2['d_r'] 
mrpi_d3['d_t'] = mrpi_d3['d_l']*(1.5) + mrpi_d3['d_r'] 
mrpi_d4['d_t'] = mrpi_d4['d_l']*(1.5) + mrpi_d4['d_r'] 
mrpi_d5['d_t'] = mrpi_d5['d_l']*(1.5) + mrpi_d5['d_r'] 
mrpi_d6['d_t'] = mrpi_d6['d_l']*(1.5) + mrpi_d6['d_r'] 
mrpi_d7['d_t'] = mrpi_d7['d_l']*(1.5) + mrpi_d7['d_r'] 
mrpi_d8['d_t'] = mrpi_d8['d_l']*(1.5) + mrpi_d8['d_r'] 
mrpi_d9['d_t'] = mrpi_d9['d_l']*(1.5) + mrpi_d9['d_r'] 
mrpi_d10['d_t'] = mrpi_d10['d_l']*(1.5) + mrpi_d10['d_r'] 
mrpi_d11['d_t'] = mrpi_d11['d_l']*(1.5) + mrpi_d11['d_r'] 
mrpi_d12['d_t'] = mrpi_d12['d_l']*(1.5) + mrpi_d12['d_r'] 
# 레귤러 사이즈 기준으로 배달 판매량
# 뷔페 데이터를 통해서 얻은 '라지 사이즈는 레귤러 사이즈의 약 1.5배이다.'를 적용

d_t = [sum(mrpi_d1['d_t']) / len(mrpi_d1), sum(mrpi_d2['d_t']) / len(mrpi_d1), sum(mrpi_d3['d_t']) / len(mrpi_d1), sum(mrpi_d4['d_t']) / len(mrpi_d1), sum(mrpi_d5['d_t']) / len(mrpi_d1), sum(mrpi_d6['d_t']) / len(mrpi_d1), sum(mrpi_d7['d_t']) / len(mrpi_d1), sum(mrpi_d8['d_t']) / len(mrpi_d1), sum(mrpi_d9['d_t']) / len(mrpi_d1), sum(mrpi_d10['d_t']) / len(mrpi_d1), sum(mrpi_d11['d_t']) / len(mrpi_d1), sum(mrpi_d12['d_t']) / len(mrpi_d1)] 
# 월별 일 평균 피자 레귤러 사이즈 판매량

d_t

plt.figure(figsize = (10, 3))
plt.plot(m_k, d_t)
# 월별 일 평균 피자 레귤러 사이즈 판매량 그래프

mrpi_d1['d_l'] = mrpi_d1['T_l'] - mrpi_d1['B_l'] 


mrpi_d['d_l'] = mrpi_d['T_l'] - mrpi_d['B_l'] # 배달로 나간 라지 사이즈 개수 

mrpi_d['d_r'] = mrpi_d['T_r'] - mrpi_d['B_r'] # 배달로 나간 레귤지 사이즈 개수 

mrpi_d[mrpi_d['d_l'] <= 0]

mrpi_d[mrpi_d['d_r'] < 0]

mrpi_d = mrpi_d[(mrpi_d['d_l'] > 0) & (mrpi_d['d_r'] >= 0)] 
# 배달로 나간 라지 사이즈 개수 중 0 이하 제거 및 배달로 나간 레귤러 사이즈 개수 중 음수 제거
# 뷔페로 나간 레귤러 사이즈가 없을 수도 있으므로 음수만 제거

mrpi_d

mrpi_d['d_t'] = mrpi_d['d_l']*(1.5) + mrpi_d['d_r'] 
# 레귤러 사이즈 기준으로 배달로 판매량
# 뷔페 데이터를 통해서 얻은 '라지 사이즈는 레귤러 사이즈의 약 1.5배이다.'를 적용

mrpi_d

plt.figure(figsize = (25, 10))
sns.lineplot(data = mrpi_d, x = 'day', y = 'd_t', ci = None)
