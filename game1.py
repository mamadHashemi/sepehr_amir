import pygame
import sys
import random
import time
pygame.init()
v=pygame.display.set_mode((1000,600))
pygame.time.Clock().tick(1)
run=True
h=True
z=25
t=0
s=0.5
xr=200          
yr=350        
xe=1000       
ye=random.randint(0,350)        
#pygame.mixer.music.load("C:\Users\karino\Downloads\Happy_Background Music_Happy_Mood.mp3")
#pygame.mixer.music.play()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            run=False
            pygame.quit()
            sys.exit
        if event.type==pygame.KEYDOWN:
           if event.key==pygame.K_UP:
                 yr-=50
           elif event.key==pygame.K_DOWN:
                yr+=25  
           elif event.key==pygame.K_RIGHT:
                h=False
       #         pygame.mixer.music.set_volume(0.2)
           elif event.key==pygame.K_LEFT:
                h=True 
        #        pygame.mixer.music.set_volume(1)
           elif event.key==pygame.K_ESCAPE:  
                run=False
                pygame.quit()
                sys.exit 
           elif event.key==pygame.K_r:
                h=True
                t=0    
                xe=1000    
                ye=random.randint(0,350) 
      #          pygame.mixer.music.load("C:\Users\karino\Downloads\Happy_Background Music_Happy_Mood.mp3")
     #           pygame.mixer.music.play()
                xr=200          
                yr=350        
    #       elif event.key==pygame.K_m:
   #             pygame.mixer.music.pause() 
           #elif event.key==pygame.K_p:
               # pygame.mixer.music.load("C:\Users\karino\Downloads\Happy_Background Music_Happy_Mood.mp3")
  #              pygame.mixer.music.play()                     
    if t>z:
        z+=25
    if  t==z:
        s+=0.0002
    if h:
      v.fill("#010099")        
      pygame.draw.rect(v,"yellow",((xr,yr),(50,50)))
      yr+=0.1
      pygame.draw.rect(v,"red",((xe,ye),(50,250)))
      xe-=s
      if ((xr<=xe<=xr+50) and ((ye<=yr<=ye+250)or(ye<=yr+50<=ye+250)))or(yr>=550):
          h=False 
          f=pygame.font.SysFont(None,80)
          im=f.render(f"Score:{t}",True,"#009900")
          v.blit(im,(400,300))
          #pygame.mixer.music.pause()
          #pygame.display.update()
          h=False
          #pygame.mixer.music.load("G:\Game-Over-Sound-Effect-4.mp3")
          #pygame.mixer.music.play()
      elif (xr>xe):
          xe=1000    
          ye=random.randint(0,350)
          t+=1
      pygame.display.update()