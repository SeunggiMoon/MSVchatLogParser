# MSVchatLogParser
Server chat log parser for MoonServer Archive Project

### 작동 과정
1. 로그 파일`(*.log)`을 불러옵니다.
2. 인코딩 오류로 인해 생성된 문자들을 제거합니다.
3. 채팅 시각과 대화 내용을 `파일명_parse.txt` 에 저장합니다.

### 예시
```
Original log: [11:11:20] [Async Chat Thread - #2/INFO]: <Uralskaya> 2농장은 평화롭다, 싱글을 하는 것 같애[m
           => [11:11:20] <Uralskaya> 2농장은 평화롭다, 싱글을 하는 것 같애
```
```
Original log: [12:32:40] [Server thread/INFO]: [0;32;22m[WEB] mom: [0;37;1m오늘 승기한테 갑옷 한 18개 수리를 부탁해야겠군[m
           => [12:32:40] [WEB] mom: 오늘 승기한테 갑옷 한 18개 수리를 부탁해야겠군
```
```
Original log: [17:18:09] [Server thread/INFO]: [Server] 하하 나는 다들 탱크 만들때 원점 타격할 비행기를 만들겠어
           => [17:18:09] [Server] 하하 나는 다들 탱크 만들때 원점 타격할 비행기를 만들겠어
```
```
Original log: [17:47:37] [Server thread/INFO]: P_Sho[/119.201.***.***:*****] logged in with entity id 477098 at ([MoonServer_nether]-51.699999 ...
           => [17:47:37]  P_Sho logged in with entity id 477098
```
___

### 유의 사항
* 로그 파일은 UTF-8로 인코딩되어 있어야 합니다. (추후 다른 인코딩도 지원 예정)
