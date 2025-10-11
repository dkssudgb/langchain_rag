from langchain_core.messages import AIMessageChunk

def stream_response(response, return_output: bool = False):
    """모델의 스트리밍 응답을 문자열로 반환 + 콘솔에 실시간 출력."""
    answer = ""
    for token in response:
        if isinstance(token, AIMessageChunk):
            answer += token.content
            print(token.content, end="", flush=True)
        elif isinstance(token, str):
            answer += token
            print(token, end="", flush=True)
    if return_output:
        return answer
