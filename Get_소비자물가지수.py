import requests
import pandas as pd

# API URL
url = "https://kosis.kr/openapi/Param/statisticsParameterData.do"
params = {
    "method": "getList",
    "apiKey": "인증키없음",  # 여기에 실제 API 키를 넣으세요
    "itmId": "T+",
    "objL1": "T10+",
    "format": "json",
    "jsonVD": "Y",
    "prdSe": "M",
    "newEstPrdCnt": "3",
    "orgId": "101",
    "tblId": "DT_1J22003"
}

# API 요청
response = requests.get(url, params=params)
data = response.json()

# 데이터프레임에 필요한 칼럼만 추출
df = pd.DataFrame(data)
df = df[[
    "TBL_NM", "PRD_DE", "TBL_ID", "ITM_NM", "ITM_NM_ENG", "ITM_ID", 
    "UNIT_NM", "ORG_ID", "UNIT_NM_ENG", "C1_OBJ_NM", "C1_OBJ_NM_ENG",
    "DT", "PRD_SE", "C1", "C1_NM", "C1_NM_ENG", "LST_CHN_DE"
]]

# 결과 출력
print(df)
