package com.cocktailcaps.demo.Controller;

import com.cocktailcaps.demo.Dto.ChatGptResponseDto;
import com.cocktailcaps.demo.Dto.QuestionRequestDto;
//import com.cocktailcaps.demo.Service.ChatGptService;
import com.cocktailcaps.demo.Service.ChatService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RequiredArgsConstructor
@RestController
@RequestMapping("/chat-gpt")
public class ChatGptController {

    private final ChatService chatService;

//    public ChatGptController(ChatGptService chatGptService) {
//        this.chatGptService = chatGptService;
//    }
    @PostMapping("/question")
    public String test(@RequestBody String question){
        return chatService.getChatResponse(question);
        // hello gpt!
    }
//    @PostMapping("/question")
//    public ChatGptResponseDto sendQuestion(@RequestBody QuestionRequestDto requestDto) {
//        return chatGptService.askQuestion(requestDto);
//    }
}
