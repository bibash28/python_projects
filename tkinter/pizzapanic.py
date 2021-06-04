#import game module from livewire packages
from livewires import games

#initialize graphic screen
games.init(screen_width=640, screen_height=480, fps=50)


games.screen.mainloop()
