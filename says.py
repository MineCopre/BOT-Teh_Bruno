import random

LIST_SAYS = [
    "Há três fatores importantes: a vitória, golear, e a nota artística. Mas este último é na patinagem artística.",
    "Para mim, um treinador não tem passado nem futuro, só tem passado.",
    "Tamos tranquilos. Tamos? Agora já estava aqui a falar à Amadora.",
    "O Lopetegui... Lopetegue... Lopet... eu às vezes troco o nome [do treinador do FC Porto]. Eu agora disse bem, Lopetegue. Uma vez eu disse logo Lotopegue, já nem sei o que é que eu disse.",
    "O único campeonato da Europa que tá em andamento, é o campeonato brasileiro.",
    "É do dia a dia. É *peaners* para nós",
    "Dentro das quatro linhas é que é o meu campo. Fora das quatro linhas, não sei jogar nele.",
    "Lopetegui e Capela... só me engano nos nomes quando eu quero. Como viram, agora não me quis enganar. Está tudo dito.",
    "Vocês os quatro, façam aí um triângulo",
    "Não respondo a essa pergunta porque isso é um assunto do forno interno do clube.",
    "Querem fazer do rapaz o bode respiratório.",
    "Quando eles levam com um... \"AAAAAAI\", ai o quê, pá? ai o quê, oh? Levaste com um pau?",
    "Lá pó País de Gales não conta, conta é na baliza.",
    "O Oblak é um grande arqueiro, tem 2 paradas... defesas... paradas...",
    "Ontem tavas bonita...",
    "Como é que ele se chama, o baixinho? O Messi.",
    "Eu nunca tinha ouvisto um homem a dizer \"I love you\" para outro homem.",
    "Sou mais conhecido na Arábia Saudita que o Ronaldo, não tenho dúvidas.",
    "Teikirize? Ah okay!"
]


def get_random_say():
    length = len(LIST_SAYS)
    #print(length)
    ran = random.randint(0, length - 1)
    return LIST_SAYS[ran]


LIST_IMGS = [
    "https://upload.wikimedia.org/wikipedia/commons/1/18/2020-02-17_Encontro_com_T%C3%A9cnico_do_Flamengo%2C_Jorge_Jesus_%28cropped%29.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/17_02_2020_Encontro_com_T%C3%A9cnico_do_Flamengo_Jorge_Jesus_%2872157713150687982%29.jpg/250px-17_02_2020_Encontro_com_T%C3%A9cnico_do_Flamengo_Jorge_Jesus_%2872157713150687982%29.jpg",
    "https://images.beinsports.com/8IWAkq6wDkeRcgfc__H0-3WsLdw=/full-fit-in/1000x0/jorgejesus-cropped_mf95s6t532z419lmkw9hk2t8w.jpg",
    "https://i.imgflip.com/e8zws.jpg",
    "https://memegenerator.net/img/images/14563467.jpg", 
]

def get_random_img():
    length = len(LIST_IMGS)
    ran = random.randint(0, length-1)
    return LIST_IMGS[ran]