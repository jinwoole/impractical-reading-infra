# impractical-reading-slackbot
42서울 비실용적 책읽기 동아리 슬랙봇

https://api.slack.com/  

좌측 메뉴 중  
1. Event subscriptions -> Request URL
여기 API Gateway 엔드포인트 입력, 사실 이것만 되면 다 된 것.

2. 인증이 되었으면, Subscribe to bot event 섹션에서 이벤트 설정
이 경우는 member_joined_channel 이벤트 구독.

3. 유저와 상호작용 해야하니, OAuth & Permission에서 권한 설정
Bot Token Scopes -> Add -> chat:write 등 필요한 권한 설정


서버 구성 방법  
* fastapi로 간단하게 구성했고, 코드 참고 바람  
* 남는 라이트세일 자원이 있어서 활용함, 나중에 누가 인수인계할라나  