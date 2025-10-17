import webbrowser
import pywhatkit

# Crea ventanas en el navegador predeterminado a peticion
def Search_pages(request: str) -> bool:
    if request.__contains__('youtube'):
        if  request.__contains__('en youtube'):
            keyword = request.split('busca')[1].replace('en youtube', '').strip()
            webbrowser.open_new_tab(f'https://www.youtube.com/results?search_query={keyword.replace(' ', '+')}')
        else:
            webbrowser.open_new_tab('https://www.youtube.com/')
    elif request.__contains__('en google'):
        keyword = request.split()[2]
        pywhatkit.search(keyword)
        print(keyword)
    else:
        print(f'No se que trataste de decir con "{request}"')
        return False
    return True