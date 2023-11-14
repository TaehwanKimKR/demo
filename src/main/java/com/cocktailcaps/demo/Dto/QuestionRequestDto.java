package com.cocktailcaps.demo.Dto;

import lombok.Getter;

import java.io.Serializable;

@Getter
public class QuestionRequestDto implements Serializable {
    //question : front에서 3개 받아서 설정
    private String question;
}
