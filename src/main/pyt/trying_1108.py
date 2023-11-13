#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

# 데이터 불러오기
drink_df = pd.read_csv(r'경로')

# 결측치를 해당 열의 평균값으로 대체
drink_df.fillna(drink_df.mean(numeric_only=True), inplace=True)

# OneHotEncoder로 범주형 변수를 원핫 인코딩
encoder = OneHotEncoder()
X = encoder.fit_transform(drink_df[['Alchol', 'Drink', 'Syrup']]).toarray()

# 타깃 변수 설정
Y = drink_df[['A_measure', 'D_measure', 'S_measure']]

# 선형 회귀 모델 학습
model = LinearRegression()
model.fit(X, Y)

new_ingredients = {
    'Alchol': input("가지고 있는 술을 입력하세요(soju/beer/liquor 등): ").lower(),
    'Drink': input("가지고 있는 음료를 입력하세요(coke/lemonade 등): ").lower(),
    'Syrup': input("가지고 있는 시럽이름을 입력하세요(sugar/lemon 등): ").lower()
}

def encode_ingredients(new_ingredients, encoder, model):
    try:
        # 입력 데이터를 원핫 인코딩으로 변환
        encoded_ingredients = encoder.transform(pd.DataFrame([new_ingredients])).toarray()

        # 모델에 입력 데이터를 전달하고 예상 재료 양 반환
        predicted_amounts = model.predict(encoded_ingredients)

        # 결과를 딕셔너리로 반환
        result_sum=int(predicted_amounts[0][0])+int(predicted_amounts[0][1])+int(predicted_amounts[0][2])
        
        result = {
            'Alchol': int(int(predicted_amounts[0][0])*240/result_sum),
            'Drink': int(int(predicted_amounts[0][1])*240/result_sum),
            'Syrup': int(int(predicted_amounts[0][2])*240/result_sum)
        }

        return result
    except ValueError as e:
        if "Found unknown categories" in str(e):
            # 알 수 없는 카테고리가 발견된 경우 처리
            result = {
                'Alchol': 60,  # 원하는 값으로 설정가능
                'Drink': 170,
                'Syrup': 10
            }
            return result
        else:
            # 다른 예외에 대한 처리를 추가할 수 있습니다?
            raise e

predicted_amounts = encode_ingredients(new_ingredients, encoder, model)

print("예상 재료의 양은:")
for ingredient, amount in predicted_amounts.items():
    print(f"{ingredient}: {amount}")



# In[ ]:




