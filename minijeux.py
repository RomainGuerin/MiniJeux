"""
Mini Jeux
Romain Guérin
Les personnages citées appartiennent à leurs propriétaires respectifs.
"""

import sys
import time
import random

record_minijeux = { 
      "partieJustePrix" : 0,
      "victoireJustePrix": 0,
      "partieRoulette" : 0,
      "victoireRouletteNormal": 0,
      "victoireRouletteDifficile": 0,
      "victoireRouletteTotalDifficile": 0,
      "partieJanken" : 0,
      "victoireJanken": 0, 
      "partiePendu" : 0,
      "victoirePendu": 0
      }

# ********************************************************************************
# Mini Jeux
# ********************************************************************************

def minijeux():
      print("\nQue veux-tu faire ?")
      print("\033[33m[Jouer]    [Résumer]    [Sortir]\033[0m")
      reponse_jeu = ""

      while not reponse_jeu == "jouer" and not reponse_jeu == "resumer" and not reponse_jeu == "résumer" and not reponse_jeu == "sortir":
            reponse_jeu = input("Que souhaites-tu faire ? ─> ").lower()

      if reponse_jeu == "jouer":
            print("\nDonc tu veux jouer ?!")
            print("\nAucun argent n'est parié ! Mais...")
            print("\033[31m/!\ ATTENTION /!\ \033[0m Les jeux d'argents sont dangereux !!!\n")
            time.sleep(1)
            choix_jeu = ""

            while not choix_jeu == "juste prix" and not choix_jeu == "la roulette" and not choix_jeu == "janken" and not choix_jeu == "pendu":
                  choix_jeu = input("Choisis un jeu : \033[33m[Juste Prix]    [La Roulette]    [Janken]    [Pendu]\033[0m\n> ").lower()

            if choix_jeu == "juste prix":
                  print("\nBienvenue au jeu du Juste Prix !!!!\n")
                  time.sleep(1)

                  print("Les règles sont simples :")
                  print(" - Trouve le nombre exact entre 10 et 10 000 Yen !")
                  print(" - Tu as 50 tentatives !")
                  print(" - Entre la valeur 0, si tu souhaites abandonner...\n")
                  time.sleep(2)

                  dirigejeux("debut", justeprix)

            elif choix_jeu == "la roulette":
                  print("\nBienvenue à La Roulette !!!")
                  time.sleep(1)
                  
                  difficulte = ""
                  while not difficulte == "normal" and not difficulte == "difficile":
                        difficulte = input("\nChoisis le niveau de difficulté : [Normal]    [Difficile]\n> ").lower()
                  time.sleep(1)

                  print("\nLes règles sont simples :")
                  print(" - Il faut choisir entre les 3 couleurs suivante : le \033[32m[Vert]\033[0m, le \033[31m[Rouge]\033[0m et le \033[30m[Noir]\033[0m")
                  print(" -> Pour trouver la bonne couleur")
                  if difficulte == "difficile":
                        print(" - Il faut choisir un chiffre/nombre entre \033[33m1 et 36\033[0m")
                        print(" -> Pour trouver le bon chiffre/numéro")

                  time.sleep(2)

                  dirigejeux("debut", laroulette, difficulte)

            elif choix_jeu == "janken":
                  print("\nBienvenue au Janken !!!")
                  time.sleep(1)

                  print("\nLa règle est simple :")
                  print(" - Il faut choisir entre : la \033[33m[Pierre]\033[0m, le \033[33m[Papier]\033[0m et les \033[33m[Ciseaux]\033[0m")
                  print("                              石 ishi       紙 kami      はさみ hasami\n")
                  time.sleep(2)

                  dirigejeux("debut", janken)

            elif choix_jeu == "pendu":
                  print("\nBienvenue sur le jeu du Pendu !!! Spécial Personnage d'Anime !!!!!!!!!!!!")
                  time.sleep(1)

                  print("\nLa règle est simple :")
                  print(" - Il faut trouver le nom/prénom du personnage qui se cache derrière les \033[33m_\033[0m !")
                  time.sleep(2)

                  dirigejeux("debut", pendu)

      elif reponse_jeu == "resumer" or reponse_jeu == "résumer" :
            print("                ╭────────────────────────────╮")
            print("                |   ╳     Scoreboard     ╳   |")
            print("                ├────────────────────────────┤")
            print("                | \033[33mLe Juste Prix\033[0m              |")
            print("                | Partie :\033[33m", record_minijeux["partieJustePrix"],"\033[0m                |")
            print("                |                            |")
            print("                | Victoire :\033[33m", record_minijeux["victoireJustePrix"],"\033[0m              |")
            print("                ├────────────────────────────┤")
            print("                | \033[32mLa Roulette\033[0m                |")
            print("                | Partie :\033[32m", record_minijeux["partieRoulette"],"\033[0m                |")
            print("                |                            |")
            print("                | Victoire Normal :\033[32m", record_minijeux["victoireRouletteNormal"],"\033[0m       |")
            print("                |                            |")
            print("                | Victoire Difficile :\033[32m", record_minijeux["victoireRouletteDifficile"],"\033[0m    |")
            print("                |                            |")
            print("                | Victoire Total :\033[32m", record_minijeux["victoireRouletteTotalDifficile"],"\033[0m        |")
            print("                ├────────────────────────────┤")
            print("                | \033[35mJanken\033[0m                     |")
            print("                | Partie :\033[35m", record_minijeux["partieJanken"],"\033[0m                |")
            print("                |                            |")
            print("                | Victoire :\033[35m", record_minijeux["victoireJanken"],"\033[0m              |")
            print("                ├────────────────────────────┤")
            print("                | \033[31mLe Pendu\033[0m                   |")
            print("                | Partie :\033[31m", record_minijeux["partiePendu"],"\033[0m                |")
            print("                |                            |")
            print("                | Victoire :\033[31m", record_minijeux["victoirePendu"],"\033[0m              |")
            print("                ╰────────────────────────────╯")
            time.sleep(2)
            minijeux()

      elif reponse_jeu == "sortir":
            fin()

