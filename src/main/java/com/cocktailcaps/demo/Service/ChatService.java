package com.cocktailcaps.demo.Service;

import io.github.flashvayne.chatgpt.dto.chat.MultiChatMessage;
import io.github.flashvayne.chatgpt.service.ChatgptService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.Arrays;

//opensource-flashvayne 사용
@Service
@RequiredArgsConstructor
public class ChatService{

    private final ChatgptService chatgptService;

    public String getChatResponse(String prompt) {
        // ChatGPT 에게 질문 전달
        return chatgptService.multiChat(Arrays.asList(new MultiChatMessage("user",prompt)));
    }
}