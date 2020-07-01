# MSVchatLogParser
Server chat log parser for MoonServer Archive Project

### 작동 과정
1. 로그 파일`(*.log)`을 불러옵니다.
2. 인코딩 오류로 인해 생성된 문자들을 제거합니다.
3. 채팅 시각과 대화 내용을 `파일명_parse.txt` 에 저장합니다.

### 예시
___

### 유의 사항
* 로그 파일은 UTF-8로 인코딩되어 있어야 합니다. (추후 다른 인코딩도 지원 예정)
