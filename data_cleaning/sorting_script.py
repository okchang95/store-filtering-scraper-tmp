# 3. 거리별 필터링, 정리
# ------------------------------------------------------------------------
# 여기서 저장된 dataframe가지고 ~ 운영시간 정리 + 해당 시간에 열려있는 카페 최종 결과 출력

import pandas as pd
import os, sys

import sort_dist

## INPUTS (sample: kg아이티뱅크) ============================================
filename = sys.argv[1]          # 'cafe_jongro'
latitude = float(sys.argv[2])   # 37.571006515132865
longitude = float(sys.argv[3])  # 126.99251768504305
radius = float(sys.argv[4])     # 0.5 # km

## =======================================================================

# data path
abs_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(abs_root_path, 'data/')

crawled_df_path = os.path.join(data_dir, f'{filename}_crawled.csv')
sorted_df = sort_dist.distance(crawled_df_path, latitude, longitude, radius)

sorted_df.to_csv(os.path.join(data_dir, f'{filename}_sorted.csv'), index=False, encoding='utf-8-sig')
print('done!')
