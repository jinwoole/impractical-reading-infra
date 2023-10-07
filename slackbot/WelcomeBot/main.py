from fastapi import FastAPI, Request
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

app = FastAPI()
TOKEN = 비밀

slack_client = WebClient(token=TOKEN)

# Slack Challenge 요청을 처리하는 엔드포인트
@app.post("/slack/events")
async def slack_event_challenge(request: Request):
    # Slack에서 전송한 요청
    data = await request.json()

    # Slack Challenge 이벤트를 확인
    if "challenge" in data:
        # Slack에서 제공한 Challenge 값을 반환
        return {"challenge": data["challenge"]}

    # 멤버 가입 이벤트를 처리
    event_type = data.get("event", {}).get("type")
    if event_type == "team_join":
        user_id = data["event"]["user"]["id"]
        try:
            # 환영 DM 전송
            response = await slack_client.chat_postMessage(
                channel=user_id,
                text=f"""<@{user_id}>님, 환영합니다! 비실용적 책읽기 모임에 참여해 주셔서 감사합니다.
#약속정하기, #책선정 등의 채널을 둘러보고 원하는 모임에 참여하거나 만들어보세요!"""
            )
            return {"message": "환영 DM이 성공적으로 전송되었습니다."}
        except SlackApiError as e:
            return {"error": f"DM 전송 중 오류 발생: {e.response['error']}"} 
        
    # Slack `channel_join` 이벤트 처리
    elif event_type == "member_joined_channel":
        user_id = data["event"]["user"]
        channel_id = data["event"]["channel"]
        if channel_id != "C060PSL2WL8":
            return
        try:
            # 환영 DM 전송, 위의 방법이 잘 작동할지 몰라 그냥 #따뜻한-환영 채널 개설함
            response = slack_client.chat_postMessage(
                channel=channel_id,
                text=f"""<@{user_id}>님, 환영합니다! 비실용적 책읽기 모임에 참여해 주셔서 감사합니다.
#약속정하기, #책선정 등의 채널을 둘러보고 원하는 모임에 참여하거나 만들어보세요!"""
            )
            return {"message": "환영 메시지가 성공적으로 전송되었습니다."}
        except SlackApiError as e:
            return {"error": f"환영 메시지 전송 중 오류 발생: {e.response['error']}"}

    # 혹시 다른거 할 거 있으면 아래에 추가

    # Slack Challenge 이외의 이벤트는 무시
    
    return {"message": "Ignored"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)