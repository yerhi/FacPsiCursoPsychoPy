# The thing to be change in UNS40 for TMS is the ITI time in the xls file 1.3,1.5 y 1.7.  // chk stimuli, mainly those that could be repeated or the frame
#vhVH (*)  // pa prt: introduce code to create prt folder at the beginning, before starting trials create the lists, then at the end of trials the conditions of prt and list filling, before break the proper creation of prt 
#!/usr/bin /env pythonf //  
# -*- coding: utf-8 -*-// 
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.80.06), juni 11, 2014, at 14:16
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
from psychopy.hardware import joystick

# Store info about the experiment session
expName = 'AAT'  # from the Builder filename that created this script
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
    blendMode='avg', useFBO=True, winType=joystick.backend
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess
    
    


joy = joystick.Joystick(0) 


# Initialize components for Routine "GeneralInstructions"
InstructionGClock = core.Clock()
InstructionG = visual.TextStim(win=win, ori=0, name='Instruction',
    text=u'You will now see a series of photographs. Some of the them are of sexual nature, others are not.\n\n In some blocks, when you see a photograph that is of sexual nature, you will have to APPROACH it, meaning that you should move the joystick towards you, as if you pull the picture closer to you. \n\n And if the photograph is not of sexual nature you will have to AVOID it, meaning that you should move the joystick away from you, as if you move the picture away. \n\n In other blocks you will have to do the opposite, approaching the non sexual and avoiding the sexual nature pictures. \n\n\n' ,    font=u'Arial',
    pos=[0, 0], height=0.07, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
Instruction = visual.TextStim(win=win, ori=0, name='Instruction',
    text=u'In this block you have to APPROACH the sexual nature pictures and AVOID the non sexual photographs. \n\n\n SEXUAL NATURE -> APPROACH \n\n NON SEXUAL NATURE -> AVOID  \n\n\n Try to do it as fast and accurate as possible.' ,    font=u'Arial',
    pos=[0, 0], height=0.07, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "AAv"
trialvClock = core.Clock()
fixation = visual.TextStim(win=win, ori=0, name='fixation',
    text=u'+',    font=u'Arial',
    units=u'norm', pos=[0, 0], height=.2, wrapWidth=None,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    depth=0.0)
Image = visual.ImageStim(win=win, name='Image',units=u'pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[257.6,400],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-1.0)

# Initialize components for Routine "resizev"
resizevClock = core.Clock()
image = visual.ImageStim(win=win, name='image',units=u'pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=0.0)

# Initialize components for Routine "break_2"
BreakClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text=u' BREAK',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text=u'Please press any button when you are ready to continue',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-1.0)



# Initialize components for Routine "InstruccionsReversed"
InstructionsRevClock = core.Clock()
InstructionRev = visual.TextStim(win=win, ori=0, name='InstructionRev',
    text=u'In this block you have to AVOID the sexual nature pictures and APPROACH the non sexual photographs. \n\n\n SEXUAL NATURE -> AVOID \n\n NON SEXUAL NATURE -> APPROACH  \n\n\n Try to do it as fast and accurate as possible.' ,    font=u'Arial',
    pos=[0, 0], height=0.07, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "AAvr"
trialvrClock = core.Clock()
fixation = visual.TextStim(win=win, ori=0, name='fixation',
    text=u'+',    font=u'Arial',
    units=u'norm', pos=[0, 0], height=.2, wrapWidth=None,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    depth=0.0)
Image = visual.ImageStim(win=win, name='Image',units=u'pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[257.6,400],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-1.0)

# Initialize components for Routine "resizevr"
resizevrClock = core.Clock()
image = visual.ImageStim(win=win, name='image',units=u'pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=0.0)


# Initialize components for Routine "break_2"
BreakClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text=u' BREAK',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text=u'Please press any button when you are ready to continue',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-1.0)


# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
Instruction = visual.TextStim(win=win, ori=0, name='Instruction',
    text=u'In this block you have to APPROACH the sexual nature pictures and AVOID the non sexual photographs. \n\n\n SEXUAL NATURE ->APPROACH \n\n NON SEXUAL NATURE -> AVOID  \n\n\n Try to do it as fast and accurate as possible.' ,    font=u'Arial',
    pos=[0, 0], height=0.07, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "AAh"
trialhClock = core.Clock()
fixation = visual.TextStim(win=win, ori=0, name='fixation',
    text=u'+',    font=u'Arial',
    units=u'norm', pos=[0, 0], height=.2, wrapWidth=None,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    depth=0.0)
Image = visual.ImageStim(win=win, name='Image',units=u'pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[337.9,272.5],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-1.0)


# Initialize components for Routine "resizeh"
resizehClock = core.Clock()
image = visual.ImageStim(win=win, name='image',units=u'pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=0.0)
    
# Initialize components for Routine "break_2"
BreakClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text=u' BREAK',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text=u'Please press any button when you are ready to continue',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-1.0)



# Initialize components for Routine "InstruccionsReversed"
InstructionsRevClock = core.Clock()
InstructionRev = visual.TextStim(win=win, ori=0, name='InstructionRev',
    text=u'In this block you have to AVOID the sexual nature pictures and APPROACH the non sexual photographs. \n\n\n SEXUAL NATURE ->AVOID \n\n NON SEXUAL NATURE -> APPROACH  \n\n\n Try to do it as fast and accurate as possible.' ,    font=u'Arial',
    pos=[0, 0], height=0.07, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "AAhr"
trialhrClock = core.Clock()
fixation = visual.TextStim(win=win, ori=0, name='fixation',
    text=u'+',    font=u'Arial',
    units=u'norm', pos=[0, 0], height=.2, wrapWidth=None,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    depth=0.0)
Image = visual.ImageStim(win=win, name='Image',units=u'pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[337.9,272.5],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-1.0)


# Initialize components for Routine "resizehr"
resizehrClock = core.Clock()
image = visual.ImageStim(win=win, name='image',units=u'pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=0.0)


# Initialize components for Routine "break_2"
BreakClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text=u' BREAK',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text=u'Please press any button when you are ready to continue',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "thanx"
thanksClock = core.Clock()
thanksText = visual.TextStim(win=win, ori=0, name='thanksText',
    text='This is the end of this task.\n\nThank you!',    font='arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    depth=0.0)# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

SexApp=[]
SexAv=[]
DanceApp=[]
DanceAv=[]
SexAppM=[]
SexAvM=[]
DanceAppM=[]
DanceAvM=[]
SexAppE=[]
SexAvE=[]
DanceAppE=[]
DanceAvE=[]
SexAppRT=[]
SexAvRT=[]
DanceAppRT=[]
DanceAvRT=[]



# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 



#------Prepare to start Routine "InstructionsG"-------
t = 0
InstructionGClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
InstructionGComponents = []
InstructionGComponents.append(InstructionG)
for thisComponent in InstructionGComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "InstructionsG"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = InstructionGClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instruction* updates
    if t >= 0.0 and InstructionG.status == NOT_STARTED:
        # keep track of start time/frame for later
        InstructionG.tStart = t  # underestimates by a little under one frame
        InstructionG.frameNStart = frameN  # exact frame index
        InstructionG.setAutoDraw(True)
    
    buttons = sum(joy.getAllButtons())
   # *Joy.buttons* updates
    if t >= 0.0 and buttons:
         continueRoutine = False
    
    
    theseKeys = event.getKeys()
        
        # check for quit:
    if "escape" in theseKeys:
            endExpNow = True
        
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionGComponents:
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

#-------Ending Routine "InstructionsG"-------
for thisComponent in InstructionGComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


 

# aqui comenzar BigLoop que comprende 4 bloques. 
# set up handler to look after randomisation of conditions etc
BigLoop = data.TrialHandler(nReps=1, method=u'random', 
    extraInfo=expInfo, originPath=None,
    trialList=[None],
        seed=None, name='BigLoop')
thisExp.addLoop(BigLoop)  # add the loop to the experiment
thisBigLoop = BigLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_5.rgb)
if thisBigLoop != None:
    for paramName in thisBigLoop.keys():
        exec(paramName + '= BigLoop.' + paramName)

for thisBigLoop in BigLoop:
    currentLoop = BigLoop
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisBigLoop != None:
        for paramName in thisBigLoop.keys():
            exec(paramName + '= thisBigLoop.' + paramName) 
           


    # MediumLoop que contiene AATv reversed individual y break        */*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*
    # set up handler to look after randomisation of conditions etc
    MediumLoopVr = data.TrialHandler(nReps=1, method=u'sequential', 
        extraInfo=expInfo, originPath=None,
        trialList=[None],
        seed=None, name='MediumLoopVr')
    thisExp.addLoop(MediumLoopVr)  # add the loop to the experiment
    thisMediumLoopVr = MediumLoopVr.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrial_6.rgb)
    if thisMediumLoopVr != None:
        for paramName in thisMediumLoopVr.keys():
            exec(paramName + '= thisMediumLoopVr.' + paramName)
    
    for thisMediumLoopVr in MediumLoopVr:
        currentLoop = MediumLoopVr
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
        if thisMediumLoopVr != None:
            for paramName in thisMediumLoopVr.keys():
                        exec(paramName + '= thisMediumLoopVr.' + paramName)
        
        
        #------Prepare to start Routine "InstructionsRev"-------
        t = 0
        InstructionsRevClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_2.status = NOT_STARTED
        # keep track of which components have finished
        InstructionsRevComponents = []
        InstructionsRevComponents.append(InstructionRev)
        for thisComponent in InstructionsRevComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "InstructionsRev"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = InstructionsRevClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Instruction* updates
            if t >= 0.0 and InstructionRev.status == NOT_STARTED:
                # keep track of start time/frame for later
                InstructionRev.tStart = t  # underestimates by a little under one frame
                InstructionRev.frameNStart = frameN  # exact frame index
                InstructionRev.setAutoDraw(True)
                event.clearEvents(eventType='joystick')
            
            
            if t >= 1 and InstructionRev.status == STARTED:
            
            
             suttons = sum(joy.getAllButtons())
             
             if t >= 0 and suttons:
                continueRoutine = False
                
             theseKeys = event.getKeys()
                
                # check for quit:
             if "escape" in theseKeys:
                endExpNow = True
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in InstructionsRevComponents:
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
        
        #-------Ending Routine "InstructionsRev"-------
        for thisComponent in InstructionsRevComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        # Loop for AAT Vr reversed 
        # set up handler to look after randomisation of conditions etc
        ApproachAvoidVr = data.TrialHandler(nReps=1, method=u'random', 
            extraInfo=expInfo, originPath=None,
            trialList=data.importConditions(u'AAT175v.xlsx'),
            seed=None, name='ApproachAvoidVrev')
        thisExp.addLoop(ApproachAvoidVr)  # add the loop to the experiment
        thisApproachAvoidVr = ApproachAvoidVr.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb=thisApproachAvoidvr.rgb)
        if thisApproachAvoidVr != None:
            for paramName in thisApproachAvoidVr.keys():
                exec(paramName + '= thisApproachAvoidVr.' + paramName)
        
        for thisApproachAvoidVr in ApproachAvoidVr:
            currentLoop = ApproachAvoidVr
            # abbreviate parameter names if possible (e.g. rgb = thisApproachAvoid.rgb)
            if thisApproachAvoidVr != None:
                for paramName in thisApproachAvoidVr.keys():
                    exec(paramName + '= thisApproachAvoidVr.' + paramName)
        
        
            #------Prepare to start Routine "trialVreversed"-------
            t = 0
            trialvrClock.reset()  # clock 
            frameN = -1
            routineTimer.add(ITI+1.75)
            avoid=[]
            approach=[]
            # update component parameters for each repeat
            Image.setImage(Pic)
            Image.setSize([257.6,400])
            Resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
            Resp.status = NOT_STARTED
            # keep track of which components have finished
            trialvrComponents = []
            trialvrComponents.append(fixation)
            trialvrComponents.append(Image)
            for thisComponent in trialvrComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "trialVreversed"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = trialvrClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation* updates
                if t >= 0.0 and fixation.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    fixation.tStart = t  # underestimates by a little under one frame
                    fixation.frameNStart = frameN  # exact frame index
                    fixation.setAutoDraw(True)
                elif fixation.status == STARTED and t >= (0.0 + (ITI-win.monitorFramePeriod*0.75)): #most of one frame period left
                    fixation.setAutoDraw(False)
                    
                # *Image* updates
                if t >= ITI and Image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    Image.tStart = t  # underestimates by a little under one frame
                    Image.frameNStart = frameN  # exact frame index
                    Image.setAutoDraw(True)
                    event.clearEvents(eventType='joystick')
                elif Image.status == STARTED and t >= (ITI + (1.75-win.monitorFramePeriod*0.75)): #most of one frame period left
                    Image.setAutoDraw(False)
                    
                # *Resp* updates                    
                    
                if t >= ITI and joy.getY()>.9:
                    Image.setSize([128.8,200])
                    avoid.append(1)
                    # keep track of start time/frame for later
                    if 'Sex' in ImageID: 
                      RespCorr = 1
                    else:
                      RespCorr = 2 

                # keyboard checking is just starting
                    RespRT = ((trialvrClock.getTime())-ITI) # now t=0
                    ApproachAvoidVr.addData('RespCorr',RespCorr)
                    ApproachAvoidVr.addData('Resp',Resp)
                    ApproachAvoidVr.addData('RespRT',RespRT)
                    
                if t >= ITI and joy.getY()<-.9:
                    Image.setSize([515.2,800])
                    approach.append(1)
                    # keep track of start time/frame for later
                    if 'Dancers' in ImageID: 
                      RespCorr = 1
                    else:
                      RespCorr = 2
                    
                    # keyboard checking is just starting
                    RespRT = ((trialvrClock.getTime())-ITI)  # now t=0
                    ApproachAvoidVr.addData('RespCorr',RespCorr)
                    ApproachAvoidVr.addData('Resp',Resp)
                    ApproachAvoidVr.addData('RespRT',RespRT)
                
                # keep track of start time/frame for later                 
                if t>= ITI and len(avoid)<1 and len(approach)<1:
                    RespCorr=None
                    RespRT=None               
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineTimer.reset()  # if we abort early the non-slip timer needs reset
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trialvrComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            tiempoImage = trialvrClock.getTime()    
            
            
            #-------Ending Routine "trialVreversed"-------
            for thisComponent in trialvrComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            thisExp.nextEntry()
            
            # Store data for .prt 
            if 'Sex' in ImageID and RespCorr==1: 
             SexAv.append(1)
             SexAvRT.append(RespRT)
            if 'Dancers'in ImageID and RespCorr==1:
             DanceApp.append(1)
             DanceAppRT.append(RespRT)
            if 'Sex' in ImageID and RespCorr==2:
             SexAvE.append(1)
            if 'Sex' in ImageID and RespCorr==None:
             SexAvM.append(1)
            if 'Dancers' in ImageID and RespCorr==2:
              DanceAppE.append(1)         
            if 'Dancers' in ImageID and RespCorr==None:
             DanceAppM.append(1)
         
        
        
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
                event.clearEvents(eventType='joystick')
             
             
            if t >= 2 and text_2.status == STARTED:
                suttons = sum(joy.getAllButtons())
                
                if t >= 2.0 and suttons:
                    continueRoutine = False
                    
                theseKeys = event.getKeys()
                    
                    # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True                
                
                
            
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
       
       
     # MediumLoop que contiene AATh y break                                           */*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*//*/*/*/*/*/*/*/*/*/*/*//*/*/*/*//*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
    # set up handler to look after randomisation of conditions etc
    MediumLoopH = data.TrialHandler(nReps=1, method=u'sequential', 
        extraInfo=expInfo, originPath=None,
        trialList=[None],
        seed=None, name='MediumLoopH')
    thisExp.addLoop(MediumLoopH)  # add the loop to the experiment
    thisMediumLoopH = MediumLoopH.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrial_6.rgb)
    if thisMediumLoopH != None:
        for paramName in thisMediumLoopH.keys():
            exec(paramName + '= thisMediumLoopH.' + paramName)
    
    for thisMediumLoopH in MediumLoopH:
        currentLoop = MediumLoopH
        # abbreviate parameter names if possible (e.g. rgb = MediumLoopH.rgb)
        if thisMediumLoopH != None:
            for paramName in thisMediumLoopH.keys():
                exec(paramName + '= thisMediumLoopH.' + paramName)


        #------Prepare to start Routine "Instructions"-------
        t = 0
        InstructionsClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_2.status = NOT_STARTED
        # keep track of which components have finished
        InstructionsComponents = []
        InstructionsComponents.append(Instruction)
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        #-------Start Routine "Instructions"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = InstructionsClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Instruction* updates
            if t >= 0.0 and Instruction.status == NOT_STARTED:
                # keep track of start time/frame for later
                Instruction.tStart = t  # underestimates by a little under one frame
                Instruction.frameNStart = frameN  # exact frame index
                Instruction.setAutoDraw(True)
                event.clearEvents(eventType='joystick')
            
            if t >= 1.0 and Instruction.status == STARTED:
            
            
             suttons = sum(joy.getAllButtons())
           
             if t >= 1.0 and suttons:
                continueRoutine = False
                
             theseKeys = event.getKeys()
                
                # check for quit:
             if "escape" in theseKeys:
                   endExpNow = True
 
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in InstructionsComponents:
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
        
        #-------Ending Routine "Instructions"-------
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        


        # Individual Loop for AATH 
        # set up handler to look after randomisation of conditions etc
        ApproachAvoidH = data.TrialHandler(nReps=1, method=u'random', 
            extraInfo=expInfo, originPath=None,
            trialList=data.importConditions(u'AAT175.xlsx'),
            seed=None, name='ApproachAvoidH')
        thisExp.addLoop(ApproachAvoidH)  # add the loop to the experiment
        thisApproachAvoidH = ApproachAvoidH.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb=thisApproachAvoid.rgb)
        if thisApproachAvoidH != None:
            for paramName in thisApproachAvoidH.keys():
                exec(paramName + '= thisApproachAvoidH.' + paramName)
        
        for thisApproachAvoidH in ApproachAvoidH:
            currentLoop = ApproachAvoidH
            # abbreviate parameter names if possible (e.g. rgb = thisApproachAvoidH.rgb)
            if thisApproachAvoidH != None:
                for paramName in thisApproachAvoidH.keys():
                    exec(paramName + '= thisApproachAvoidH.' + paramName)
            
            
            #------Prepare to start Routine "trialh"-------
            t = 0
            trialhClock.reset()  # clock 
            frameN = -1
            routineTimer.add(ITI+1.75)
            avoid=[]
            approach=[]
            # update component parameters for each repeat
            Image.setImage(Pic)
            Image.setSize([337.9,272.5])
            Resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
            Resp.status = NOT_STARTED
            # keep track of which components have finished
            trialhComponents = []
            trialhComponents.append(fixation)
            trialhComponents.append(Image)
            for thisComponent in trialhComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "trialh"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = trialhClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation* updates
                if t >= 0.0 and fixation.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    fixation.tStart = t  # underestimates by a little under one frame
                    fixation.frameNStart = frameN  # exact frame index
                    fixation.setAutoDraw(True)
                elif fixation.status == STARTED and t >= (0.0 + (ITI-win.monitorFramePeriod*0.75)): #most of one frame period left
                    fixation.setAutoDraw(False)
                
                # *Image* updates
                if t >= ITI and Image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    Image.tStart = t  # underestimates by a little under one frame
                    Image.frameNStart = frameN  # exact frame index
                    Image.setAutoDraw(True)
                    event.clearEvents(eventType='joystick')
                elif Image.status == STARTED and t >= (ITI + (1.75-win.monitorFramePeriod*0.75)): #most of one frame period left
                    Image.setAutoDraw(False)
                
                 # *Resp* updates
                 
                if t >= ITI and joy.getY()>.9:
                    Image.setSize([170.5,137.5])
                    avoid.append(1)
                    # keep track of start time/frame for later
                    if 'Dancers' in ImageID: 
                      RespCorr = 1
                    else:
                      RespCorr = 2                    
                    
                    # keyboard checking is just starting
                    RespRT = ((trialhClock.getTime())-ITI) # now t=0
                    ApproachAvoidH.addData('RespCorr',RespCorr)
                    ApproachAvoidH.addData('Resp',Resp)
                    ApproachAvoidH.addData('RespRT',RespRT)
                    
                if t >= ITI and joy.getY()<-.9:
                    Image.setSize([682,550])
                    approach.append(1)
                    # keep track of start time/frame for later
                    if 'Sex' in ImageID: 
                      RespCorr = 1
                    else:
                      RespCorr = 2                    
                    
                    # keyboard checking is just starting
                    RespRT = ((trialhClock.getTime())-ITI) # now t=0
                    ApproachAvoidH.addData('RespCorr',RespCorr)
                    ApproachAvoidH.addData('Resp',Resp)
                    ApproachAvoidH.addData('RespRT',RespRT)
                    
                # keep track of start time/frame for later                 
                if t>= ITI and len(avoid)<1 and len(approach)<1:
                    RespCorr=None
                    RespRT=None               
                    
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineTimer.reset()  # if we abort early the non-slip timer needs reset
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trialhComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            tiempoImage = trialhClock.getTime()    
            
            
            #-------Ending Routine "trialh"-------
            for thisComponent in trialhComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.nextEntry()
            
            #aqui acaba individual loop
            # Store data for .prt 
            if 'Sex' in ImageID and RespCorr==1: 
             SexApp.append(1)
             SexAppRT.append(RespRT)
            if 'Dancers'in ImageID and RespCorr==1:
             DanceAv.append(1)
             DanceAvRT.append(RespRT)
            if 'Sex' in ImageID and RespCorr==2:
             SexAppE.append(1)
            if 'Sex' in ImageID and RespCorr==None:
             SexAppM.append(1)
            if 'Dancers' in ImageID and RespCorr==2:
             DanceAvE.append(1)         
            if 'Dancers' in ImageID and RespCorr==None:
             DanceAvM.append(1)
         
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
                event.clearEvents(eventType='joystick')
                
            if t >= 2 and text_2.status == STARTED:
                suttons = sum(joy.getAllButtons())
                
                if t >= 2 and suttons:
                  continueRoutine = False
                   
                theseKeys = event.getKeys()
                    
                    # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True                
                
            
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
        
        
# MediumLoop que contiene AAThrev y break                                      /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*//*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/**/*/*
    # set up handler to look after randomisation of conditions etc
    MediumLoopHr = data.TrialHandler(nReps=1, method=u'sequential', 
        extraInfo=expInfo, originPath=None,
        trialList=[None],
        seed=None, name='MediumLoopHr')
    thisExp.addLoop(MediumLoopHr)  # add the loop to the experiment
    thisMediumLoopHr = MediumLoopHr.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrial_6.rgb)
    if thisMediumLoopHr != None:
        for paramName in thisMediumLoopHr.keys():
            exec(paramName + '= thisMediumLoopHr.' + paramName)
    
    for thisMediumLoopHr in MediumLoopHr:
        currentLoop = MediumLoopHr
        # abbreviate parameter names if possible (e.g. rgb = MediumLoopH.rgb)
        if thisMediumLoopHr != None:
            for paramName in thisMediumLoopHr.keys():
                exec(paramName + '= thisMediumLoopHr.' + paramName)
 

        #------Prepare to start Routine "InstructionsRev"-------
        t = 0
        InstructionsRevClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_2.status = NOT_STARTED
        # keep track of which components have finished
        InstructionsRevComponents = []
        InstructionsRevComponents.append(InstructionRev)
        for thisComponent in InstructionsRevComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "InstructionsRev"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = InstructionsRevClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Instruction* updates
            if t >= 0.0 and InstructionRev.status == NOT_STARTED:
                # keep track of start time/frame for later
                InstructionRev.tStart = t  # underestimates by a little under one frame
                InstructionRev.frameNStart = frameN  # exact frame index
                InstructionRev.setAutoDraw(True)
                event.clearEvents(eventType='joystick')
            
            if t >= 1.0 and InstructionRev.status == STARTED:
            
            
             suttons = sum(joy.getAllButtons())
           
             if t >= 1.0 and suttons:
                continueRoutine = False
                
             theseKeys = event.getKeys()
                
                # check for quit:
             if "escape" in theseKeys:
                   endExpNow = True
                   
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in InstructionsRevComponents:
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
        
        #-------Ending Routine "InstructionsRev"-------
        for thisComponent in InstructionsRevComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)


        # Individual Loop for AAT H rev 
        # set up handler to look after randomisation of conditions etc
        ApproachAvoidHr = data.TrialHandler(nReps=1, method=u'random', 
            extraInfo=expInfo, originPath=None,
            trialList=data.importConditions(u'AAT175.xlsx'),
            seed=None, name='ApproachAvoidHr')
        thisExp.addLoop(ApproachAvoidHr)  # add the loop to the experiment
        thisApproachAvoidHr = ApproachAvoidHr.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb=thisApproachAvoid.rgb)
        if thisApproachAvoidHr != None:
            for paramName in thisApproachAvoidHr.keys():
                exec(paramName + '= thisApproachAvoidHr.' + paramName)
        
        for thisApproachAvoidHr in ApproachAvoidHr:
            currentLoop = ApproachAvoidHr
            # abbreviate parameter names if possible (e.g. rgb = thisApproachAvoidHr.rgb)
            if thisApproachAvoidHr != None:
                for paramName in thisApproachAvoidHr.keys():
                    exec(paramName + '= thisApproachAvoidHr.' + paramName)



            #------Prepare to start Routine "trialreversed"-------
            t = 0
            trialhrClock.reset()  # clock 
            frameN = -1
            routineTimer.add(ITI+1.75)
            avoid=[]
            approach=[]
            # update component parameters for each repeat
            Image.setImage(Pic)
            Image.setSize([337.9,272.5])
            Resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
            Resp.status = NOT_STARTED
            # keep track of which components have finished
            trialhrComponents = []
            trialhrComponents.append(fixation)
            trialhrComponents.append(Image)
            for thisComponent in trialhrComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "trialhreversed"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = trialhrClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation* updates
                if t >= 0.0 and fixation.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    fixation.tStart = t  # underestimates by a little under one frame
                    fixation.frameNStart = frameN  # exact frame index
                    fixation.setAutoDraw(True)
                elif fixation.status == STARTED and t >= (0.0 + (ITI-win.monitorFramePeriod*0.75)): #most of one frame period left
                    fixation.setAutoDraw(False)
                
                # *Image* updates
                if t >= ITI and Image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    Image.tStart = t  # underestimates by a little under one frame
                    Image.frameNStart = frameN  # exact frame index
                    Image.setAutoDraw(True)
                    event.clearEvents(eventType='joystick')
                elif Image.status == STARTED and t >= (ITI + (1.75-win.monitorFramePeriod*0.75)): #most of one frame period left
                    Image.setAutoDraw(False)
                
                # *Resp* updates
                 
                if t >= ITI and joy.getY()>.9:
                    Image.setSize([170.5,137.5])
                    avoid.append(1)
                    # keep track of start time/frame for later
                    if 'Sex' in ImageID: 
                      RespCorr = 1
                    else:
                      RespCorr = 2                    
                    
                # keyboard checking is just starting
                    RespRT = ((trialhrClock.getTime())-ITI) # now t=0
                    ApproachAvoidHr.addData('RespCorr',RespCorr)
                    ApproachAvoidHr.addData('Resp',Resp)
                    ApproachAvoidHr.addData('RespRT',RespRT)                 
                    
                if t >= ITI and joy.getY()<-.9:
                    Image.setSize([682,550])
                    approach.append(1)
                    # keep track of start time/frame for later
                    if 'Dancers' in ImageID: 
                      RespCorr = 1
                    else:
                      RespCorr = 2                     
                    
                    # keyboard checking is just starting
                    RespRT = ((trialhrClock.getTime())-ITI)  # now t=0
                    ApproachAvoidHr.addData('RespCorr',RespCorr)
                    ApproachAvoidHr.addData('Resp',Resp)
                    ApproachAvoidHr.addData('RespRT',RespRT)
                
                # keep track of start time/frame for later                 
                if t>= ITI and len(avoid)<1 and len(approach)<1:
                    RespCorr=None
                    RespRT=None               
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineTimer.reset()  # if we abort early the non-slip timer needs reset
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trialhrComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            tiempoImage = trialhrClock.getTime()    
            
            
            #-------Ending Routine "trialhreversed"-------
            for thisComponent in trialhrComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            thisExp.nextEntry()
            
            # Store data for .prt 
            if 'Sex' in ImageID and RespCorr==1: 
             SexAv.append(1)
             SexAvRT.append(RespRT)
            if 'Dancers'in ImageID and RespCorr==1:
             DanceApp.append(1)
             DanceAppRT.append(RespRT)
            if 'Sex' in ImageID and RespCorr==2:
             SexAvE.append(1)
            if 'Sex' in ImageID and RespCorr==None:
             SexAvM.append(1)
            if 'Dancers' in ImageID and RespCorr==2:
              DanceAppE.append(1)         
            if 'Dancers' in ImageID and RespCorr==None:
             DanceAppM.append(1)
       
       
       
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
                event.clearEvents(eventType='joystick')

            if t >= 2 and text_2.status == STARTED:
                suttons = sum(joy.getAllButtons())
                
                if t >= 2 and suttons:
                  continueRoutine = False
                   
                theseKeys = event.getKeys()
                    
                    # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True                
                
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
    
    thisExp.nextEntry()

    # MediumLoop que contiene AATv y break */*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/**/*/*/*/*/*/**/*/*/*/*/*/*/*//*/*/*/*/*/*///*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*
    # set up handler to look after randomisation of conditions etc
    MediumLoop = data.TrialHandler(nReps=1, method=u'sequential', 
        extraInfo=expInfo, originPath=None,
        trialList=[None],
        seed=None, name='MediumLoop')
    thisExp.addLoop(MediumLoop)  # add the loop to the experiment
    thisMediumLoop = MediumLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrial_6.rgb)
    if thisMediumLoop != None:
        for paramName in thisMediumLoop.keys():
            exec(paramName + '= thisMediumLoop.' + paramName)
    
    for thisMediumLoop in MediumLoop:
        currentLoop = MediumLoop
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
        if thisMediumLoop != None:
            for paramName in thisMediumLoop.keys():
                exec(paramName + '= thisMediumLoop.' + paramName)

        #------Prepare to start Routine "Instructions"-------
        t = 0
        InstructionsClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_2.status = NOT_STARTED
        # keep track of which components have finished
        InstructionsComponents = []
        InstructionsComponents.append(Instruction)
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        #-------Start Routine "Instructions"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = InstructionsClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Instruction* updates
            if t >= 0.0 and Instruction.status == NOT_STARTED:
                # keep track of start time/frame for later
                Instruction.tStart = t  # underestimates by a little under one frame
                Instruction.frameNStart = frameN  # exact frame index
                Instruction.setAutoDraw(True)
                event.clearEvents(eventType='joystick')
            
            if t >= 1.0 and Instruction.status == STARTED:
            
            
             suttons = sum(joy.getAllButtons())
           
             if t >= 1.0 and suttons:
                continueRoutine = False
                
             theseKeys = event.getKeys()
                
                # check for quit:
             if "escape" in theseKeys:
                   endExpNow = True
 
    
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in InstructionsComponents:
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
        
        #-------Ending Routine "Instructions"-------
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)


        # Loop individual para AATv 
        # set up handler to look after randomisation of conditions etc
        ApproachAvoidv = data.TrialHandler(nReps=1, method=u'random', 
            extraInfo=expInfo, originPath=None,
            trialList=data.importConditions(u'AAT175v.xlsx'),
            seed=None, name='ApproachAvoidv')
        thisExp.addLoop(ApproachAvoidv)  # add the loop to the experiment
        thisApproachAvoidv = ApproachAvoidv.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb=thisApproachAvoidv.rgb)
        if thisApproachAvoidv != None:
            for paramName in thisApproachAvoidv.keys():
                exec(paramName + '= thisApproachAvoidv.' + paramName)
        
        for thisApproachAvoidv in ApproachAvoidv:
            currentLoop = ApproachAvoidv
            # abbreviate parameter names if possible (e.g. rgb = thisApproachAvoidv.rgb)
            if thisApproachAvoidv != None:
                for paramName in thisApproachAvoidv.keys():
                    exec(paramName + '= thisApproachAvoidv.' + paramName)

            #------Prepare to start Routine "trialV"-------
            t = 0
            trialvClock.reset()  # clock 
            frameN = -1
            routineTimer.add(ITI+1.75)
            avoid=[]
            approach=[]
            # update component parameters for each repeat
            Image.setImage(Pic)
            Image.setSize([257.6,400])
            Resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
            Resp.status = NOT_STARTED
            # keep track of which components have finished
            trialvComponents = []
            trialvComponents.append(fixation)
            trialvComponents.append(Image)
            for thisComponent in trialvComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "trialV"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = trialvClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation* updates
                if t >= 0.0 and fixation.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    fixation.tStart = t  # underestimates by a little under one frame
                    fixation.frameNStart = frameN  # exact frame index
                    fixation.setAutoDraw(True)
                elif fixation.status == STARTED and t >= (0.0 + (ITI-win.monitorFramePeriod*0.75)): #most of one frame period left
                    fixation.setAutoDraw(False)
                
                # *Image* updates
                if t >= ITI and Image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    Image.tStart = t  # underestimates by a little under one frame
                    Image.frameNStart = frameN  # exact frame index
                    Image.setAutoDraw(True)
                    event.clearEvents(eventType='joystick')
                elif Image.status == STARTED and t >= (ITI + (1.75-win.monitorFramePeriod*0.75)): #most of one frame period left
                    Image.setAutoDraw(False)
                
                 # *Resp* updates
                 
                if t >= ITI and joy.getY()>.9:
                    Image.setSize([128.8,200])
                    avoid.append(1)
                    # keep track of start time/frame for later
                    if 'Dancers' in ImageID: 
                      RespCorr = 1
                    else:
                      RespCorr = 2                    
                    
                    # keyboard checking is just starting
                    RespRT = ((trialvClock.getTime())-ITI) # now t=0
                    ApproachAvoidv.addData('RespCorr',RespCorr)
                    ApproachAvoidv.addData('Resp',Resp)
                    ApproachAvoidv.addData('RespRT',RespRT)
                    
                if t >= ITI and joy.getY()<-.9:
                    Image.setSize([515.2,800])
                    approach.append(1)
                    # keep track of start time/frame for later
                    if 'Sex' in ImageID: 
                      RespCorr = 1
                    else:
                      RespCorr = 2                    
                    
                    # keyboard checking is just starting
                    RespRT = ((trialvClock.getTime())-ITI)  # now t=0
                    ApproachAvoidv.addData('RespCorr',RespCorr)
                    ApproachAvoidv.addData('Resp',Resp)
                    ApproachAvoidv.addData('RespRT',RespRT)
                   
                # keep track of start time/frame for later                 
                if t>= ITI and len(avoid)<1 and len(approach)<1:
                    RespCorr=None
                    RespRT=None               
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineTimer.reset()  # if we abort early the non-slip timer needs reset
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trialvComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            tiempoImage = trialvClock.getTime()    
            
            
            #-------Ending Routine "trialV"-------
            for thisComponent in trialvComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
              
            thisExp.nextEntry()
            
            #aqui acaba individual loop
            # Store data for .prt 
            if 'Sex' in ImageID and RespCorr==1: 
             SexApp.append(1)
             SexAppRT.append(RespRT)
            if 'Dancers'in ImageID and RespCorr==1:
             DanceAv.append(1)
             DanceAvRT.append(RespRT)
            if 'Sex' in ImageID and RespCorr==2:
             SexAppE.append(1)
            if 'Sex' in ImageID and RespCorr==None:
             SexAppM.append(1)
            if 'Dancers' in ImageID and RespCorr==2:
             DanceAvE.append(1)         
            if 'Dancers' in ImageID and RespCorr==None:
             DanceAvM.append(1)
                
          


    #compose prt files #AAT
    AverageSexAvRT = (sum(SexAvRT)/(len(SexAvRT)+.0001))
    AverageDanceAppRT = (sum(DanceAppRT)/(len(DanceAppRT)+.0001))
    AverageSexAppRT = (sum(SexAppRT)/(len(SexAppRT)+.0001))
    AverageDanceAvRT = (sum(DanceAvRT)/(len(DanceAvRT)+.0001))
    
    header = \
    'Experiment:  AAT_Hrev \n' + \
    'BackgroundColor: 0 0 0\n' + \
    'TextColor:   255 255 217\n' + \
    'TimeCourseColor: 255 255 255\n' + \
    'TimeCourseThick: 3\n' + \
    'ReferenceFuncColor:  255 255 51\n' + \
    'ReferenceFuncThick:  2\n' + \
    'NrOfConditions:  17\n'
    
    output = open (prtFile + '.prt', 'w')
    output.write(header)
    for name,list in zip(
            ['SexApp','SexAv','DanceApp','DanceAv','SexAppE','SexAvE','DanceAppE','DanceAvE','SexAppM','SexAvM','DanceAppM','DanceAvM','SexAppRT','SexAvRT','DanceAppRT','DanceAvRT'],
            [SexApp,SexAv,DanceApp,DanceAv,SexAppE,SexAvE,DanceAppE,DanceAvE,SexAppM,SexAvM,DanceAppM,DanceAvM,SexAppRT,SexAvRT,DanceAppRT,DanceAvRT]):
        output.write('\n' + \
        name + '\n' + 'Freq: ' +
        str(len(list)) + '\n' )
        for x in list:
            output.write(str(x) + '\n')         
    output.write('\n' + 'AverageSexAppRT: ' + str(AverageSexAppRT))
    output.write('\n' + 'AverageSexAvRT: ' + str(AverageSexAvRT))
    output.write('\n' + 'AverageDanceAppRT: ' + str(AverageDanceAppRT))
    output.write('\n' + 'AverageDanceAvRT: ' + str(AverageDanceAvRT))
    output.close()


win.close()
core.quit()
    # completed 1 repeats of 'ApproachAvoid'

