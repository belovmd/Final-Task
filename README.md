RSS reader is a command utility, which receives RSS URL and prints the result in convenient output format

Input data has the following interface:

`rss_reader.py source [-h] [--version] [--verbose] [--json] [--limit LIMIT][--to-fb2][--output-path PATH]`
````
positional arguments:
source - URL which provides a RSS feed
optional arguments or date if you want use --date:
-h - prints this help page
--version - prints in stdout current version
--verbose - prints all logs in stdout
--json - prints news in JSON format
--limit LIMIT - limits the amount of news entries in the output 
-- date DATE - retrieves news from local storage by date. If there is no news in local storage - does nothing
-- to-fb2  - conver news to fb2 format. If not path saves file data.fb2 in file in home directory.
--output-path - CLI saves news in fb2 format along this path
--verbose - debug mode
````
How use?
````

	rss-reader https://news.yahoo.com/rss - CLI prints news from site
	
	rss-reader https://news.yahoo.com/rss --limit 1  - CLI prints one news form the site
	
	rss-reader https://news.yahoo.com/rss --limit 1 --verbose - debug mode to this command 
	
	rss-reader https://news.yahoo.com/rss --json - CLI prints news in json format from the site
	
	rss-reader https://news.yahoo.com/rss --to-fb2 - CLI saves data from the site im home directory
	
	rss-reader https://news.yahoo.com/rss --to-fb2 --path C:\Users\User\Desktop\HW5 - CLI saves data from site in the directiry  C:\Users\User\Desktop\HW5
	
	rss-redaer date --date 20191212 - CLI prints news from local storage by date
	
	rss-reader date --date 20191212 --fb2 - CLI saves data from local storage sorted by date in fb2 format in home directory
	
	rss-reader date --date 20191212 --fb2 --output-path C:\Users\User\Desktop\HW5  - CLI saves data from local storage sorted by date in fb2 format in home the directory

	
All data from sites saved in the local storage in json format. Name of this storage is news.json
````
JSON structure:
	 
```
{
		"title":[pub_date, link, img_url, description, formatted_date]  
		...
	},
Examle:
		{
  "FBI warned six months ago about loophole Pensacola shooter used to obtain a gun": [
    "Tue, 10 Dec 2019 15:56:04 -0500",
    "https://news.yahoo.com/fbi-warned-six-months-ago-about-loophole-pensacola-shooter-used-to-obtain-a-gun-205604918.html",
    "http://l2.yimg.com/uu/api/res/1.2/Rsnc.mnZ77eC3PEjNTn5fg--/YXBwaWQ9eXRhY2h5b247aD04Njt3PTEzMDs-/https://media-mbst-pub-ue1.s3.amazonaws.com/creatr-uploaded-images/2019-12/8f935820-1b85-11ea-95aa-3efcae4b593c",
    "More thn six months before the Dec. 6 shooting t  nvl bse in Penscol Fl. where  Sudi gunmn used  weon obtined using  hunting license exemtion the FBI issued  reort wrning bout recisely this loohole.",
    "20191210"
  ],
  "Rudy Giuliani&#39;s divorce battle ends, but legal troubles continue for Trump lawyer": [
    "Wed, 11 Dec 2019 11:49:35 -0500",
    "https://news.yahoo.com/rudy-giulianis-divorce-battle-ends-163602216.html",
    "http://l.yimg.com/uu/api/res/1.2/gAvsqnUWQRXB5v8gOItjKA--/YXBwaWQ9eXRhY2h5b247aD04Njt3PTEzMDs-/https://media.zenfs.com/en-us/usa_today_news_641/24fe5b925a685d3cb58f8387398d93c3",
    "Rudy Giulini President Donld Trum's lwyer hs settled his divorce fight with Judith Nthn. Federl rosecutors continue to investigte him.",
    "20191211"
  ]
}
Formatted date:
	Wed, 11 Dec 2019 11:49:35 -0500 = 20191211

#How install?
1) clone repository from https://github.com/PavelMartysiuk/Final-Task
2) `$cd rss_readerend
3)  `$python setup.py install
4) run `$rss_reader https://news.yahoo.com/rss --limit 2 --verbose`
	
