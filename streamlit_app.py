import streamlit as st
import feedparser
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
import html
import re

# RSS 피드 URL 목록 (국내 뉴스)
RSS_FEEDS = {
    '한겨레': 'https://www.hani.co.kr/rss/',
    '경향신문': 'https://www.khan.co.kr/rss/rssdata/total_news.xml',
    '조선일보': 'http://news.chosun.com/site/data/rss/rss.xml',
    '연합뉴스': 'https://www.yna.co.kr/rss/all',
    '동아일보': 'https://rss.donga.com/total.xml',
    'KBS 뉴스': 'http://world.kbs.co.kr/rss/rss_news.htm?lang=k',
    'MBC 뉴스': 'https://imnews.imbc.com/rss/news/news_00.xml',
    'SBS 뉴스': 'https://news.sbs.co.kr/news/SectionRssFeed.do?sectionId=01',
}

def fetch_news(feed_url):
    feed = feedparser.parse(feed_url)
    news_items = []
    for entry in feed.entries:
        title = html.unescape(entry.title)
        summary = html.unescape(entry.summary)
        summary = re.sub('<[^<]+?>', '', summary)  # HTML 태그 제거
        news_items.append({"title": title, "link": entry.link, "summary": summary})
    return news_items

def generate_wordcloud(text):
    # 폰트 파일 경로 설정
    font_path = os.path.join(os.path.dirname(__file__), 'NanumGothic.ttf')
    
    # 폰트 파일이 존재하는지 확인
    if not os.path.exists(font_path):
        st.error(f"폰트 파일을 찾을 수 없습니다: {font_path}")
        return
    
    # 워드클라우드 생성
    wordcloud = WordCloud(width=800, height=400, background_color='white', font_path=font_path).generate(text)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    
    # Streamlit에 그리기
    st.pyplot(plt)

# Streamlit 앱 코드
st.title("국내 뉴스 RSS 피드")

# 관심 있는 주제 및 키워드 입력
keyword = st.text_input("관심 있는 주제나 키워드를 입력하세요:", "북한")
num_news = st.slider("보여줄 뉴스 개수를 선택하세요:", 1, 20, 10)

if st.button("뉴스 보기"):
    news_data = []
    for source, url in RSS_FEEDS.items():
        news_items = fetch_news(url)
        for item in news_items:
            # 대소문자 구분 없이 키워드 비교
            if keyword.lower() in item['title'].lower():
                news_data.append(item)
    
    # 선택한 뉴스 개수만큼 출력
    if len(news_data) > num_news:
        news_data = news_data[:num_news]
    
    # 출력된 뉴스 표시
    if news_data:
        for news in news_data:
            st.subheader(news['title'])
            st.write(news['summary'])
            st.write(f"[링크로 이동]({news['link']})")

        # 워드클라우드 생성
        all_titles = ' '.join(item['title'] for item in news_data)
        generate_wordcloud(all_titles)
    else:
        st.write("해당 키워드에 대한 뉴스가 없습니다.")
