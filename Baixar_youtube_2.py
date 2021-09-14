"""
Esse programa me redireciona para um site que faz downloads de vídeos, então é mais útil ver como é que abre uma 
aba no navegador etc
"""

import webbrowser

url="https://www.youtube.com/watch?v=-eIStUWXh-0&t=2541s"

url=url[:12]+'ss'+url[12:]

webbrowser.open(url)