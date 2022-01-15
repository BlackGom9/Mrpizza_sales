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

s_B_p = [sum(mrpi_d1['B_p']), sum(mrpi_d2['B_p']), sum(mrpi_d3['B_p']), sum(mrpi_d4['B_p']), sum(mrpi_d5['B_p']), sum(mrpi_d6['B_p']), sum(mrpi_d7['B_p']), sum(mrpi_d8['B_p']), sum(mrpi_d9['B_p']), sum(mrpi_d10['B_p']), sum(mrpi_d11['B_p']), sum(mrpi_d12['B_p'])] # 월별 총 매출 합

s_B_p

plt.rc('font', family='Malgun Gothic')
plt.figure(figsize = (10, 3))
plt.plot(m_k, s_B_p) # 월별 총 뷔페 인원

mrpi_dp = mrpi_d[mrpi_d['B_p'] != 0] # 뷔페인원 0인 행 제거

plt.rc('font', family='Malgun Gothic')
plt.figure(figsize = (25, 10))
sns.lineplot(data = mrpi_dp, x = 'day', y = 'B_p', ci = None) # 일별 뷔페인원 

plt.figure(figsize = (10, 5))
sns.boxplot(data = mrpi_dp, x = 'dayw', y = 'B_p', order = day_o) 