def dirigejeux(moment, jeu, mode=""):
      if moment == "debut":
            print("\nEs-tu sûr de vouloir jouer ?\033[33m oui/non \033[0m")
      elif moment == "rejouer":
            print("\Veux-tu rejouer ?\033[33m oui/non \033[0m")
      choix = ""
      while not choix == "oui" and not choix == "non":
            choix = input("> ").lower()
      
      if choix == "oui":
            if mode == "":
                  jeu()
            else:
                  jeu(mode)
      elif choix == "non":
            minijeux()

def justeprix():
      record_minijeux["partieJustePrix"] += 1
      print("\nC'est ta", record_minijeux["partieJustePrix"], "partie(s).\n")
      time.sleep(2)

      print("\nPrêt ?!")
      time.sleep(2)
      print("C'est parti !!!!!\n")
      time.sleep(1)

      numero = int(random.randint(10,10000))
      numero_choix = 0
      tentative = 0

      while True:
            try:
                  numero_choix = int(input("Un nombre ? > "))
                  if numero_choix == 0:
                        quitter = ""
                        while not quitter == "oui" and not quitter == "non":
                              quitter = input("Es-tu sûr de vouloir quitter ?\033[33m oui/non \033[0m > ").lower()
                        if quitter == "oui":
                              print("Tu quittes ta partie de Juste Prix...")
                              minijeux()
                        elif quitter == "non":
                              print("")
                              pass
                  if numero_choix == numero:
                        print("\nBravo")
                        print("\033[32mTu as gagné !! Ce n'était pas facile, mais bravo !!!\n\033[0m")
                        record_minijeux["victoireJustePrix"] += 1
                        print("\nC'est ta", record_minijeux["victoireJustePrix"], "victoire !\n")
                        time.sleep(2)
                        dirigejeux("rejouer", justeprix)
                  elif numero_choix != numero and numero_choix != 0:
                        tentative += 1
                        print(f"Nombre de tentatives restantes : {50-tentative}\n")
                        if numero_choix >= numero:
                              print("C'est Moins !")
                        elif numero_choix <= numero:
                              print("C'est Plus !")
                  else:
                        pass
                  if tentative >= 50:
                        print(f"Dommage... Tu y étais presque, le numéro était : {numero}...\n")
                        dirigejeux("rejouer", justeprix)
            except ValueError:
                  print("Ce n'est pas un nombre...")

