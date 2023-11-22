import OccupancyGrid
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import sv_ttk
from PIL import ImageTk, Image
import GenerateOGfromImage
import Joystick

"Opens current Occupancy Grid"
OCG = OccupancyGrid.OccupancyGrid("Occupancy Grids/Occupancy Grid3.txt")
OCGarr = np.array(OCG.getOGGrid())

"Tkinter window size and formatting"
width = "570"
height = "835"
root = tk.Tk()
root.geometry(width + "x" + height)
root.minsize(int(width), int(height))
root.maxsize(int(width), int(height))
root.title("2848 Swerve Simulation")
sv_ttk.use_dark_theme()

"Joystick instance"
"joystick1 = Joystick.XboxController()"
"root.after(20, updateJoystick)"

"Initialize all frames for main window"
borderwidth = 5
tFrame = ttk.Frame(root, relief='raised', borderwidth=borderwidth, width=570)
mFrame = ttk.Frame(root)
mFrame0 = ttk.Frame(mFrame, relief='groove', borderwidth=borderwidth)
mFrame1 = ttk.Frame(mFrame, height=744, width=165)

"pack main frames"
tFrame.pack()
mFrame.pack()

"pack subframes"
mFrame0.pack(side='left')
mFrame1.pack(side='left')

"Create and pack field&robot image and canvas"
cSizeMultiplier = 7680 / 3720
cWidth = 375
cHeight = int(cWidth * cSizeMultiplier)
mFrame0.configure(width=cWidth, height=cHeight)
canvas = tk.Canvas(mFrame0, height=cHeight, width=cWidth)
canvas.pack(side='left', anchor='sw')

fieldImage = Image.open("Images/Field Image5.png")
fieldImage = fieldImage.resize((cHeight, cWidth))
fieldImage = fieldImage.rotate(90, expand=True)
img = ImageTk.PhotoImage(fieldImage)
canvas.create_image(0, cHeight / 2, anchor="w", image=img)

robotImage = Image.open("Images/RobotImageBlue.png")
robotImage = robotImage.resize((40, 40))
tkrobotImage = ImageTk.PhotoImage(robotImage)
crobotImage = canvas.create_image(cWidth / 2, cHeight / 2, image=tkrobotImage)

robotx = cWidth / 2
roboty = -1 * cHeight / 2
robotw = 0  # in degrees

"Create and pack buttons for tFrame"
tbWidth = 20
enabledFlash = ttk.Button(tFrame, text="Enable", width=570)
enabledFlash.pack()

"Create and pack canvases for joystick graphs"
jcsize = 165
jcanvas0 = tk.Canvas(mFrame1, width=jcsize, height=jcsize)
jcanvas1 = tk.Canvas(mFrame1, width=jcsize, height=jcsize)
jcanvas0lbl = ttk.Label(mFrame1, text="Left Joystick")
jcanvas1lbl = ttk.Label(mFrame1, text="Right Joystick")

jpadx = 5
jpady = 10
jcanvas0lbl.pack(side='top', anchor="center", pady=jpady, padx=jpadx)
jcanvas0.pack(side='top', anchor="w", pady=jpady, padx=jpadx)
jcanvas1.pack(side='top', anchor="w", pady=jpady, padx=jpadx)
jcanvas1lbl.pack(side='top', anchor="center", pady=jpady, padx=jpadx)

"Draw axes on Joystick Canvases"
jcanvas0.create_oval(0, 0, jcsize, jcsize, fill="white")
jcanvas1.create_oval(0, 0, jcsize, jcsize, fill="white")

jcanvas0.create_line(jcsize / 2, 0, jcsize / 2, jcsize, dash=(4, 2))
jcanvas0.create_line(0, jcsize / 2, jcsize, jcsize / 2, dash=(4, 2))
jcanvas1.create_line(jcsize / 2, 0, jcsize / 2, jcsize, dash=(4, 2))
jcanvas1.create_line(0, jcsize / 2, jcsize, jcsize / 2, dash=(4, 2))

"Adding joystick images to Joystick Canvases"
jimgsize = 40

joystickImagge = Image.open("Images/Thumbstick.png")
joystickImagge = joystickImagge.resize((jimgsize, jimgsize))
jimgpng = ImageTk.PhotoImage(joystickImagge)
jimg0 = jcanvas0.create_image(jcsize / 2, jcsize / 2, image=jimgpng)
jimg1 = jcanvas1.create_image(jcsize / 2, jcsize / 2, image=jimgpng)

timer = ttk.Label(mFrame1, text="Timer: ", width=tbWidth)
timer.pack(anchor='sw')

"Creating Menubar"
menubar = tk.Menu()
fieldM = tk.Menu(menubar, tearoff=False)
robotM = tk.Menu(menubar, tearoff=False)
driveM = tk.Menu(menubar, tearoff=False)
physicalSettingsM = tk.Menu(menubar, tearoff=False)
kinematicsM = tk.Menu(menubar, tearoff=False)
dimensionsM = tk.Menu(menubar, tearoff=False)
simulationM = tk.Menu(menubar, tearoff=False)

menubar.add_cascade(label='Field', menu=fieldM)
fieldM.add_cascade(label="Update Field Image")
fieldM.add_cascade(label="Update Occupancy Grid")
fieldM.add_cascade(label="Display Occupancy Grid")
fieldM.add_cascade(label="Set Default")

menubar.add_cascade(label='Robot', menu=robotM)
robotM.add_cascade(label="Drive", menu=driveM)
driveM.add_cascade(label="Tank")
driveM.add_cascade(label="Swerve")
robotM.add_cascade(label="Physical Settings", menu=physicalSettingsM)
physicalSettingsM.add_cascade(label="Kinematics", menu=kinematicsM)
physicalSettingsM.add_cascade(label="Dimensions", menu=dimensionsM)
kinematicsM.add_cascade(label="MAX Velocity")
kinematicsM.add_cascade(label="MAX Acceleration")
kinematicsM.add_cascade(label="MAX Jerk")
dimensionsM.add_cascade(label="Edit Width")
dimensionsM.add_cascade(label="Edit Length")

"Display of menu bar in the app"
root.config(menu=menubar)

"loop main window"
root.mainloop()
