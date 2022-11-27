from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from dados import *

###### Cores usadas #######
cor1 = "#3d3d3d"  # preta
cor2 = "#fafcff"  # branca
cor3 = "#21c25c"  # verde
cor4 = "#eb463b"  # vermelha
cor5 = "#dedcdc"  # cinza
cor6 = "#3080f0"  # azul


fundo = cor2

janela = Tk()
janela.title('Pokedex ')
janela.geometry('550x550')
janela.config(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use('clam')

# CREATE FRAME
frame_pokemon = Frame(janela, width=550, height=280, bg=cor5, relief='flat')
frame_pokemon.grid(row=1, column=0)


pok_nome = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font='Fixedsys 20', bg=cor2)
pok_nome.place(x=12, y=10)

pok_tipo = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font='Ivy 10 bold', bg=cor2)
pok_tipo.place(x=12, y=50)

pok_id = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font='Ivy 9 bold', bg=cor2)
pok_id.place(x=12, y=75)


def trocar_pokemom(chave):
    global image_poke, pok_imagem

    # fundo
    frame_pokemon['bg'] = pokemon[chave]["tipo"][3]
    pok_nome['bg'] = pokemon[chave]["tipo"][3]
    pok_tipo['bg'] = pokemon[chave]["tipo"][3]
    pok_id['bg'] = pokemon[chave]["tipo"][3]
    pok_nome.lift()
    pok_tipo.lift()
    pok_id.lift()
    
    

    # TIPO / ATRIBUT / HABLDS / STATS
    pok_nome['text'] = chave
    pok_tipo['text'] = pokemon[chave]["tipo"][1]
    pok_id['text'] = pokemon[chave]["tipo"][0]
    pok_hp['text'] = pokemon[chave]["status"][0]
    pok_ataq['text'] = pokemon[chave]["status"][1]
    pok_def['text'] = pokemon[chave]["status"][2]
    pok_speed['text'] = pokemon[chave]["status"][3]
    pok_total['text'] = pokemon[chave]["status"][4]
    pok_hab['text'] = pokemon[chave]["habilidades"][0]
    pok_hab1['text'] = pokemon[chave]["habilidades"][1]

    # IMAGE
    link = pokemon[chave]["tipo"][2]
    
    # imagens
    image_poke = Image.open(link)
    image_poke = image_poke.resize((240, 240))
    image_poke = ImageTk.PhotoImage(image_poke)

    pok_imagem = Label(frame_pokemon,image=image_poke, relief='flat', bg=cor2)
    pok_imagem.place(x=60, y=50)

    pok_tipo.lift # sobrepor
    pok_tipo.lift()
    pok_imagem['bg'] = pokemon[chave]["tipo"][3]



# PT1
pok_stats = Label(janela, text='Status', relief='flat', anchor=CENTER, font='Verdana 20', bg=cor2)
pok_stats.place(x=15, y=310)

pok_hp = Label(janela, text='', relief='flat', anchor=CENTER, font='Verdana 10', bg=cor2)
pok_hp.place(x=15, y=360)

pok_ataq = Label(janela, text='', relief='flat', anchor=CENTER, font='Verdana 10', bg=cor2)
pok_ataq.place(x=15, y=388)

pok_def = Label(janela, text='', relief='flat', anchor=CENTER, font='Verdana 10', bg=cor2)
pok_def.place(x=15, y=420)

pok_speed = Label(janela, text='', relief='flat', anchor=CENTER, font='Verdana 10', bg=cor2)
pok_speed.place(x=15, y=450)

pok_total = Label(janela, text='', relief='flat', anchor=CENTER, font='Verdana 10', bg=cor2)
pok_total.place(x=15, y=480)

# PT2
pok_stats = Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font='Verdana 20', bg=cor2)
pok_stats.place(x=180, y=310)

pok_hab = Label(janela, text='', relief='flat', anchor=CENTER, font='Verdana 10', bg=cor2)
pok_hab.place(x=180, y=360)

pok_hab1 = Label(janela, text='', relief='flat', anchor=CENTER, font='Verdana 10', bg=cor2)
pok_hab1.place(x=180, y=388)

# BUTTONS

# imagens
image_cabe1 = Image.open('images/cabeca-pikachu.png')
image_cabe1 = image_cabe1.resize((40, 40))
image_cabe1 = ImageTk.PhotoImage(image_cabe1)

b_pok_1 = Button(janela,command=lambda:trocar_pokemom('Pikachu') ,text='Pikachu',width=150,image=image_cabe1,font='Verdana 12',padx =5,compound=LEFT ,relief='raised',overrelief=RIDGE,anchor=NW, bg=cor2)
b_pok_1.place(x=380, y=10)


image_cabe2 = Image.open('images/cabeca-bulbasaur.png')
image_cabe2 = image_cabe2.resize((40, 40))
image_cabe2 = ImageTk.PhotoImage(image_cabe2)

b_pok_2 = Button(janela,command=lambda:trocar_pokemom('Bulbasaur') ,text='Bulbasaur',width=150,image=image_cabe2,font='Verdana 12',padx =5,compound=LEFT ,relief='raised',overrelief=RIDGE,anchor=NW, bg=cor2)
b_pok_2.place(x=380, y=65)


image_cabe3 = Image.open('images/cabeca-charmander.png')
image_cabe3 = image_cabe3.resize((40, 40))
image_cabe3 = ImageTk.PhotoImage(image_cabe3)

b_pok_3 = Button(janela,command=lambda:trocar_pokemom('Charmander') ,text='Charmander',width=150,image=image_cabe3,font='Verdana 12',padx =5,compound=LEFT ,relief='raised',overrelief=RIDGE,anchor=NW, bg=cor2)
b_pok_3.place(x=380, y=120)


image_cabe4 = Image.open('images/cabeca-gengar.png')
image_cabe4 = image_cabe4.resize((40, 40))
image_cabe4 = ImageTk.PhotoImage(image_cabe4)

b_pok_4 = Button(janela,command=lambda:trocar_pokemom('Gengar') ,text='Gengar',width=150,image=image_cabe4,font='Verdana 12',padx =5,compound=LEFT ,relief='raised',overrelief=RIDGE,anchor=NW, bg=cor2)
b_pok_4.place(x=380, y=175)


image_cabe5 = Image.open('images/cabeca-gyarados.png')
image_cabe5 = image_cabe5.resize((40, 40))
image_cabe5 = ImageTk.PhotoImage(image_cabe5)

b_pok_5 = Button(janela,command=lambda:trocar_pokemom('Gyarados') ,text='Gyarados',width=150,image=image_cabe5,font='Verdana 12',padx =5,compound=LEFT ,relief='raised',overrelief=RIDGE,anchor=NW, bg=cor2)
b_pok_5.place(x=380, y=230)


image_cabe6 = Image.open('images/cabeca-dragonite.png')
image_cabe6 = image_cabe6.resize((40, 40))
image_cabe6 = ImageTk.PhotoImage(image_cabe6)

b_pok_6 = Button(janela,command=lambda:trocar_pokemom('Dragonite') ,text='Dragonite',width=150,image=image_cabe6,font='Verdana 12',padx =5,compound=LEFT ,relief='raised',overrelief=RIDGE,anchor=NW, bg=cor2)
b_pok_6.place(x=380, y=285)



janela.mainloop()


