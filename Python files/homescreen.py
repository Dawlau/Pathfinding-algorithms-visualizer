class HomeScreen:

    def __init__(self):
        self.HowToUse = None
        self.Start = None



    def render(self, screen):

        import constants, graphics, colors, pygame

        width, height = graphics.CMMS30.size("How to use")
        self.HowToUse = graphics.createText(
                                            screen, 
                                            graphics.CMMS30, 
                                            "How to Use", 
                                            colors.black, 
                                            (constants.width // 2 - width // 2, constants.height // 2 - height // 2)
                                           )


        width, height = graphics.CMMS30.size("Start")
        self.Start = graphics.createText(
                                         screen, 
                                         graphics.CMMS30,
                                         "Start",
                                         colors.black,
                                         (self.HowToUse.topleft[0] + width // 2, self.HowToUse.topleft[1] - height)
                                        )

        pygame.display.flip()




    def play(self, screen):

        import pygame, sys, tkinter, utilities
        from HowToUse import HowToUse
        

        self.render(screen)

        while True:

            for event in pygame.event.get():
                if event.type is pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]: # Quit
                    pygame.quit()
                    sys.exit()
                elif event.type is pygame.MOUSEBUTTONDOWN:

                    clickCoords = pygame.mouse.get_pos()
                    if utilities.inRect(self.Start, clickCoords):
                        return
                    elif utilities.inRect(self.HowToUse, clickCoords):
                        howtouse = HowToUse()