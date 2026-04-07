#leanring ot code s ins njicer:P 
import time
import pygame
pygame.mixer.init()
def lyrics_generation():
    
    music = ["1) nbhd", "2) cas", "3)men at work"]
    print(music)
    user_choice = input('enter from the baove music 👆 ?').strip().lower()
    if user_choice=="1":
        print("oaky so you have slected hte list 1 👇")
        #nbdh song list 
        nbhd_song = ["softcore","reflections", "prey"]
        for i in nbhd_song:
            time.sleep(1)
            print(i)
        user_song_choice = input("enter song name? love ").strip().lower()
        if user_song_choice in nbhd_song[0]:
            print("you have selected softcore")
            pygame.mixer.music.load('softcore.mp3') 
            pygame.mixer.music.play(-1, 0.0) # Replace with the path to your music file

            #lyrics
            user_love_lyrics = input("want me to add lyrics? 'yes' or 'no' ").strip().lower()
            if user_love_lyrics=="yes":
                print("here are the 👇 lyrics")
                #list of lyrics
                softcore = """
                Are we too young for this?
                Feels like I can't move
                """
                #text simulate using pht
                speed = 3
                #iterate the loop or text
                for iterate in softcore:
                    print(iterate, end="", flush=True)
                    time.sleep(speed)

        if user_song_choice in nbhd_song[1]:
            print("okay so oyu have select the reflections")
            print("do you want to me to generate lyrics for it ")
            pygame.mixer.music.stop()
            pygame.mixer.music.load('softcore.mp3') 
            pygame.mixer.music.play(-1, 0.0)
            #user lyrics
            user_lyrics = input("enter want or yes or no? ").strip().lower()
            if user_lyrics=="yes":
                print("okay generating lyrics..")
                
                reflection_lyrics = """you've been my muse for a long time
                you get me through every dark night
                i am always gone,out on the go
                i'm on the run you go home alone """
                
                #determien the speed of the song 
                speed = 0.1
                for char in reflection_lyrics:
                    print(char, end="", flush=True)
                    time.sleep(speed)
                
            
        if user_song_choice in nbhd_song[2]:
            print("okay you have select prey")
            print("do you want to generate lyrics 👇 below ")
            #userlyrics
            user_okay_lyrics = input("Enter 'yes' or 'no' ?")
            if user_okay_lyrics=="yes":
                print("generate lyrics fro prey ")
                prey_lyrics = """
                something is worng i can't explain
                everything change when the bird game
                heaven no i you know what i mean, don't you 
                prey..prey.prey..prey......
                """
                #looop trhough to simulate teh text
                speed = 0.1
                for text_simulate in prey_lyrics:
                    print(text_simulate, end="", flush=True)
                    time.sleep(speed)

    elif user_choice=="2":
        print("you have select CAS ")
        print("i think 'gonzalez' is your favourite!")
        def generating_their_Song():
            speed =0.1
            songs_cas = """
                        1)sweet
                        2)apacolypse
                        3)k"""
            #iterating 
            for iteratee in songs_cas:
                print(iteratee, end="", flush=True)
                time.sleep(speed)
            # user_cas_selecti
        generating_their_Song()
    elif user_choice=="3":
        print("you have select down under but i have select 'dragosta din tie fr you'") 
        
        user_lyrics_choice = input("want to generate lyriscs type 'yes' or 'no").lower().strip()
        # pygame.mixer.music.load('C:\Users\ADMIN\newpyfolder\ozone.mp3') 
        pygame.mixer.music.play(-1, 0.0)
        if user_lyrics_choice=="yes":
            speed_lyric = 2
            print("generating lyrics...")
            lyrics_dragosta_ten = '''
              alors, cet yai o picasso....'''
            #text simulation f
            for simulate in lyrics_dragosta_ten:
                print(simulate, end="", flush=True)

        pygame.mixer.music.stop()
lyrics_generation()
