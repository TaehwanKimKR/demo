package com.cocktailcaps.demo.Controller;

import org.python.*;
import org.python.core.PyFunction;
import org.python.core.PyInteger;
import org.python.core.PyObject;
import org.python.util.PythonInterpreter;
import org.springframework.web.bind.annotation.*;

@RestController
public class PythonController {
    private static PythonInterpreter interpreter;

    @PostMapping("/pytest")
    public String pytest(@RequestBody String termJson){
        RestTemplate restTemplate = new RestTemplate();

        interpreter = new PythonInterpreter();
        interpreter.execfile("src/main/pyt/test.py");
        interpreter.exec("print(testFunc(5, 10))");

        PyFunction pyFunction = interpreter.get("testFunc", PyFunction.class);

        int a = 10;
        int b = 20;

        PyObject pyobj = pyFunction.__call__(new PyInteger(a), new PyInteger(b));
        System.out.println(pyobj.toString());

        return pyobj.toString();
    }

//    @GetMapping("/trytest")
//    public String trytest(){
//        interpreter = new PythonInterpreter();
//        interpreter.execfile("src/main/pyt/trying_1108.py");
//
//    }

}
