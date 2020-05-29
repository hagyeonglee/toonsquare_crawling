# toonsquare_crawling
static
   - style.css : 전체적인 css스타일 적용(표, 버튼 스타일)
   - supervise.css : supervise하는 페이지의 css 스타일

templates
   - editsupervise.html : 수퍼바이즈한 데이터를 고치는 페이지에 대한 html 파일 : 1차적으로 수퍼바이즈가 완료된 데이터를 다시 고치고 싶을 때 보여지는 프론트 엔드 화면
   - selectview.html : 1차 수퍼바이즈가 진행되는 화면 : 각 문장에서 느껴지는 감정에 해당하는 버튼을 클릭한 후 SAVE버튼을 무조건 눌러주어야만 저장이된다. 수퍼바이즈는 각 페이지 넘버를 입력하여 화면 이동하여 같은 방법으로 진행하면 된다.
   - submitsup.html : 수퍼바이즈한 데이터를 고치는 페이지에 대한 html 파일 (2) : 수퍼바이즈 -> 수정 단계를 거친 최종의 supervised 데이터가 보여지느 프론트 화면
   - supbervise.html : 1차 수퍼바이즈가 끝난 데이터들에 대해 결과를 보여주는 화면 역시, SAVE 버튼을 눌러야 저장이 되고 결과가 반영된다.(이때, csv파일로도 저장된다.)-> supervised_first.csv 라는 파일명으로 저장
   - view.html : 홈 루트 페이지에서 보여지는 프론트 화면 이때, RESULT를 누르면 당연히 수퍼바이즈가 이뤄지지 않았으므로 supervised칸이 NaN으로 표시된다.
   
app.py : flask 앱 작동 -> 전체적인 대쉬보드 기능 구현

naver_webtoon_comments.csv -> 크롤링한 네이버 댓글 데이터를 인공지능이 한 번 감정 분석을 함.

supervised_first.csv -> 1차 수퍼바이즈한 데이터파일
 
supervised.csv -> 최종 수퍼바이즈 데이터 파일