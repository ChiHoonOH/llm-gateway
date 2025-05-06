# 학습 방향 
 - 전체 흐름 -> 세부 내용으로
# llm-gateway(전체 흐름)
## 기술명
-  Langchain, FastAPI, Boto, SageMaker Studio

front -> FastAPI         -> Langchain                 -> bedrock(boto)
        Controller)         - Service(리소스)          - boto 실행을 위한 wrapper, 메서드 양식 통일을 위해 필요(?)
			    - http 통신(boto)          - llm 모델 호출(boto) 


chain = LLMChain(
    prompt=prompt,
    llm=llm,
    memory=memory
)

prompt 형식 및 내용으로, llm 모델에게 내용을 보내겠다. 해당 메모리 정도로

prompt = PromptTemplate(
    input_variables=["question"],
    template="당신은 친절한 비서입니다. 질문에 답하세요: {question}"
)

llm = Bedrock(
    model_id="anthropic.claude-v2",
    region_name="us-east-1"
)

Bedrock 개체 내부는
prompt = {"prompt": "Hello", "max_tokens": 100}
client = boto3.client("bedrock-runtime")
response = client.invoke_model(modelId=..., body=json.dumps(prompt))
와 같은 형식으로 되어 있음

response = chain.run("내일 날씨 알려줘")
