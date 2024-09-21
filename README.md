# ⌨ 키워드 기반 국내 뉴스 RSS 피드 앱

본 프로젝트는 국내 뉴스 RSS 피드를 사용하여, 사용자가 관심 있는 주제(키워드)를 입력하면 관련된 국내 뉴스를 실시간으로 검색하고, 뉴스의 제목과 요약을 보여주는 스트림릿 기반의 앱을개발하는 것을 목표로 합니다. 이 앱은 사용자가 입력한 키워드에 따른 뉴스 기사들을 사용자가 설정한 개수만큼 뉴스를 수집 및 요약하여 화면에 표시하고, 단어 빈도수를 워드클라우드 형태로 시각화하여 제공하는 기능을 갖추고 있습니다. 

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://rsskorea.streamlit.app//)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