def laroulette(difficulte):
      couleur_list = ["Vert", "Rouge", "Rouge", "Rouge", "Rouge", "Rouge", "Rouge", "Noir", "Noir", "Noir", "Noir", "Noir", "Noir"]
      couleur_resultat = random.choice(couleur_list)
      roulette_couleur_choix = ""
      
      nombre_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
      nombre_resultat = random.choice(nombre_list)
      roulette_nombre_choix = ""

      record_minijeux["partieRoulette"] += 1
      print("\nC'est ta", record_minijeux["partieRoulette"], "partie(s).\n")

      while not roulette_couleur_choix == "vert" and not roulette_couleur_choix == "rouge" and not roulette_couleur_choix == "noir":
            roulette_couleur_choix = input("\nChoisis ta couleur : ").lower()

      if difficulte == "difficile":
            while True:
                  try:
                        roulette_nombre_choix = int(input("Choisis ton chiffre/nombre entre 1 et 36 : "))
                        if roulette_nombre_choix <= 0 or roulette_nombre_choix >= 36:
                              print("Choisis un chiffre/nombre entre 1 et 36...")
                        else:
                              break
                  except ValueError:
                        print("Un chiffre s'il te plaît...")

      time.sleep(2)
      print("\n...\n")
      time.sleep(2)

      if roulette_couleur_choix == couleur_resultat.lower():
            print(f"Bravo ! C'est bien la couleur {couleur_resultat} !\n")
            if roulette_couleur_choix == "vert":
                  print("\033[32mGG c'est rare de tomber sur le vert !\033[0m")
            elif roulette_couleur_choix == "rouge":
                  print("\033[31mBien joué !\033[0m")
            elif roulette_couleur_choix == "noir":
                  print("\033[30mBien joué !\033[0m")
            if difficulte == "normal":
                  record_minijeux["victoireRouletteNormal"] += 1
                  print("\nC'est ta", record_minijeux["victoireRouletteNormal"], "victoire, en mode normal !\n")
      else:
            print(f"Dommage... C'était la couleur {couleur_resultat}...")

      if difficulte == "difficile" and roulette_nombre_choix == nombre_resultat:
            print(f"\033[32m\nBravo ! C'est bien le chiffre/nombre {nombre_resultat} !\033[0m")
            if roulette_couleur_choix == couleur_resultat.lower() and roulette_nombre_choix == nombre_resultat:
                  record_minijeux["victoireRouletteTotalDifficile"] += 1
                  print("\nC'est ta", record_minijeux["victoireRouletteTotalDifficile"], "victoire, TOTAL !!!\n")
            else:
                  record_minijeux["victoireRouletteDifficile"] += 1
                  print("\nC'est ta", record_minijeux["victoireRouletteDifficile"], "victoire, en mode difficile !\n")
      elif  difficulte == "difficile" and roulette_nombre_choix != nombre_resultat:
            print(f"\nDommage... C'était le chiffre/nombre {nombre_resultat}...")
      time.sleep(2)

      dirigejeux("rejouer", laroulette, difficulte)

def janken():
      janken_list = ["pierre", "papier", "ciseaux"]
      janken_resultat = random.choice(janken_list)
      janken_choix = ""

      record_minijeux["partieJanken"] += 1
      print("\nC'est ta", record_minijeux["partieJanken"], "partie(s).\n")

      while not janken_choix in janken_list:
            janken_choix = input("\nQuel est ton choix ? > ").lower()
      time.sleep(2)
      print("\nJan\n")
      time.sleep(1)
      print("\nKen\n")
      time.sleep(1)
      print("\nPON !!!\n")

      if janken_choix == janken_resultat.lower():
            print(f"Humm... Vous avez tous les deux choisis : {janken_resultat} !")
      elif janken_choix == "pierre" and janken_resultat == "papier":
            print("\033[31mPerdu\033[0m")
      elif janken_choix == "pierre" and janken_resultat == "ciseaux":
            print("\033[32mBien joué !\033[0m")
            record_minijeux["victoireJanken"] += 1
      elif janken_choix == "papier" and janken_resultat == "pierre":
            print("\033[32mBien joué !\033[0m")
            record_minijeux["victoireJanken"] += 1
      elif janken_choix == "papier" and janken_resultat == "ciseaux":
            print("\033[31mPerdu\033[0m")
      elif janken_choix == "ciseaux" and janken_resultat == "pierre":
            print("\033[31mPerdu\033[0m")
      elif janken_choix == "ciseaux" and janken_resultat == "papier":
            print("\033[32mBien joué !\033[0m")
            record_minijeux["victoireJanken"] += 1

      print("\nEn total, tu as gagné", record_minijeux["victoireJanken"], "fois !\n")

      time.sleep(2)

      dirigejeux("rejouer", janken)

