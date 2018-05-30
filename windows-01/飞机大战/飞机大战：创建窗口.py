import pygame
import time
"""
搭建界面，完成窗口和背景图
"""
def main():
    #1.创建窗口
    screen = pygame.display.set_mode((480,852),0,32)
    #2.创建一个背景图片
    background = pygame.image.load(r"D:\seafile-backup\untitled1\飞机大战\feiji\background.png")
    while True:
        screen.blit(background,(0,0))
        pygame.display.update()
        time.sleep(0.01)
if __name__ == "__main__":
    main()