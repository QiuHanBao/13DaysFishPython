# conding='utf-8'
from bs4 import BeautifulSoup

str = """
<title>hello,内含段子</title>
    <script type="text/javascript" src='http://www.lovehhy.net/JS/Loading.js'></script>
    <script type="text/javascript" src="http://www.lovehhy.net/ViewExt.aspx"></script>
    <script type="text/javascript" src="http://images.lovehhy.net/js/video/videojs-ie8.min.js"></script>
    <div id="menu_bg">
        <div class="menu">
            <li><a href="http://www.lovehhy.net/Default.aspx"></a></li><li><a href="http://www.lovehhy.net/Joke/Detail/"  class="here"></a></li><li><a href="http://www.lovehhy.net/Yulu/Detail/" ></a></li><li><a href="http://www.lovehhy.net/ShiCi/Detail/" >zzz</a></li>
        </div>        
        <div class="menu">
            <li><a href="http://www.lovehhy.net/Default.aspx"></a></li><li><a href="http://www.lovehhy.net/Joke/Detail/"  class="here"></a></li><li><a href="http://www.lovehhy.net/Yulu/Detail/" ></a></li><li><a href="http://www.lovehhy.net/ShiCi/Detail/" ></a></li>
        </div>        
    </div>"""
soup = BeautifulSoup(str, 'lxml')

print(soup.title)
# print(soup.div)
