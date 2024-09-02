from datetime import datetime

def ranking_news(news_list):
    g = 1.8
    list_news = news_list

    for news in list_news:
        time_obj = datetime.strptime(news['time'], '%Y-%m-%d %H:%M:%S')
        t = (datetime.now() - time_obj).total_seconds() / 3600
        score = news['like_count'] / pow((t + 2), g)
        news['Score'] = score

    sorted_news = sorted(list_news, key=lambda x: x['Score'], reverse=True)

    return sorted_news