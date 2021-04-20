import random

LIST_GIFS = [
    "https://tenor.com/view/jorge-jesus-iguana-flamengo-benfica-gif-21038777",
    "https://tenor.com/view/jjboce-jorge-jesus-mariana-aguas-jorge-jesus-bonita-jorge-jesus-sporting-jorge-jesus-benfica-gif-18178654",
    "https://tenor.com/view/jorge-jesus-jorge-jesus-cinco-jorge-jesus-flamengo-jorge-jesus-benfica-benfica-gif-18140838",
    "https://tenor.com/view/jorge-jesus-jjboce-jorge-jesus-benfica-jorge-jesus-sporting-jorge-jesus-beibes-gif-18178422",
    "https://tenor.com/view/jorge-jesus-hand-gesture-sign-of-the-horns-gif-15159792",
    "https://tenor.com/view/jorge-jesus-benfica-mad-coach-soccer-gif-15791803",
    "https://tenor.com/view/jjboce-jorge-jesus-teikirize-take-it-easy-calm-down-gif-20428527",
    "https://tenor.com/view/bl8gifs-jjboce-jj-benfica-jorge-jesus-benfica-jj-bola-gif-18452782",
    "https://tenor.com/view/jjboce-jorge-jesus-quando-eu-quero-jj-quando-eu-quero-jorge-jesus-benfica-jj-benfica-gif-18207463",
    "https://tenor.com/view/jjboce-cincazero-cincazere-jorge-jesus-cinco-cincun-gif-18148068",
    "https://tenor.com/view/arrasar-arrasou-mister-jorge-jesus-jj-gif-20322350",
    "https://tenor.com/view/jorge-jesus-jj-jesus-jorge-benfica-gif-20375232",
    "https://tenor.com/view/jorge-jesus-enjoying-fun-happy-rock-and-roll-gif-15792148",
    "https://tenor.com/view/jorge-jesus-sporting-bola-gif-18130614",
    "https://tenor.com/view/jorge-jorge-jesus-bola-jesus-ican-see-you-gif-13838381",
    "https://tenor.com/view/bl8gifs-jjboce-jj-ai-lav-iu-ilove-you-iluv-u-gif-18497457",
    "https://tenor.com/view/bl8gifs-jjboce-jj-sete-golos-sete-golos-7golos-gif-18535182",
    "https://tenor.com/view/vamos-vamos-flamengo-jorge-jesus-hagan-caso-ou%c3%a7o-gif-15183173",
    "https://tenor.com/view/monkey-chimp-jjboce-tabacaria-do-maestro-jorge-jesus-gif-18682558",
    "https://tenor.com/view/caladinhos-sofrer-calate-calemse-pouco-barulho-gif-20326436",
    "https://tenor.com/view/bem-jogado-grande-jogada-nota-artistica-cincun-darwin-nunez-gif-20002435",
    "https://tenor.com/view/falar-de-qu%c3%aa-que-dizes-sem-sentido-fala-de-coisas-serias-conversa-da-treta-gif-19891393",
    "https://tenor.com/view/hay-hi-hello-bye-whats-up-gif-15767779"
]


def get_random_gif():
    length = len(LIST_GIFS)
    print(length)
    ran = random.randint(0, length - 1)
    return LIST_GIFS[ran]