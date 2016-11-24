import pygame
from adxl345 import ADXL345

pygame.init()
gameLoop = True

mainWindow = pygame.display.set_mode((1024,768))
pygame.display.set_caption("ADXL345: AirPaint")

fps = pygame.time.Clock()

adxl345 = ADXL345()
print "ADXL345 on address 0x%x:" % (adxl345.address)
'''
print "   x = %.3fG" % ( axes['x'] )
print "   y = %.3fG" % ( axes['y'] )
print "   z = %.3fG" % ( axes['z'] )
'''
multi = 20.0

lineList = []
while gameLoop:
    axes = adxl345.getAxes(True)
    mainWindow.fill((0,100,255))
    pygame.draw.line(mainWindow, WHITE, [axes['x']*multi, axes['y']*multi],[axes['x']*multi + 1, axes['y']*multi + 1],5);
    lineList.append([axes['x']*multi, axes['y']*multi])
    for i in range(len(lineList)-1):
        pygame.draw.line(mainWindow, WHITE, lineList[i], lineList[i+1],5);
    fps.tick(60)
    pygame.display.flip()

pygame.quit()
quit()
