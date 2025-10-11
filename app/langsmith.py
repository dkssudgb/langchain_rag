import os

def langsmith(project_name: str | None = None, set_enable: bool = True):
    if set_enable:
        langchain_key = os.environ.get("LANGCHAIN_API_KEY", "")
        langsmit_key = os.environ.get("LANGSMITH_API_KEY", "")
        result = langchain_key if len(langchain_key.strip()) >= len(langsmit_key.strip()) else langsmit_key
        if result.strip() == "":
            print("LangChain/LangSmith API Key가 설정되지 않았습니다.")
            return

        os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"
        os.environ["LANGSMITH_TRACING"]  = "true"
        if project_name:
            os.environ["LANGSMITH_PROJECT"] = project_name
            print(f"LangSmith 추적을 시작합니다.\n[프로젝트명] {project_name}")
    else:
        os.environ["LANGSMITH_TRACING"] = "false"
        print("LangSmith 추적을 하지 않습니다.")
