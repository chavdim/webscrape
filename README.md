# Webscrape
Extract particular html elements from url

[![asciicast](https://asciinema.org/a/9mairg5nr70sjjq2v531owdvg.png)](https://asciinema.org/a/9mairg5nr70sjjq2v531owdvg)

# Usage
w = Webscraper()<br>
w.getHtml(url)
<br>
r = w.getElementsOfType("span",contains = "review-text" ) 
<br><br>
This will extract all span type elements that contain the text "review-text"
<br>
that are contained in the html fetched from the url.
<br><br>such as: <br>
\<span id="review-text"> ... \</span>
<br> or <br>
\<span class="review-text"> ... \</span>

#Requirements
requests library:<br>
https://github.com/kennethreitz/requests
