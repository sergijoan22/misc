import requests
from bs4 import BeautifulSoup
import emoji


# funcion para devolver uno u otro emoji dependiendo de la condición climatológica
# emoji name must be surrounded by : before and after
# List of emoji names:
# https://www.webfx.com/tools/emoji-cheat-sheet/
'''
def emoji_clim_cond(clim_cond):
    if clim_cond == 'Sunny':
        simb = emoji.emojize(':sunny: :sunny: :sunny:', language='alias')
    elif clim_cond == 'Clear Night':
        simb = emoji.emojize(':crescent_moon: :crescent_moon: :crescent_moon:', language='alias')
    elif clim_cond == 'Partly Cloudy':
        simb = emoji.emojize(':cloud: :cloud: :sunny:', language='alias')
    elif clim_cond == 'Scattered Showers':
        simb = emoji.emojize(':cloud: :cloud: :droplet:', language='alias')
    elif clim_cond == 'Partly Cloudy Night':
        simb = emoji.emojize(':crescent_moon: :cloud: :cloud:', language='alias')
    elif clim_cond == 'Mostly Cloudy':
        simb = emoji.emojize(':cloud: :cloud: :sunny:', language='alias')
    elif clim_cond == 'Mostly Clear Night':
        simb = emoji.emojize(':crescent_moon: :crescent_moon: :cloud:', language='alias')
    elif clim_cond == 'Rain':
        simb = emoji.emojize(':droplet: :droplet: :droplet:', language='alias')
    elif clim_cond == 'Mostly Sunny':
        simb = emoji.emojize(':sunny: :sunny: :cloud:', language='alias')
    else:
        simb = emoji.emojize(':confused: :confused: :confused:', language='alias')
    return simb
'''










# get the html from the web
r = requests.get("https://weather.com/es-ES/tiempo/hoy/l/e6ef5cffd86534ff3e76c51dbda24ee1e4a4c3780efa486bc4637f4aec0bf7b8")


# guardamos el html en un archivo
with open('tiempo_valencia.html', "w", encoding="utf-8") as f:
    f.write(r.text)

# convert to beautiful soup object
soup = BeautifulSoup(r.text, 'lxml')


# de todas las iteraciones que se va a hacer con los tags de span, id guardando
# por que numero de iteracion va
global found
global temp_morning
global temp_afternoon
global temp_night
global temp_earlymorn
global condition_morning
global condition_afternoon
global condition_night
global condition_earlymorn
global a_with_morning
global a_with_afternoon
global a_with_night
global a_with_dawn
found = 0
a_with_morning = 0
a_with_afternoon = 0
a_with_night = 0
a_with_dawn = 0

# find tags with name <a> whose attribut href has a concrete value
texto_href = "/es-ES/tiempo/horario/l/e6ef5cffd86534ff3e76c51dbda24ee1e4a4c3780efa486bc4637f4aec0bf7b8"
enlaces = soup.find_all('a', href = texto_href)

# iterated each of the filtered <a>
for enlace in enlaces:
    all_span = enlace.find_all('span', 'data-testid' == "TemperatureValue")

    # show the content of each filtered <span> tag
    # and in which order were found
    for i in all_span:
        if found == 1:
            temp_morning = i.string
            condition_morning = i.title
        if found == 2:
            temp_afternoon = i.string
        if found == 3:
            temp_night = i.string
        if found == 4:
            temp_earlymorn = i.string
        found = 0
        if i.string == 'Mañana':
            found = 1
            a_with_morning = 1
        if i.string == 'Tarde':
            found = 2
            a_with_afternoon = 1
        if i.string == 'Noche':
            found = 3
            a_with_night = 1
        if i.string == 'Madrugada':
            found = 4
            a_with_dawn = 1


    if a_with_morning == 1:
        a_with_morning = 0
        condition_morning = enlace.title.string

    if a_with_afternoon == 1:
        a_with_afternoon = 0
        condition_afternoon = enlace.title.string

    if a_with_night == 1:
        a_with_night = 0
        condition_night = enlace.title.string  

    if a_with_dawn == 1:
        a_with_dawn = 0
        condition_dawn = enlace.title.string


print('\n --------------------------------------------------------------')
print('Mañana:',temp_morning, '--' , condition_morning, '\n')
print('Tarde:',temp_afternoon, '--' , condition_afternoon, '\n')
print('Noche:', temp_night, '--' , condition_night, '\n')
print('Amanecer', temp_earlymorn, '--' , condition_dawn)
print('--------------------------------------------------------------')



# mostrar las temp y las cond clim en emojis
'''
print('\n --------------------------------------------------------------')
print('Mañana:',temp_morning, emoji_clim_cond(condition_morning), '\n')
print('Tarde:',temp_afternoon, emoji_clim_cond(condition_afternoon), '\n')
print('Noche:', temp_night, emoji_clim_cond(condition_night), '\n')
print('Amanecer', temp_earlymorn, emoji_clim_cond(condition_dawn),)
print('--------------------------------------------------------------')
'''


input()


'''
# guardamos el html en un archivo
with open('tiempo_valencia.html', "w", encoding="utf-8") as f:
    f.write(r.text)

'''