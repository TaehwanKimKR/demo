#!/usr/bin/env python
# coding: utf-8

# In[3]:
import pandas as pd
import json
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from http import HTTPStatus
from flask import Flask, jsonify, redirect, render_template, request, url_for
import requests
import json

app = Flask(__name__)

@app.route('/')
def root():
    return 'welcome to flask'


@app.route('/pytest', methods=['POST'])
def pytest():
    #json string으로 받기
    dto_json = request.get_json()
    #받은 json string을 파이썬 object로 변환(new_ingredients)
    #new_ingredients = json.loads(dto_json)
    new_ingredients = dto_json
    # 데이터 불러오기
    drink_df = pd.read_csv(r'C:\Users\USER\IdeaProjects\demo\src\main\pyt\data.csv')

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

    #output : json으로 묶기
    #print("예상 재료의 양은:")
    ret_object = {}
    for ingredient, amount in predicted_amounts.items():
        #dict 생성
        ret_object[ingredient] = amount
        #print(f"{ingredient}: {amount}")
    #print(ret_object)
    ret_string = json.dumps(ret_object, ensure_ascii=False)
    return ret_string
    #return jsonify({"data": ret_string, "status": HTTPStatus.OK})

if __name__ == '__main__':
    app.debug = True
    app.run(port=8080, debug=True)
# In[ ]:




