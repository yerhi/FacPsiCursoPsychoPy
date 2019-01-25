# The thing to be change in UNS40 for TMS is the ITI time in the xls file  1.5  and in script (take this one)// the file for example trial line 74 and 80
#vhVH (*)  // pa prt: introduce code to create prt folder at the beginning, before starting trials create the lists, then at the end of trials the conditions of prt and list filling, before break the proper creation of prt 
#!/usr/bin /env pythonf //  possible to erase the first 4 lists after test period
# -*- coding: utf-8 -*-// lines 67 and 82 for examples // make sure of using right excel file (right answer = left or right -according to keyboard and not button box-)

"""
This experiment was created using PsychoPy2 Experiment Builder (v1.80.06), augustus 13, 2014, at 18:36
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Store info about the experiment session
expName = 'NAP'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup filename for saving
filename = 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# Setup folders and files for saving

if not os.path.isdir('prts'):
    os.makedirs('prts')  # if this fails (e.g. permissions) we will get error

prtFile = 'prts/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Example"
ExampleClock = core.Clock()
Instructions = visual.TextStim(win=win, ori=0, name='Instructions',
    text=u'You will now see two images at the same time. \n\nPlease only attend to the image that is surrounded by a black frame. Your objective is to quickly categorize the image. If the image has sexual content, press the left key. If the image contains sports, dancers or objects (thus NON sexual content), press the right key.\n\nPlease press the spacebar to continue.',    font=u'Arial',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial" C:\Users\Geraldine.Rodriguez\Documents\SEX.DEWITTE\NAP SEKS
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
ExampleZwart = visual.ImageStim(win=win, name='ExampleZwart',units=u'pix', 
    image=u'C:\\Users\\Geraldine.rodriguez\\Documents\\SEX.DEWITTE\\NAP SEKS\\examplezwart.jpg', mask=None,
    ori=0, pos=[0,-165], size=[326, 266],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-1.0)
ExampleGrijs = visual.ImageStim(win=win, name='ExampleGrijs',units=u'pix', 
    image=u'C:\\Users\\Geraldine.rodriguez\\Documents\\SEX.DEWITTE\\NAP SEKS\\examplegrijs.jpg', mask=None,
    ori=0, pos=[0, 175], size=[326, 266],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-2.0)
ExampleText1 = visual.TextStim(win=win, ori=0, name='ExampleText1',
    text=u'EXAMPLE',    font=u'Arial',
    units=u'norm', pos=[0, .7], height=0.09, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-3.0)
textexample = visual.TextStim(win=win, ori=0, name='textexample',
    text=u'In this case you would have to press the right key, since the black frame picture doesn\u2019t have sexual content.',    font=u'Arial',
    units=u'norm', pos=[0,-.7], height=0.075, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-4.0)

# Initialize components for Routine "ToStart"
ToStartClock = core.Clock()
TextToStart = visual.TextStim(win=win, ori=0, name='TextToStart',
    text=u'\nThus, please remember: \n\nSexual content -> left \nNon sexual content -> right\n\nTry to do this as fast and accurate as possible. \n\nPlease press the spacebar when you are ready to start. ',    font=u'Arial',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "Trial"
TrialClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
PreTrialImageI = visual.ImageStim(win=win, name='PreTrialImageI',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[326,266],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-1.0)
PreTrialImageII = visual.ImageStim(win=win, name='PreTrialImageII',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[326, 266],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-2.0)
Fixation2 = visual.TextStim(win=win, ori=0, name='Fixation2',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
PosTrialImageI = visual.ImageStim(win=win, name='PosTrialImageI',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[326, 266],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-5.0)
PosTrialImageII = visual.ImageStim(win=win, name='PosTrialImageII',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[326, 266],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-6.0)

# Initialize components for Routine "break_2"
BreakClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text=u'       BREAK',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text=u'Please press any button when you are ready to continue ',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-1.0)



# Initialize components for Routine "Trial2"
Trial2Clock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
PreTrialImageI = visual.ImageStim(win=win, name='PreTrialImageI',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[326,266],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-1.0)
PreTrialImageII = visual.ImageStim(win=win, name='PreTrialImageII',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[326, 266],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-2.0)
Fixation2 = visual.TextStim(win=win, ori=0, name='Fixation2',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
PosTrialImageI = visual.ImageStim(win=win, name='PosTrialImageI',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[326, 266],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-5.0)
PosTrialImageII = visual.ImageStim(win=win, name='PosTrialImageII',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[326, 266],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-6.0)


# Initialize components for Routine "break_2"
BreakClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text=u'       BREAK',    font=u'Arial',
    pos=[0, 0], height=0.09, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text=u'            BREAK \n\nPlease press any key when you are ready to continue. ',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-1.0)




# Initialize components for Routine "Trial3"
Trial3Clock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
PreTrialImageI = visual.ImageStim(win=win, name='PreTrialImageI',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[326,266],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-1.0)
PreTrialImageII = visual.ImageStim(win=win, name='PreTrialImageII',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[326, 266],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-2.0)
Fixation2 = visual.TextStim(win=win, ori=0, name='Fixation2',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
PosTrialImageI = visual.ImageStim(win=win, name='PosTrialImageI',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[326, 266],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-5.0)
PosTrialImageII = visual.ImageStim(win=win, name='PosTrialImageII',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[326, 266],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-6.0)


# Initialize components for Routine "thank_you"
thank_youClock = core.Clock()
Thanks = visual.TextStim(win=win, ori=0, name='Thanks',
    text='Thank you!',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 



##------Prepare to start Routine "Example"-------
t = 0
ExampleClock.reset()  # clock 
frameN = -1
routineTimer.add(60.000000)
# update component parameters for each repeat
Resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
Resp.status = NOT_STARTED
# keep track of which components have finished
ExampleComponents = []
ExampleComponents.append(Instructions)
ExampleComponents.append(Resp)
for thisComponent in ExampleComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Example"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ExampleClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions* updates
    if t >= 0.0 and Instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instructions.tStart = t  # underestimates by a little under one frame
        Instructions.frameNStart = frameN  # exact frame index
        Instructions.setAutoDraw(True)
    elif Instructions.status == STARTED and t >= (0.0 + (60-win.monitorFramePeriod*0.75)): #most of one frame period left
        Instructions.setAutoDraw(False)
    
    # *Resp* updates
    if t >= 0 and Resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        Resp.tStart = t  # underestimates by a little under one frame
        Resp.frameNStart = frameN  # exact frame index
        Resp.status = STARTED
        # keyboard checking is just starting
        Resp.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    elif Resp.status == STARTED and t >= (0 + (60-win.monitorFramePeriod*0.75)): #most of one frame period left
        Resp.status = STOPPED
    if Resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            Resp.keys = theseKeys[-1]  # just the last key pressed
            Resp.rt = Resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ExampleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Example"-------
for thisComponent in ExampleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Resp.keys in ['', [], None]:  # No response was made
   Resp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('Resp.keys',Resp.keys)
if Resp.keys != None:  # we had a response
    thisExp.addData('Resp.rt', Resp.rt)
thisExp.nextEntry()

#------Prepare to start Routine "trial"-------
t = 0
trialClock.reset()  # clock 
frameN = -1
routineTimer.add(15.000000)
# update component parameters for each repeat
RespExample = event.BuilderKeyResponse()  # create an object of type KeyResponse
RespExample.status = NOT_STARTED
# keep track of which components have finished
trialComponents = []
trialComponents.append(ISI)
trialComponents.append(ExampleZwart)
trialComponents.append(ExampleGrijs)
trialComponents.append(ExampleText1)
trialComponents.append(textexample)
trialComponents.append(RespExample)
for thisComponent in trialComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "trial"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ExampleZwart* updates
    if t >= 0.0 and ExampleZwart.status == NOT_STARTED:
        # keep track of start time/frame for later
        ExampleZwart.tStart = t  # underestimates by a little under one frame
        ExampleZwart.frameNStart = frameN  # exact frame index
        ExampleZwart.setAutoDraw(True)
    elif ExampleZwart.status == STARTED and t >= (0.0 + (15.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        ExampleZwart.setAutoDraw(False)
    
    # *ExampleGrijs* updates
    if t >= 0.0 and ExampleGrijs.status == NOT_STARTED:
        # keep track of start time/frame for later
        ExampleGrijs.tStart = t  # underestimates by a little under one frame
        ExampleGrijs.frameNStart = frameN  # exact frame index
        ExampleGrijs.setAutoDraw(True)
    elif ExampleGrijs.status == STARTED and t >= (0.0 + (15.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        ExampleGrijs.setAutoDraw(False)
    
    # *ExampleText1* updates
    if t >= 0.0 and ExampleText1.status == NOT_STARTED:
        # keep track of start time/frame for later
        ExampleText1.tStart = t  # underestimates by a little under one frame
        ExampleText1.frameNStart = frameN  # exact frame index
        ExampleText1.setAutoDraw(True)
    elif ExampleText1.status == STARTED and t >= (0.0 + (15-win.monitorFramePeriod*0.75)): #most of one frame period left
        ExampleText1.setAutoDraw(False)
    
    # *textexample* updates
    if t >= 0.0 and textexample.status == NOT_STARTED:
        # keep track of start time/frame for later
        textexample.tStart = t  # underestimates by a little under one frame
        textexample.frameNStart = frameN  # exact frame index
        textexample.setAutoDraw(True)
    elif textexample.status == STARTED and t >= (0.0 + (15-win.monitorFramePeriod*0.75)): #most of one frame period left
        textexample.setAutoDraw(False)
    
    # *RespExample* updates
    if t >= 0.0 and RespExample.status == NOT_STARTED:
        # keep track of start time/frame for later
        RespExample.tStart = t  # underestimates by a little under one frame
        RespExample.frameNStart = frameN  # exact frame index
        RespExample.status = STARTED
        # keyboard checking is just starting
        RespExample.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    elif RespExample.status == STARTED and t >= (0.0 + (15-win.monitorFramePeriod*0.75)): #most of one frame period left
        RespExample.status = STOPPED
    if RespExample.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            RespExample.keys = theseKeys[-1]  # just the last key pressed
            RespExample.rt = RespExample.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    # *ISI* period
    if t >= 0.0 and ISI.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI.tStart = t  # underestimates by a little under one frame
        ISI.frameNStart = frameN  # exact frame index
        ISI.start(0.5)
    elif ISI.status == STARTED: #one frame should pass before updating params and completing
        ISI.complete() #finish the static period
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if RespExample.keys in ['', [], None]:  # No response was made
   RespExample.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('RespExample.keys',RespExample.keys)
if RespExample.keys != None:  # we had a response
    thisExp.addData('RespExample.rt', RespExample.rt)
thisExp.nextEntry()






#------Prepare to start Routine "ToStart"-------
t = 0
ToStartClock.reset()  # clock 
frameN = -1
routineTimer.add(10.000000)
# update component parameters for each repeat
Resptostart = event.BuilderKeyResponse()  # create an object of type KeyResponse
Resptostart.status = NOT_STARTED
# keep track of which components have finished
ToStartComponents = []
ToStartComponents.append(TextToStart)
ToStartComponents.append(Resptostart)
for thisComponent in ToStartComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "ToStart"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ToStartClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TextToStart* updates
    if t >= 0.0 and TextToStart.status == NOT_STARTED:
        # keep track of start time/frame for later
        TextToStart.tStart = t  # underestimates by a little under one frame
        TextToStart.frameNStart = frameN  # exact frame index
        TextToStart.setAutoDraw(True)
    elif TextToStart.status == STARTED and t >= (0.0 + (10.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        TextToStart.setAutoDraw(False)
    
    # *Resptostart* updates
    if t >= 0 and Resptostart.status == NOT_STARTED:
        # keep track of start time/frame for later
        Resptostart.tStart = t  # underestimates by a little under one frame
        Resptostart.frameNStart = frameN  # exact frame index
        Resptostart.status = STARTED
        # keyboard checking is just starting
        Resptostart.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    elif Resptostart.status == STARTED and t >= (0 + (10-win.monitorFramePeriod*0.75)): #most of one frame period left
        Resptostart.status = STOPPED
    if Resptostart.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            Resptostart.keys = theseKeys[-1]  # just the last key pressed
            Resptostart.rt = Resptostart.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ToStartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "ToStart"-------
for thisComponent in ToStartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.nextEntry()




SexP=[]
DanceP=[]
SexNoP=[]
DanceNoP=[]
SexPerrors=[]
DancePerrors=[]
SexNoPerrors=[]
DanceNoPerrors=[]
SexPmisses=[]
DancePmisses=[]
SexNoPmisses=[]
DanceNoPmisses=[]
NAP1misses=[]
NAP1errors=[]
SexP_RT=[]
DanceP_RT=[]
SexNoP_RT=[]
DanceNoP_RT=[]

# set up handler to look after randomisation of conditions etc
TRIALS = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('NAP.xlsx'),
    seed=None, name='TRIALS')
thisExp.addLoop(TRIALS)  # add the loop to the experiment
thisTRIALS = TRIALS.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTRIALS.rgb)
if thisTRIALS != None:
    for paramName in thisTRIALS.keys():
        exec(paramName + '= thisTRIALS.' + paramName)

for thisTRIALS in TRIALS:
    currentLoop = TRIALS
    # abbreviate parameter names if possible (e.g. rgb = thisTRIALS.rgb)
    if thisTRIALS != None:
        for paramName in thisTRIALS.keys():
            exec(paramName + '= thisTRIALS.' + paramName)
    
    #------Prepare to start Routine "Trial"-------
    t = 0
    TrialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    PreTrialImageI.setPos(PositionI)
    PreTrialImageI.setImage(TargetI)
    PreTrialImageII.setPos(PositionII)
    PreTrialImageII.setImage(DistractorI)
    KeyRespI = event.BuilderKeyResponse()  # create an object of type KeyResponse
    KeyRespI.status = NOT_STARTED
    PosTrialImageI.setPos(PositionIII)
    PosTrialImageI.setImage(TargetII)
    PosTrialImageII.setPos(PositionIV)
    PosTrialImageII.setImage(DistractorII)
    KeyRespII = event.BuilderKeyResponse()  # create an object of type KeyResponse
    KeyRespII.status = NOT_STARTED
    # keep track of which components have finished
    TrialComponents = []
    TrialComponents.append(text)
    TrialComponents.append(PreTrialImageI)
    TrialComponents.append(PreTrialImageII)
    TrialComponents.append(KeyRespI)
    TrialComponents.append(Fixation2)
    TrialComponents.append(PosTrialImageI)
    TrialComponents.append(PosTrialImageII)
    TrialComponents.append(KeyRespII)
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t  # underestimates by a little under one frame
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        elif text.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text.setAutoDraw(False)
        
        # *PreTrialImageI* updates
        if t >= 1.75 and PreTrialImageI.status == NOT_STARTED:
            # keep track of start time/frame for later
            PreTrialImageI.tStart = t  # underestimates by a little under one frame
            PreTrialImageI.frameNStart = frameN  # exact frame index
            PreTrialImageI.setAutoDraw(True)
        elif PreTrialImageI.status == STARTED and t >= (1.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            PreTrialImageI.setAutoDraw(False)
        
        # *PreTrialImageII* updates
        if t >= 1.75 and PreTrialImageII.status == NOT_STARTED:
            # keep track of start time/frame for later
            PreTrialImageII.tStart = t  # underestimates by a little under one frame
            PreTrialImageII.frameNStart = frameN  # exact frame index
            PreTrialImageII.setAutoDraw(True)
        elif PreTrialImageII.status == STARTED and t >= (1.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            PreTrialImageII.setAutoDraw(False)
        
        # *KeyRespI* updates
        if t >= 1.75 and KeyRespI.status == NOT_STARTED:
            # keep track of start time/frame for later
            KeyRespI.tStart = t  # underestimates by a little under one frame
            KeyRespI.frameNStart = frameN  # exact frame index
            KeyRespI.status = STARTED
            # keyboard checking is just starting
            KeyRespI.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif KeyRespI.status == STARTED and t >= (1.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            KeyRespI.status = STOPPED
        if KeyRespI.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                KeyRespI.keys = theseKeys[-1]  # just the last key pressed
                KeyRespI.rt = KeyRespI.clock.getTime()
                # was this 'correct'?
                if (KeyRespI.keys == str(RightAnswerI)) or (KeyRespI.keys == RightAnswerI):
                    KeyRespI.corr = 1
                else:
                    KeyRespI.corr = 2
                # a response ends the routine
                continueRoutine = True
        
        # *Fixation2* updates
        if t >= 3.5 and Fixation2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Fixation2.tStart = t  # underestimates by a little under one frame
            Fixation2.frameNStart = frameN  # exact frame index
            Fixation2.setAutoDraw(True)
        elif Fixation2.status == STARTED and t >= (3 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            Fixation2.setAutoDraw(False)
        
        # *PosTrialImageI* updates
        if t >= 5.25 and PosTrialImageI.status == NOT_STARTED:
            # keep track of start time/frame for later
            PosTrialImageI.tStart = t  # underestimates by a little under one frame
            PosTrialImageI.frameNStart = frameN  # exact frame index
            PosTrialImageI.setAutoDraw(True)
        elif PosTrialImageI.status == STARTED and t >= (4.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            PosTrialImageI.setAutoDraw(False)
        
        # *PosTrialImageII* updates
        if t >= 5.25 and PosTrialImageII.status == NOT_STARTED:
            # keep track of start time/frame for later
            PosTrialImageII.tStart = t  # underestimates by a little under one frame
            PosTrialImageII.frameNStart = frameN  # exact frame index
            PosTrialImageII.setAutoDraw(True)
        elif PosTrialImageII.status == STARTED and t >= (4.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            PosTrialImageII.setAutoDraw(False)
        
        # *KeyRespII* updates
        if t >= 5.25 and KeyRespII.status == NOT_STARTED:
            # keep track of start time/frame for later
            KeyRespII.tStart = t  # underestimates by a little under one frame
            KeyRespII.frameNStart = frameN  # exact frame index
            KeyRespII.status = STARTED
            # keyboard checking is just starting
            KeyRespII.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif KeyRespII.status == STARTED and t >= (4.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            KeyRespII.status = STOPPED
        if KeyRespII.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                KeyRespII.keys = theseKeys[-1]  # just the last key pressed
                KeyRespII.rt = KeyRespII.clock.getTime()
                # was this 'correct'?
                if (KeyRespII.keys == str(RightAnswerII)) or (KeyRespII.keys == RightAnswerII):
                    KeyRespII.corr = 1
                else:
                    KeyRespII.corr = 2
                # a response ends the routine
                continueRoutine = True
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Trial"-------
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
        
    # check responses
    if KeyRespI.keys in ['', [], None]:  # No response was made
       KeyRespI.keys=None
       # was no response the correct answer?!
       if str(RightAnswerI).lower() == 'none': KeyRespI.corr = 1  # correct non-response
       else: KeyRespI.corr = 0  # failed to respond (incorrectly)
    # store data for TRIALS (TrialHandler)
    TRIALS.addData('KeyRespI.keys',KeyRespI.keys)
    TRIALS.addData('KeyRespI.corr', KeyRespI.corr)
    if KeyRespI.keys != None:  # we had a response
        TRIALS.addData('KeyRespI.rt', KeyRespI.rt)
    # check responses
    if KeyRespII.keys in ['', [], None]:  # No response was made
       KeyRespII.keys=None
       # was no response the correct answer?!
       if str(RightAnswerII).lower() == 'none': KeyRespII.corr = 1  # correct non-response
       else: KeyRespII.corr = 0  # failed to respond (incorrectly)
    # store data for TRIALS (TrialHandler)
    TRIALS.addData('KeyRespII.keys',KeyRespII.keys)
    TRIALS.addData('KeyRespII.corr', KeyRespII.corr)
    if KeyRespII.keys != None:  # we had a response
        TRIALS.addData('KeyRespII.rt', KeyRespII.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'TRIALS'

    # store data for .prt
    if TrialType == 1 and KeyRespII.corr==1:
     SexP.append(1)
     SexP_RT.append(KeyRespII.rt)
    if TrialType == 2 and KeyRespII.corr==1:
     DanceP.append(1)
     DanceP_RT.append(KeyRespII.rt) 
    if TrialType == 3 and KeyRespII.corr==1:
     SexNoP.append(1)
     SexNoP_RT.append(KeyRespII.rt) 
    if TrialType == 4 and KeyRespII.corr==1:
     DanceNoP.append(1)
     DanceNoP_RT.append(KeyRespII.rt) 


    if TrialType == 1 and KeyRespII.corr==2:
     SexPerrors.append(1)
    if TrialType == 1 and KeyRespII.corr==0:
     SexPmisses.append(1)

    if TrialType == 2 and KeyRespII.corr==2:
     DancePerrors.append(1)
    if TrialType == 2 and KeyRespII.corr==0:
     DancePmisses.append(1)    

    if TrialType == 3 and KeyRespII.corr==2:
     SexNoPerrors.append(1)
    if TrialType == 3 and KeyRespII.corr==0:
     SexNoPmisses.append(1)


    if TrialType == 4 and KeyRespII.corr==2:
     DanceNoPerrors.append(1)
    if TrialType == 4 and KeyRespII.corr==0:
     DanceNoPmisses.append(1)    




    if TrialType == 1 and KeyRespI.corr==2:
     NAP1errors.append(1)
    if TrialType == 1 and KeyRespI.keys==0:
     NAP1misses.append(1)

#B
#R
#E
#A
#K

#Prepare to start routine "Break"
t = 0
BreakClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
BreakComponents = []
BreakComponents.append(text)
BreakComponents.append(text_2)
for thisComponent in BreakComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Break"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = BreakClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    elif text.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        text.setAutoDraw(False)
    
    # *text_2* updates
    if t >= 2 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)

    
    # *key_resp_2* updates
    if t >= 2 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
           key_resp_2.keys = theseKeys[-1]  # just the last key pressed
           key_resp_2.rt = key_resp_2.clock.getTime()
    # a response ends the routine
           continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "Break"-------
for thisComponent in BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.nextEntry()


#******************************************************************************************************************************************************************************************************


# set up handler to look after randomisation of conditions etc
TRIALS = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('NAP2.xlsx'),
    seed=None, name='TRIALS')
thisExp.addLoop(TRIALS)  # add the loop to the experiment
thisTRIALS = TRIALS.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTRIALS.rgb)
if thisTRIALS != None:
    for paramName in thisTRIALS.keys():
        exec(paramName + '= thisTRIALS.' + paramName)

for thisTRIALS in TRIALS:
    currentLoop = TRIALS
    # abbreviate parameter names if possible (e.g. rgb = thisTRIALS.rgb)
    if thisTRIALS != None:
        for paramName in thisTRIALS.keys():
            exec(paramName + '= thisTRIALS.' + paramName)
    
    #------Prepare to start Routine "Trial"-------
    t = 0
    TrialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    PreTrialImageI.setPos(PositionI)
    PreTrialImageI.setImage(TargetI)
    PreTrialImageII.setPos(PositionII)
    PreTrialImageII.setImage(DistractorI)
    KeyRespI = event.BuilderKeyResponse()  # create an object of type KeyResponse
    KeyRespI.status = NOT_STARTED
    PosTrialImageI.setPos(PositionIII)
    PosTrialImageI.setImage(TargetII)
    PosTrialImageII.setPos(PositionIV)
    PosTrialImageII.setImage(DistractorII)
    KeyRespII = event.BuilderKeyResponse()  # create an object of type KeyResponse
    KeyRespII.status = NOT_STARTED
    # keep track of which components have finished
    TrialComponents = []
    TrialComponents.append(text)
    TrialComponents.append(PreTrialImageI)
    TrialComponents.append(PreTrialImageII)
    TrialComponents.append(KeyRespI)
    TrialComponents.append(Fixation2)
    TrialComponents.append(PosTrialImageI)
    TrialComponents.append(PosTrialImageII)
    TrialComponents.append(KeyRespII)
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t  # underestimates by a little under one frame
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        elif text.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text.setAutoDraw(False)
        
        # *PreTrialImageI* updates
        if t >= 1.75 and PreTrialImageI.status == NOT_STARTED:
            # keep track of start time/frame for later
            PreTrialImageI.tStart = t  # underestimates by a little under one frame
            PreTrialImageI.frameNStart = frameN  # exact frame index
            PreTrialImageI.setAutoDraw(True)
        elif PreTrialImageI.status == STARTED and t >= (1.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            PreTrialImageI.setAutoDraw(False)
        
        # *PreTrialImageII* updates
        if t >= 1.75 and PreTrialImageII.status == NOT_STARTED:
            # keep track of start time/frame for later
            PreTrialImageII.tStart = t  # underestimates by a little under one frame
            PreTrialImageII.frameNStart = frameN  # exact frame index
            PreTrialImageII.setAutoDraw(True)
        elif PreTrialImageII.status == STARTED and t >= (1.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            PreTrialImageII.setAutoDraw(False)
        
        # *KeyRespI* updates
        if t >= 1.75 and KeyRespI.status == NOT_STARTED:
            # keep track of start time/frame for later
            KeyRespI.tStart = t  # underestimates by a little under one frame
            KeyRespI.frameNStart = frameN  # exact frame index
            KeyRespI.status = STARTED
            # keyboard checking is just starting
            KeyRespI.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif KeyRespI.status == STARTED and t >= (1.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            KeyRespI.status = STOPPED
        if KeyRespI.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                KeyRespI.keys = theseKeys[-1]  # just the last key pressed
                KeyRespI.rt = KeyRespI.clock.getTime()
                # was this 'correct'?
                if (KeyRespI.keys == str(RightAnswerI)) or (KeyRespI.keys == RightAnswerI):
                    KeyRespI.corr = 1
                else:
                    KeyRespI.corr = 2
                # a response ends the routine
                continueRoutine = True
        
        # *Fixation2* updates
        if t >= 3.5 and Fixation2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Fixation2.tStart = t  # underestimates by a little under one frame
            Fixation2.frameNStart = frameN  # exact frame index
            Fixation2.setAutoDraw(True)
        elif Fixation2.status == STARTED and t >= (3 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            Fixation2.setAutoDraw(False)
        
        # *PosTrialImageI* updates
        if t >= 5.25 and PosTrialImageI.status == NOT_STARTED:
            # keep track of start time/frame for later
            PosTrialImageI.tStart = t  # underestimates by a little under one frame
            PosTrialImageI.frameNStart = frameN  # exact frame index
            PosTrialImageI.setAutoDraw(True)
        elif PosTrialImageI.status == STARTED and t >= (4.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            PosTrialImageI.setAutoDraw(False)
        
        # *PosTrialImageII* updates
        if t >= 5.25 and PosTrialImageII.status == NOT_STARTED:
            # keep track of start time/frame for later
            PosTrialImageII.tStart = t  # underestimates by a little under one frame
            PosTrialImageII.frameNStart = frameN  # exact frame index
            PosTrialImageII.setAutoDraw(True)
        elif PosTrialImageII.status == STARTED and t >= (4.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            PosTrialImageII.setAutoDraw(False)
        
        # *KeyRespII* updates
        if t >= 5.25 and KeyRespII.status == NOT_STARTED:
            # keep track of start time/frame for later
            KeyRespII.tStart = t  # underestimates by a little under one frame
            KeyRespII.frameNStart = frameN  # exact frame index
            KeyRespII.status = STARTED
            # keyboard checking is just starting
            KeyRespII.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif KeyRespII.status == STARTED and t >= (4.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            KeyRespII.status = STOPPED
        if KeyRespII.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                KeyRespII.keys = theseKeys[-1]  # just the last key pressed
                KeyRespII.rt = KeyRespII.clock.getTime()
                # was this 'correct'?
                if (KeyRespII.keys == str(RightAnswerII)) or (KeyRespII.keys == RightAnswerII):
                    KeyRespII.corr = 1
                else:
                    KeyRespII.corr = 2
                # a response ends the routine
                continueRoutine = True
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Trial"-------
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
        
    # check responses
    if KeyRespI.keys in ['', [], None]:  # No response was made
       KeyRespI.keys=None
       # was no response the correct answer?!
       if str(RightAnswerI).lower() == 'none': KeyRespI.corr = 1  # correct non-response
       else: KeyRespI.corr = 0  # failed to respond (incorrectly)
    # store data for TRIALS (TrialHandler)
    TRIALS.addData('KeyRespI.keys',KeyRespI.keys)
    TRIALS.addData('KeyRespI.corr', KeyRespI.corr)
    if KeyRespI.keys != None:  # we had a response
        TRIALS.addData('KeyRespI.rt', KeyRespI.rt)
    # check responses
    if KeyRespII.keys in ['', [], None]:  # No response was made
       KeyRespII.keys=None
       # was no response the correct answer?!
       if str(RightAnswerII).lower() == 'none': KeyRespII.corr = 1  # correct non-response
       else: KeyRespII.corr = 0  # failed to respond (incorrectly)
    # store data for TRIALS (TrialHandler)
    TRIALS.addData('KeyRespII.keys',KeyRespII.keys)
    TRIALS.addData('KeyRespII.corr', KeyRespII.corr)
    if KeyRespII.keys != None:  # we had a response
        TRIALS.addData('KeyRespII.rt', KeyRespII.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'TRIALS'

    # store data for .prt
    if TrialType == 1 and KeyRespII.corr==1:
     SexP.append(1)
     SexP_RT.append(KeyRespII.rt)
    if TrialType == 2 and KeyRespII.corr==1:
     DanceP.append(1)
     DanceP_RT.append(KeyRespII.rt) 
    if TrialType == 3 and KeyRespII.corr==1:
     SexNoP.append(1)
     SexNoP_RT.append(KeyRespII.rt) 
    if TrialType == 4 and KeyRespII.corr==1:
     DanceNoP.append(1)
     DanceNoP_RT.append(KeyRespII.rt) 


    if TrialType == 1 and KeyRespII.corr==2:
     SexPerrors.append(1)
    if TrialType == 1 and KeyRespII.corr==0:
     SexPmisses.append(1)

    if TrialType == 2 and KeyRespII.corr==2:
     DancePerrors.append(1)
    if TrialType == 2 and KeyRespII.corr==0:
     DancePmisses.append(1)    

    if TrialType == 3 and KeyRespII.corr==2:
     SexNoPerrors.append(1)
    if TrialType ==3 and KeyRespII.corr==0:
     SexNoPmisses.append(1)

    if TrialType == 4 and KeyRespII.corr==2:
     DanceNoPerrors.append(1)
    if TrialType == 4 and KeyRespII.corr==0:
     DanceNoPmisses.append(1)    


    if TrialType == 1 and KeyRespI.corr==2:
     NAP1errors.append(1)
    if TrialType == 1 and KeyRespI.keys==0:
     NAP1misses.append(1)

#B
#R
#E
#A
#K

#Prepare to start routine "Break"
t = 0
BreakClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
BreakComponents = []
BreakComponents.append(text)
BreakComponents.append(text_2)
for thisComponent in BreakComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Break"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = BreakClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    elif text.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        text.setAutoDraw(False)
    
    # *text_2* updates
    if t >= 2 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)

    
    # *key_resp_2* updates
    if t >= 2 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
           key_resp_2.keys = theseKeys[-1]  # just the last key pressed
           key_resp_2.rt = key_resp_2.clock.getTime()
    # a response ends the routine
           continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "Break"-------
for thisComponent in BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.nextEntry()

#******************************************************************************************************************************************************************************************************

# set up handler to look after randomisation of conditions etc
TRIALS = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('NAP3.xlsx'),
    seed=None, name='TRIALS')
thisExp.addLoop(TRIALS)  # add the loop to the experiment
thisTRIALS = TRIALS.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTRIALS.rgb)
if thisTRIALS != None:
    for paramName in thisTRIALS.keys():
        exec(paramName + '= thisTRIALS.' + paramName)

for thisTRIALS in TRIALS:
    currentLoop = TRIALS
    # abbreviate parameter names if possible (e.g. rgb = thisTRIALS.rgb)
    if thisTRIALS != None:
        for paramName in thisTRIALS.keys():
            exec(paramName + '= thisTRIALS.' + paramName)
    
    #------Prepare to start Routine "Trial"-------
    t = 0
    TrialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    PreTrialImageI.setPos(PositionI)
    PreTrialImageI.setImage(TargetI)
    PreTrialImageII.setPos(PositionII)
    PreTrialImageII.setImage(DistractorI)
    KeyRespI = event.BuilderKeyResponse()  # create an object of type KeyResponse
    KeyRespI.status = NOT_STARTED
    PosTrialImageI.setPos(PositionIII)
    PosTrialImageI.setImage(TargetII)
    PosTrialImageII.setPos(PositionIV)
    PosTrialImageII.setImage(DistractorII)
    KeyRespII = event.BuilderKeyResponse()  # create an object of type KeyResponse
    KeyRespII.status = NOT_STARTED
    # keep track of which components have finished
    TrialComponents = []
    TrialComponents.append(text)
    TrialComponents.append(PreTrialImageI)
    TrialComponents.append(PreTrialImageII)
    TrialComponents.append(KeyRespI)
    TrialComponents.append(Fixation2)
    TrialComponents.append(PosTrialImageI)
    TrialComponents.append(PosTrialImageII)
    TrialComponents.append(KeyRespII)
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t  # underestimates by a little under one frame
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        elif text.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text.setAutoDraw(False)
        
        # *PreTrialImageI* updates
        if t >= 1.75 and PreTrialImageI.status == NOT_STARTED:
            # keep track of start time/frame for later
            PreTrialImageI.tStart = t  # underestimates by a little under one frame
            PreTrialImageI.frameNStart = frameN  # exact frame index
            PreTrialImageI.setAutoDraw(True)
        elif PreTrialImageI.status == STARTED and t >= (1.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            PreTrialImageI.setAutoDraw(False)
        
        # *PreTrialImageII* updates
        if t >= 1.75 and PreTrialImageII.status == NOT_STARTED:
            # keep track of start time/frame for later
            PreTrialImageII.tStart = t  # underestimates by a little under one frame
            PreTrialImageII.frameNStart = frameN  # exact frame index
            PreTrialImageII.setAutoDraw(True)
        elif PreTrialImageII.status == STARTED and t >= (1.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            PreTrialImageII.setAutoDraw(False)
        
        # *KeyRespI* updates
        if t >= 1.75 and KeyRespI.status == NOT_STARTED:
            # keep track of start time/frame for later
            KeyRespI.tStart = t  # underestimates by a little under one frame
            KeyRespI.frameNStart = frameN  # exact frame index
            KeyRespI.status = STARTED
            # keyboard checking is just starting
            KeyRespI.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif KeyRespI.status == STARTED and t >= (1.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            KeyRespI.status = STOPPED
        if KeyRespI.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                KeyRespI.keys = theseKeys[-1]  # just the last key pressed
                KeyRespI.rt = KeyRespI.clock.getTime()
                # was this 'correct'?
                if (KeyRespI.keys == str(RightAnswerI)) or (KeyRespI.keys == RightAnswerI):
                    KeyRespI.corr = 1
                else:
                    KeyRespI.corr = 2
                # a response ends the routine
                continueRoutine = True
        
        # *Fixation2* updates
        if t >= 3.5 and Fixation2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Fixation2.tStart = t  # underestimates by a little under one frame
            Fixation2.frameNStart = frameN  # exact frame index
            Fixation2.setAutoDraw(True)
        elif Fixation2.status == STARTED and t >= (3 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            Fixation2.setAutoDraw(False)
        
        # *PosTrialImageI* updates
        if t >= 5.25 and PosTrialImageI.status == NOT_STARTED:
            # keep track of start time/frame for later
            PosTrialImageI.tStart = t  # underestimates by a little under one frame
            PosTrialImageI.frameNStart = frameN  # exact frame index
            PosTrialImageI.setAutoDraw(True)
        elif PosTrialImageI.status == STARTED and t >= (4.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            PosTrialImageI.setAutoDraw(False)
        
        # *PosTrialImageII* updates
        if t >= 5.25 and PosTrialImageII.status == NOT_STARTED:
            # keep track of start time/frame for later
            PosTrialImageII.tStart = t  # underestimates by a little under one frame
            PosTrialImageII.frameNStart = frameN  # exact frame index
            PosTrialImageII.setAutoDraw(True)
        elif PosTrialImageII.status == STARTED and t >= (4.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            PosTrialImageII.setAutoDraw(False)
        
        # *KeyRespII* updates
        if t >= 5.25 and KeyRespII.status == NOT_STARTED:
            # keep track of start time/frame for later
            KeyRespII.tStart = t  # underestimates by a little under one frame
            KeyRespII.frameNStart = frameN  # exact frame index
            KeyRespII.status = STARTED
            # keyboard checking is just starting
            KeyRespII.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif KeyRespII.status == STARTED and t >= (4.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            KeyRespII.status = STOPPED
        if KeyRespII.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                KeyRespII.keys = theseKeys[-1]  # just the last key pressed
                KeyRespII.rt = KeyRespII.clock.getTime()
                # was this 'correct'?
                if (KeyRespII.keys == str(RightAnswerII)) or (KeyRespII.keys == RightAnswerII):
                    KeyRespII.corr = 1
                else:
                    KeyRespII.corr = 2
                # a response ends the routine
                continueRoutine = True
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Trial"-------
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
        
    # check responses
    if KeyRespI.keys in ['', [], None]:  # No response was made
       KeyRespI.keys=None
       # was no response the correct answer?!
       if str(RightAnswerI).lower() == 'none': KeyRespI.corr = 1  # correct non-response
       else: KeyRespI.corr = 0  # failed to respond (incorrectly)
    # store data for TRIALS (TrialHandler)
    TRIALS.addData('KeyRespI.keys',KeyRespI.keys)
    TRIALS.addData('KeyRespI.corr', KeyRespI.corr)
    if KeyRespI.keys != None:  # we had a response
        TRIALS.addData('KeyRespI.rt', KeyRespI.rt)
    # check responses
    if KeyRespII.keys in ['', [], None]:  # No response was made
       KeyRespII.keys=None
       # was no response the correct answer?!
       if str(RightAnswerII).lower() == 'none': KeyRespII.corr = 1  # correct non-response
       else: KeyRespII.corr = 0  # failed to respond (incorrectly)
    # store data for TRIALS (TrialHandler)
    TRIALS.addData('KeyRespII.keys',KeyRespII.keys)
    TRIALS.addData('KeyRespII.corr', KeyRespII.corr)
    if KeyRespII.keys != None:  # we had a response
        TRIALS.addData('KeyRespII.rt', KeyRespII.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'TRIALS'

    # store data for .prt
    if TrialType == 1 and KeyRespII.corr==1:
     SexP.append(1)
     SexP_RT.append(KeyRespII.rt)
    if TrialType == 2 and KeyRespII.corr==1:
     DanceP.append(1)
     DanceP_RT.append(KeyRespII.rt) 
    if TrialType == 3 and KeyRespII.corr==1:
     SexNoP.append(1)
     SexNoP_RT.append(KeyRespII.rt) 
    if TrialType == 4 and KeyRespII.corr==1:
     DanceNoP.append(1)
     DanceNoP_RT.append(KeyRespII.rt) 


    if TrialType == 1 and KeyRespII.corr==2:
     SexPerrors.append(1)
    if TrialType == 1 and KeyRespII.corr==0:
     SexPmisses.append(1)

    if TrialType == 2 and KeyRespII.corr==2:
     DancePerrors.append(1)
    if TrialType == 2 and KeyRespII.corr==0:
     DancePmisses.append(1)    

    if TrialType == 3 and KeyRespII.corr==2:
     SexNoPerrors.append(1)
    if TrialType == 3 and KeyRespII.corr==0:
     SexNoPmisses.append(1)


    if TrialType == 4 and KeyRespII.corr==2:
     DanceNoPerrors.append(1)
    if TrialType == 4 and KeyRespII.corr==0:
     DanceNoPmisses.append(1)    




    if TrialType == 1 and KeyRespI.corr==2:
     NAP1errors.append(1)
    if TrialType == 1 and KeyRespI.keys==0:
     NAP1misses.append(1)

#B
#R
#E
#A
#K



#******************************************************************************************************************************************************************************************************


AverageSexP_RT = (sum(SexP_RT)/(len(SexP_RT)+.0001))
AverageDanceP_RT = (sum(DanceP_RT)/(len(DanceP_RT)+.001))
AverageSexNoP_RT = (sum(SexNoP_RT)/(len(SexNoP_RT)+.001))
AverageDanceNoP_RT = (sum(DanceNoP_RT)/(len(DanceNoP_RT)+.001))

#compose prt files #NAPrun1
header = \
'FileVersion: \n' + \
'ResolutionOfTime: Volumes\n' + \
'Experiment:  NAP \n' + \
'BackgroundColor: 0 0 0\n' + \
'TextColor:   255 255 217\n' + \
'TimeCourseColor: 255 255 255\n' + \
'TimeCourseThick: 3\n' + \
'ReferenceFuncColor:  255 255 51\n' + \
'ReferenceFuncThick:  2\n' + \
'ParametricWeights:  0\n' + \
'NrOfConditions:  19\n'

output = open (prtFile + '.prt', 'w')
output.write(header)
for name,list in zip(
        ['SexP','DanceP','SexNoP','DanceNoP','NAP1errors','SexPerrors','DancePerrors','SexNoPerrors','DanceNoPerrors','NAP1misses','SexPmisses','DancePmisses','SexNoPmisses','DanceNoPmisses','SexP_RT','DanceP_RT','SexNoP_RT','DanceNoP_RT'],
        [SexP,DanceP,SexNoP,DanceNoP,NAP1errors,SexPerrors,DancePerrors,SexNoPerrors,DanceNoPerrors,NAP1misses,SexPmisses,DancePmisses,SexNoPmisses,DanceNoPmisses,SexP_RT,DanceP_RT,SexNoP_RT,DanceNoP_RT],):
    output.write('\n' + \
    name + '\n' + 'Freq: ' +
    str(len(list)) + '\n' )
    for x in list:
       output.write(str(x) + '\n')         
output.write('\n' + 'SexP_RT: ' + str(AverageSexP_RT))
output.write('\n' + 'DanceP_RT: ' + str(AverageDanceP_RT))
output.write('\n' + 'SexNoP_RT: ' + str(AverageSexNoP_RT))
output.write('\n' + 'DanceNoP_RT: ' + str(AverageDanceNoP_RT))
output.close()


#------Prepare to start Routine "thank_you"-------
t = 0
thank_youClock.reset()  # clock 
frameN = -1
routineTimer.add(3.500000)
# update component parameters for each repeat
# keep track of which components have finished
thank_youComponents = []
thank_youComponents.append(Thanks)
for thisComponent in thank_youComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "thank_you"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thank_youClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Thanks* updates
    if t >= 0.0 and Thanks.status == NOT_STARTED:
        # keep track of start time/frame for later
        Thanks.tStart = t  # underestimates by a little under one frame
        Thanks.frameNStart = frameN  # exact frame index
        Thanks.setAutoDraw(True)
    elif Thanks.status == STARTED and t >= (0.0 + (3.5-win.monitorFramePeriod*0.75)): #most of one frame period left
        Thanks.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thank_youComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "thank_you"-------
for thisComponent in thank_youComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
win.close()
core.quit()
