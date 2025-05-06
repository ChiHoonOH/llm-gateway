# llm-gateway
## 기술명
-  Langchain, FastAPI, Boto, SageMaker Studio



Langchain, FastAPI, boto, SageMaker Studio 

front -> FastAPI         -> Langchain                 -> bedrock(boto)
        Controller)          Service(리소스)          boto 실행을 위한 wrapper, 메서드 양식 통일을 위해 필요(?)
				http 통신(boto)                               llm 모델 호출(boto) 
