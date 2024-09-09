import requests
import json

# Ollama API의 엔드포인트 URL (로컬 서버의 URL 확인)
url = "http://localhost:11434/api/generate"  # Ollama가 실행 중인 API URL

def query_ollama(prompt):
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "model": "llama3.1",  # 사용 중인 모델 이름
        "prompt": prompt,
    }

    response = requests.post(url, headers=headers, json=data)
    
    # 응답 내용 확인
    response_text = response.text
    print("Response Text:", response_text)  # 응답 내용 출력

    # 응답 데이터를 JSON으로 변환
    try:
        # 여러 줄로 나뉘어 있는 경우를 처리
        response_lines = response_text.splitlines()
        json_strings = [line for line in response_lines if line.strip()]
        
        # JSON 배열이 아닐 경우 처리
        if not json_strings:
            return "No response from LLaMA"
        
        # 응답을 하나의 JSON 배열로 결합
        combined_json = '[' + ','.join(json_strings) + ']'
        response_json = json.loads(combined_json)
        
        # 모든 응답 파트를 모아서 조합
        final_response = ''.join(part.get('response', '') for part in response_json if part.get('done', False))
        
        # 만약 응답이 완전히 완료되지 않은 경우 추가 처리
        if not final_response:
            final_response = ''.join(part.get('response', '') for part in response_json)

        return final_response if final_response else "No complete response from LLaMA"
    except (json.JSONDecodeError, KeyError, TypeError) as e:
        return f"Failed to decode JSON response. Error: {str(e)}"

def save_response_to_file(user_input, response):
    with open("llama_responses.txt", "a", encoding="utf-8") as f:
        f.write(f"User Input: {user_input}\n")
        f.write(f"LLaMA Response: {response}\n")
        f.write("=" * 40 + "\n")

def main():
    while True:
        user_input = input("Enter your query (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break

        # Ollama에 질의하고 응답 받기
        response = query_ollama(user_input)
        print(f"LLaMA: {response}")

        # 응답을 파일에 저장
        save_response_to_file(user_input, response)

if __name__ == "__main__":
    main()
