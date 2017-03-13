import cx_Freeze

executables = [cx_Freeze.Executable("Deeper.py")]

cx_Freeze.setup(
    name = "Deeper",
    options = {"build_exe":{"packages":["pygame", "pickle"], "include_files":["1001fonts-pix-pixelfjverdana12pt-eula.txt", "Pickaxe.png", "toolbar.dat", "background.png", "bricks.png", "clay.png", "CheckboxChecked.png", "coalore.png", "DeeperIcon.jpg", "DeeperIcon.ico", "dirt.png", "goldore.png", "grass.png", "ironore.png", "lamp.png", "LICENSE.txt", "mouse.png", "mud.png", "Player.png", "PlayerSkin.png", "stone.png", "ToolbarTile.png", "PixelFJVerdana12pt.TTF", "legacypc.png", "craftshelf.png", "DownButton.png", "UpButton.png", "ShutdownButton.png", "UpButton.png", "NoneBlock.png", "EraseButton.png", "HomeButton.png", "Options.png", "BuildX.png", "ShutdownButton2.png", "world1.deep"]}},
    description = "Deeper - v0.2.1.5 Alpha",
    version = "0.2.1.5",
    executables = executables
)




































