# from pyscript import display, document
import pandas as pd
import subprocess
import os
import time

def file_exists(filename):
    return os.path.exists(os.path.join('data', filename)) # 존재하면 True

if __name__ =="__main__":

    # def function(evt):  
    #     lat_value = document.querySelector("#latValue")
    #     lng_value = document.querySelector("#lngValue")
    #     radius_value = document.querySelector("#radiusValue")
    #     date_value = document.querySelector("#dateValue")
    #     time_value = document.querySelector("#timeValue")
    #     result= document.querySelector("#result")
    #     # 입력값 확인
    #     # result.innerText = f'{lat_value.value, lng_value.value, radius_value.value, date_value.value.split('-'), time_value.value}'
        
    #     ## 입력값
    #     search_lat = lat_value.value    # 위도
    #     search_lng = lng_value.value    # 경도
    #     search_radius = radius_value.value  # 반경
    #     search_date = date_value.value.split('-')
    #     search_time = time_value.value
    #     '''
    #     '37.57035764261156', <class 'str'>
    #     '126.99036702755654', <class 'str'> 
    #     '0.3', <class 'str'>
    #     ['2024', '07', '31'], <class 'list'>
    #     '00:45', <class 'str'>
    #     '''

    #     ## 필터링 진행 함수 
    #     if float(search_radius) > 10:
    #         result.innerText = "반경을 10 이하로 입력해주세요."
    #     else:
    #         # 필터링
    #         result.innerText = "=========검색결과==========="
    #         pass

    # INPUTS: 들어올것으로 예상
    filename = 'test'
    search_lat = '37.571006515132865' 
    search_lng = '126.99251768504305' 
    search_radius = '0.5' # km
    search_date = ['2024','07','06'] 
    search_time = '01:00' # 궁금한 시간

    # Define file paths
    csv_file = f'{filename}.csv'
    crawled_file = f'{filename}_crawled.csv'
    sorted_file = f'{filename}_sorted.csv'

    if not os.path.exists('data'):
        os.makedirs('data')

    # 1) f'{filename}.csv'가 없으면 만들어
    if not file_exists(csv_file):
        if file_exists('original_data.csv'):
            print('1) data_load.py 실행')
            print('original_data.csv을 불러옵니다..')
            starttime = time.time()
            subprocess.run(['python', 'data_load.py', filename])
            endtime = time.time()
            print(f'1) data_load.py 완료!, {endtime - starttime} seconds {"="*20}\n')
        else:
            print("데이터를 로드할 수 없습니다 ㅠ ...(1)")

    # 2) f'{filename}_crawled.csv'가 없으면 만들어
    if file_exists(csv_file) and not file_exists(crawled_file):
        print('2) crawl.py 실행')
        print(f'{csv_file}.csv을 불러옵니다..')
        starttime = time.time()
        subprocess.run(['python', 'crawl.py', filename])
        endtime = time.time()
        print(f'2) crawl.py 완료!, {endtime - starttime} seconds {"="*20}\n')
    else:
        print("데이터를 로드할 수 없습니다 ㅠ ...(2)")

    # 3) f'{filename}_sorted.csv'가 없으면 만들어
    if file_exists(crawled_file) and not file_exists(sorted_file):
        print('3) sort_distance.py 실행')
        print(f'{crawled_file}을 불러옵니다..')
        starttime = time.time()
        subprocess.run(['python', 'sort_distance.py', filename, search_lat, search_lng, search_radius])
        endtime = time.time()
        print(f'3) sort_distance.py 완료, {endtime - starttime} seconds {"="*20}\n')
        print(f'total: {endtime - starttime} seconds')
    else:
        print("데이터를 로드할 수 없습니다 ㅠ ...(3)")
    
    # 4) f'{filename}_sorted.csv'가 있으면 실행
    if file_exists(sorted_file):
        print('4) get_time.py 실행')
        print(f'{sorted_file}을 불러옵니다..')

        year, mon, day = search_date
        time_ = ''.join(search_time.split(':'))
        result_filename = f'result_{year + mon + day}_{time_}.csv'

        starttime = time.time()
        subprocess.run(['python', 'get_time.py', filename, year, mon, day, search_time, result_filename])
        endtime = time.time()
        print(f'4) get_time.py 완료!, {endtime - starttime} seconds {"="*20}\n')

        result_path = os.path.join('result/', result_filename)
        df = pd.read_csv(result_path)
        print(df)

    else:
        print("4) 데이터를 로드할 수 없습니다 ㅠ ...(4)")
        # result.innerText = "데이터를 로드할 수 없습니다."
    # 오래걸리는 이유: "get_holiday_ls"가 405번 실행됨 




    # data_lilst = os.listdir('data/')

    # if not f'{filename}.csv' in data_lilst:
    #     subprocess.run(['python', 'data_load.py', 
    #                     str(filename)])
        
    # elif not f'{filename}_crawled.csv' in data_lilst:
    #     subprocess.run(['python', 'crawl.py',
    #                     str(filename)])
        
    # elif not f'{filename}_sorted.csv' in data_lilst:
    #     subprocess.run(['python', 'sort_distance.py', 
    #                     str(filename), 
    #                     str(search_lat), 
    #                     str(search_lng), 
    #                     str(search_radius)])
        
    # if f'{filename}_sorted.csv' in data_lilst:
    #     subprocess.run(['python', 'get_time.py', 
    #                     str(filename), 
    #                     str(year), 
    #                     str(mon), 
    #                     str(day), 
    #                     str(search_time),
    #                     str(result_filename)])
            