import sentiment_analysis.oseti as oseti
import pandas as pd

analyzer = oseti.Analyzer()

string_list = [
'なんだかしんどいと思ったら気圧のせいか…',
'なんだかしんどいと思ったら気圧のせいか…😵', 
'なんだかしんどいと思ったら気圧のせいか…(´+ω+｀)', 
'@mika_pollen_b なんだかしんどいと思ったら気圧のせいか…',
"なんだかしんどいと思ったら気圧のせいか…。https://twitter.com/terunekootenki/status/1524699067569229825?s=20&t=OC7RWlnr7ifTa2ExRZY-WQ",
"@mika_pollen_b なんだかしんどいと思ったら気圧のせいか…😵(´+ω+｀) https://twitter.com/terunekootenki/status/1524699067569229825?s=20&t=OC7RWlnr7ifTa2ExRZY-WQ",
"senの箸置きをもらった。", 
"senの箸置きをもらった😍", 
"senの箸置きをもらった(^^)/", 
"@mika_pollen_b senの箸置きをもらった。",
"senの箸置きをもらった https://twitter.com/sennostore/status/1482943517614014464?s=20&t=DnG8A50srEIOaZHZG-ubig",
"@mika_pollen_b senの箸置きをもらった😍(^^)/ https://twitter.com/sennostore/status/1482943517614014464?s=20&t=DnG8A50srEIOaZHZG-ubig",
"Rainbow Stansmithあまりの可愛さに靴紐を白色に付け替えて履いてる。",
"Rainbow Stansmithあまりの可愛さに靴紐を白色に付け替えて履いてる😭😭",
"Rainbow Stansmithあまりの可愛さに靴紐を白色に付け替えて履いてる( ；∀；)",
"@mika_pollen_b Rainbow Stansmithあまりの可愛さに靴紐を白色に付け替えて履いてる。",
"Rainbow Stansmithあまりの可愛さに靴紐を白色に付け替えて履いてる https://twitter.com/ABCMART_INFO/status/1519642632301215745?s=20&t=DnG8A50srEIOaZHZG-ubig",
"@mika_pollen_b Rainbow Stansmithあまりの可愛さに靴紐を白色に付け替えて履いてる😭😭( ；∀；) https://twitter.com/ABCMART_INFO/status/1519642632301215745?s=20&t=DnG8A50srEIOaZHZG-ubig",
"雨が止んで良かったね。",
"雨が止んで良かったね😊",
"雨が止んで良かったね(^^)",
"@mika_pollen_b 雨が止んで良かったね。",
"雨が止んで良かったね https://twitter.com/Yahoo_weather/status/1525579771723542528?s=20&t=DnG8A50srEIOaZHZG-ubig",
"@mika_pollen_b 雨が止んで良かったね😊(^^) https://twitter.com/Yahoo_weather/status/1525579771723542528?s=20&t=DnG8A50srEIOaZHZG-ubig",
"⛰🏫⛰⛰🚶🏻‍♀️🐗⛰⛰⛰⛰⛰",
"_(:3 」∠)__(┐「ε:)__(:3 」∠)_",
"@mika_pollen_b @mika_pollen_b @mika_pollen_b",
"_(:3 」∠)__(┐「ε:)__(:3 」∠)_。 https://twitter.com/mika_pollen_a/status/1526732089726742528?s=20&t=GmwN2Q7f5jj7FMh5bufGFw",
"@mika_pollen_b @mika_pollen_b @mika_pollen_b ⛰🏫⛰⛰🚶🏻‍♀️🐗⛰⛰⛰⛰⛰ _(:3 」∠)__(┐「ε:)__(:3 」∠)_ https://twitter.com/mika_pollen_a/status/1526732089726742528?s=20&t=GmwN2Q7f5jj7FMh5bufGFw",
"疲れた。泣きそう。もう消えたい。",
"疲れた。泣きそう。もう消えたい。😭😭",
"疲れた。泣きそう。もう消えたい。( ；∀；)",
"@mika_pollen_b 疲れた。泣きそう。もう消えたい。",
"疲れた。泣きそう。もう消えたい https://twitter.com/mika_pollen_a/status/1526735493815496705?s=20&t=GmwN2Q7f5jj7FMh5bufGFw",
"@mika_pollen_b 疲れた。泣きそう。もう消えたい。😭😭( ；∀；) https://twitter.com/mika_pollen_a/status/1526735493815496705?s=20&t=GmwN2Q7f5jj7FMh5bufGFw",
"またしんどくなるんじゃ無いかと思うと出かけるの憂鬱だ…。",
"またしんどくなるんじゃ無いかと思うと出かけるの憂鬱だ…。😓😓",
"またしんどくなるんじゃ無いかと思うと出かけるの憂鬱だ…。(/ _ ; )",
"@mika_pollen_b またしんどくなるんじゃ無いかと思うと出かけるの憂鬱だ…。",
"またしんどくなるんじゃ無いかと思うと出かけるの憂鬱だ… https://twitter.com/mika_pollen_a/status/1526741304205783040?s=20&t=GmwN2Q7f5jj7FMh5bufGFw",
"@mika_pollen_b またしんどくなるんじゃ無いかと思うと出かけるの憂鬱だ…。😓😓(/ _ ; ) https://twitter.com/mika_pollen_a/status/1526741304205783040?s=20&t=GmwN2Q7f5jj7FMh5bufGFw",
"やったー合格したー",
"やったー合格したー！！！！！",
"やったー合格したー？？？？？",
"えーん。憂鬱だー",
"えーん。憂鬱だー！！！！！",
"えーん。憂鬱だー？？？？？",
]

results = []

for string in string_list:
    results.append({'tweet_text': string, "oseti_score": analyzer.analyze(str(string))})

df = pd.DataFrame(results)
        
df.to_csv('./results.csv', index = False)