def pendu():
      pendu_list = ["ai-ohto", "bell-cranel", "chika-fujiwara", "dio-brando", "eren-yeager", 
      "felix-argyle", "gin-akutagawa", "hachiman-hikigaya", "izuku-midoriya", "jibril",
      "killua-zoldyck", "levi", "megumin", "nezuko-kamado", "osamu-dazai", "piccolo", 
      "quinella", "ristu-tainaka", "shalltear-bloodfallen", "touka-kirishima", "umaru-doma", 
      "violet-evergarden", "william-vangeance", "xerxes-break", "yuuji-itadori", "zero-two"]
      solution = str(random.choice(pendu_list))
      tentatives = 7
      resultat_pendu = ""
      lettres_pendu = "-"
      essaie = "> "
      proposition = ""
      lettre = "abcdefghijklmnopqrstuvwxyz"

      record_minijeux["partiePendu"] += 1
      print("\nC'est ta", record_minijeux["partiePendu"], "partie(s).\n")

      for l in solution:
            resultat_pendu = resultat_pendu + "_ "

      while tentatives > 0:
            print("\nLe personnage d'Anime : ", resultat_pendu)
            while True:
                  try:
                        proposition = input("Proposes une lettre : ")[0:1].lower()
                        time.sleep(1)
                        if not proposition in lettre:
                              print("Choisis une lettre...")
                        else:
                              break
                  except ValueError:
                        print("Ce n'est pas une lettre...")
            essaie += proposition + " / "

            if proposition in solution:
                  lettres_pendu = lettres_pendu + proposition
                  print("> C'est correct !\n")
            elif proposition == " ":
                  pass
            else:
                  tentatives -= 1
                  print("> C'est incorrect :/\n")
                  if tentatives==0:
                        print(" ╔╦════════╳══")
                        print(" ║║/       |  ")
                        print(" ║║        0  ")
                        print(" ║║       /|\ ")
                        print(" ║║        |  ")
                        print("/║║       / \ ")
                        print("═╩╩════════════\n")
                  elif tentatives<=1:
                        print(" ╔╦════════╳══")
                        print(" ║║/       |  ")
                        print(" ║║        0  ")
                        print(" ║║       /|\ ")
                        print(" ║║        |  ")
                        print("/║║           ")
                        print("═╩╩════════════\n")
                  elif tentatives<=2:
                        print(" ╔╦════════╳══")
                        print(" ║║/       |  ")
                        print(" ║║        0  ")
                        print(" ║║       /|\ ")
                        print(" ║║           ")
                        print("/║║           ")
                        print("═╩╩════════════\n")
                  elif tentatives<=3:
                        print(" ╔╦════════╳══")
                        print(" ║║/       |  ")
                        print(" ║║        0  ")
                        print(" ║║        |  ")
                        print(" ║║           ")
                        print("/║║           ")
                        print("═╩╩════════════\n")
                  elif tentatives<=4:
                        print(" ╔╦════════╳══")
                        print(" ║║/       |  ")
                        print(" ║║        0  ")
                        print(" ║║           ")
                        print(" ║║           ")
                        print("/║║           ")
                        print("═╩╩════════════\n")
                  elif tentatives<=5:
                        print(" ╔╦════════╳══")
                        print(" ║║/       |  ")
                        print(" ║║           ")
                        print(" ║║           ")
                        print(" ║║           ")
                        print("/║║           ")
                        print("═╩╩════════════\n")
                  elif tentatives<=6:
                        print(" ╔╦════════╳══")
                        print(" ║║/          ")
                        print(" ║║           ")
                        print(" ║║           ")
                        print(" ║║           ")
                        print("/║║           ")
                        print("═╩╩════════════\n")
            print(f"Tentatives restantes : {tentatives}")
            print(f"Lettres déjà essayées {essaie}")

            resultat_pendu = ""
            for x in solution:
                  if x in lettres_pendu:
                        resultat_pendu += x + " "
                  else:
                        resultat_pendu += "_ "
            
            if tentatives == 0:
                  print(f"\nDommage... C'était : {solution.upper()} !\n")
            if "_" not in resultat_pendu:
                  print(f"\nBravo ! C'est bel est bien : {solution.upper()} !\n")
                  record_minijeux["victoirePendu"] += 1
                  print("C'est ta", record_minijeux["victoirePendu"], "victoire !\n")
                  tentatives = 0
      dirigejeux("rejouer", pendu)
      time.sleep(2)

# ********************************************************************************
# Début et Fin
# ********************************************************************************

def fin():
      sys.exit("Tu quittes les mini-jeux.")

# Pour lancer le jeu, on appelle la fonction d'introduction
if __name__ == "__main__":
      minijeux()
