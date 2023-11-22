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
width = "970"
height = "870"
root = tk.Tk()
root.geometry(width + "x" + height)
root.minsize(int(width), int(height))
root.maxsize(int(width), int(height))
root.title("2848 Swerve Path Planner")
sv_ttk.use_dark_theme()



"Joystick instance"
"joystick1 = Joystick.XboxController()"
"root.after(20, updateJoystick)"

"Initialize all frames for main window"
borderwidth = 5
tFrame = ttk.Frame(root, relief='raised', borderwidth=borderwidth)
tFrame0 = ttk.Frame(tFrame)
tFrame1 = ttk.Frame(tFrame)
mFrame = ttk.Frame(root)
mFrame0 = ttk.Frame(mFrame, relief='groove', borderwidth=borderwidth)
mFrame1 = ttk.Frame(mFrame)
bFrame = ttk.Frame(root, relief='raised', borderwidth=borderwidth)
bFrame0 = ttk.Frame(bFrame)
bFrame1 = ttk.Frame(bFrame)

"pack main frames"
tFrame.pack()
mFrame.pack()
bFrame.pack()

"pack subframes"
tFrame0.pack(side='left')
tFrame1.pack(side='left')
mFrame0.pack(side='left')
mFrame1.pack(side='left')
bFrame0.pack(side='left')
bFrame1.pack(side='left')

"Create and pack field&robot image and canvas"
cSizeMultiplier = 7680 / 3720
cWidth = 375
cHeight = int(cWidth * cSizeMultiplier)
mFrame0.configure(width=cWidth, height=cHeight)
canvas = tk.Canvas(mFrame0, height=cHeight, width=cWidth)
canvas.pack(side='left', anchor='sw', expand=True, padx=200)


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
pickStart = ttk.Button(tFrame0, text="Pick Start", width=tbWidth)
pickEnd = ttk.Button(tFrame0, text="Pick End", width=tbWidth)
showPath = ttk.Button(tFrame0, text="Show Path", width=tbWidth)
enabledFlash = ttk.Button(tFrame1, text="Enable", width=tbWidth)

tbpadx = 37
tbpady = 0
pickStart.pack(side="left", padx=tbpadx, pady=tbpady)
pickEnd.pack(side="left", padx=tbpadx, pady=tbpady)
showPath.pack(side="left", padx=tbpadx, pady=tbpady)
enabledFlash.pack(anchor="e")

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

"Create and pack buttons for bFrame"
btn_destroy_wapoints = ttk.Button(bFrame0, text="Destroy Waypoints", width=tbWidth)
togglePieces = ttk.Button(bFrame0, text="Toggle Pieces", width=tbWidth)
timer = ttk.Label(bFrame1, text="Timer", width=tbWidth)

bbpadx = 107
bbpady = 0
btn_destroy_wapoints.pack(side='left', padx=bbpadx, pady=bbpady, fill='x')
togglePieces.pack(side='left', padx=bbpadx, pady=bbpady, fill='x')
timer.pack(pady=bbpady, fill='x')



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

menubar.add_cascade(label="Simulation", menu=simulationM)
simulationM.add_cascade(label="Set % error")
simulationM.add_cascade(label="Set PID")

"Display of menu bar in the app"
root.config(menu=menubar)
