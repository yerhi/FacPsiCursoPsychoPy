#!/usr/bin/env python2  In this version the letter lasts for 200 ms and there is ITI, from 650 to 1050 ms. The prt creation file is added
# -*- coding: utf-8 -*- *** For version B, change Letra por LetraB and the codification of responses for lists in prt (if 'M' in blablaba...)
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.80.03), October 31, 2014, at 18:34
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
expName = 'GoNoGo'  # from the Builder filename that created this script
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


endExpNow = False  # flag for 'escape' or other condition => quit the ex



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

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
Instr = visual.TextStim(win=win, ori=0, name='Instr',
    text=u'Go- No go.\n\nIn this task you will see either an \u201c M \u201d or a  \u201c C \u201c on the screen. What we now want you to do is to put your right index finger on the spacebar. When you see a \u201cC\u201c presented on the screen, you should press the spacebar as fast as possible. However, when you see an \u201cM\u201c on the screen, you must NOT press the key. \n\nIt is very important that you react as fast as possible, but also that you watch out not to make any mistakes.\n\nPress any key to continue. \n',    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "Instr2"
Instr2Clock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='Thus, please remember:\n\nC -> DO respond\n\nM -> DO NOT respond \n\nPlease press any key to start.',    font='Arial',
    pos=[0, 0], height=0.09, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "InitFix"
InitFixClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='+',    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
Letter = visual.TextStim(win=win, ori=0, name='Letter',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.25, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)
fix = visual.TextStim(win=win, ori=0, name='fix',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "Break"
BreakClock = core.Clock()
Breaaak = visual.TextStim(win=win, ori=0, name='Breaaak',
    text='BREAK\n',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
Continue = visual.TextStim(win=win, ori=0, name='Continue',
    text=u'Please press the spacebar to continue.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
Letter = visual.TextStim(win=win, ori=0, name='Letter',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.25, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)
fix = visual.TextStim(win=win, ori=0, name='fix',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "Break"
BreakClock = core.Clock()
Breaaak = visual.TextStim(win=win, ori=0, name='Breaaak',
    text='BREAK\n',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
Continue = visual.TextStim(win=win, ori=0, name='Continue',
    text=u'Please press the spacebar to continue.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
Letter = visual.TextStim(win=win, ori=0, name='Letter',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.25, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)
fix = visual.TextStim(win=win, ori=0, name='fix',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "Break"
BreakClock = core.Clock()
Breaaak = visual.TextStim(win=win, ori=0, name='Breaaak',
    text='BREAK\n',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
Continue = visual.TextStim(win=win, ori=0, name='Continue',
    text=u'Please press the spacebar to continue.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
Letter = visual.TextStim(win=win, ori=0, name='Letter',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.25, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)
fix = visual.TextStim(win=win, ori=0, name='fix',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "Break"
BreakClock = core.Clock()
Breaaak = visual.TextStim(win=win, ori=0, name='Breaaak',
    text='BREAK\n',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
Continue = visual.TextStim(win=win, ori=0, name='Continue',
    text=u'Please press the spacebar to continue.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
Letter = visual.TextStim(win=win, ori=0, name='Letter',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.25, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)
fix = visual.TextStim(win=win, ori=0, name='fix',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "Thanx"
ThanxClock = core.Clock()
ThankYou = visual.TextStim(win=win, ori=0, name='ThankYou',
    text='This is the end of this task.\n\nThank you!',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


 

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "trial"-------
t = 0
trialClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
KeyInstr = event.BuilderKeyResponse()  # create an object of type KeyResponse
KeyInstr.status = NOT_STARTED
# keep track of which components have finished
trialComponents = []
trialComponents.append(ISI)
trialComponents.append(Instr)
trialComponents.append(KeyInstr)
for thisComponent in trialComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "trial"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instr* updates
    if t >= 0.0 and Instr.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr.tStart = t  # underestimates by a little under one frame
        Instr.frameNStart = frameN  # exact frame index
        Instr.setAutoDraw(True)
    elif Instr.status == STARTED and t >= (0.0 + (40-win.monitorFramePeriod*0.75)): #most of one frame period left
        Instr.setAutoDraw(False)
    
    # *KeyInstr* updates
    if t >= 0.0 and KeyInstr.status == NOT_STARTED:
        # keep track of start time/frame for later
        KeyInstr.tStart = t  # underestimates by a little under one frame
        KeyInstr.frameNStart = frameN  # exact frame index
        KeyInstr.status = STARTED
        # keyboard checking is just starting
        KeyInstr.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if KeyInstr.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            KeyInstr.keys = theseKeys[-1]  # just the last key pressed
            KeyInstr.rt = KeyInstr.clock.getTime()
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
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if KeyInstr.keys in ['', [], None]:  # No response was made
   KeyInstr.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('KeyInstr.keys',KeyInstr.keys)
if KeyInstr.keys != None:  # we had a response
    thisExp.addData('KeyInstr.rt', KeyInstr.rt)
thisExp.nextEntry()




#------Prepare to start Routine "Instr2"-------
t = 0
Instr2Clock.reset()  # clock 
frameN = -1
routineTimer.add(10.000000)
# update component parameters for each repeat
KeyInstr2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
KeyInstr2.status = NOT_STARTED
# keep track of which components have finished
Instr2Components = []
Instr2Components.append(text)
Instr2Components.append(KeyInstr2)
for thisComponent in Instr2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instr2"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Instr2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    elif text.status == STARTED and t >= (0.0 + (10.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        text.setAutoDraw(False)
    
    # *KeyInstr2* updates
    if t >= 0.0 and KeyInstr2.status == NOT_STARTED:
        # keep track of start time/frame for later
        KeyInstr2.tStart = t  # underestimates by a little under one frame
        KeyInstr2.frameNStart = frameN  # exact frame index
        KeyInstr2.status = STARTED
        # keyboard checking is just starting
        KeyInstr2.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    elif KeyInstr2.status == STARTED and t >= (0.0 + (10-win.monitorFramePeriod*0.75)): #most of one frame period left
        KeyInstr2.status = STOPPED
    if KeyInstr2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            KeyInstr2.keys = theseKeys[-1]  # just the last key pressed
            KeyInstr2.rt = KeyInstr2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Instr2"-------
for thisComponent in Instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if KeyInstr2.keys in ['', [], None]:  # No response was made
   KeyInstr2.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('KeyInstr2.keys',KeyInstr2.keys)
if KeyInstr2.keys != None:  # we had a response
    thisExp.addData('KeyInstr2.rt', KeyInstr2.rt)
thisExp.nextEntry()

#------Prepare to start Routine "InitFix"-------
t = 0
InitFixClock.reset()  # clock 
frameN = -1
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
InitFixComponents = []
InitFixComponents.append(text_2)
for thisComponent in InitFixComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "InitFix"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = InitFixClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    elif text_2.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InitFixComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "InitFix"-------
for thisComponent in InitFixComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# set up handler to look after randomisation of conditions etc



HITS=[]
HITSrt =[]
NOGOTRIALS=[]
FA=[]
FArt=[]
MISSES=[]


# set up handler to look after randomisation of conditions etc
GoNoGoLoop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('gonogo.xlsx'),
    seed=None, name='GoNoGoLoop')
thisExp.addLoop(GoNoGoLoop)  # add the loop to the experiment
thisGoNoGoLoop = GoNoGoLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisGoNoGoLoop.rgb)
if thisGoNoGoLoop != None:
    for paramName in thisGoNoGoLoop.keys():
        exec(paramName + '= thisGoNoGoLoop.' + paramName)

for thisGoNoGoLoop in GoNoGoLoop:
    currentLoop = GoNoGoLoop
    # abbreviate parameter names if possible (e.g. rgb = thisGoNoGoLoop.rgb)
    if thisGoNoGoLoop != None:
        for paramName in thisGoNoGoLoop.keys():
            exec(paramName + '= thisGoNoGoLoop.' + paramName)
    
    #------Prepare to start Routine "Trial"-------
    t = 0
    TrialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(ITI+.2)
    # update component parameters for each repeat
    Letter.setText(Letra)
    Resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Resp.status = NOT_STARTED
    # keep track of which components have finished
    TrialComponents = []
    TrialComponents.append(Letter)
    TrialComponents.append(Resp)
    TrialComponents.append(fix)
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
        
        # *Letter* updates
        if t >= 0.0 and Letter.status == NOT_STARTED:
            # keep track of start time/frame for later
            Letter.tStart = t  # underestimates by a little under one frame
            Letter.frameNStart = frameN  # exact frame index
            Letter.setAutoDraw(True)
        elif Letter.status == STARTED and t >= (0.0 + (.200-win.monitorFramePeriod*0.75)): #most of one frame period left
            Letter.setAutoDraw(False)
        
        # *Resp* updates
        if t >= 0.0 and Resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            Resp.tStart = t  # underestimates by a little under one frame
            Resp.frameNStart = frameN  # exact frame index
            Resp.status = STARTED
            # keyboard checking is just starting
            Resp.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif Resp.status == STARTED and t >= (0.0 + (.650-win.monitorFramePeriod*0.75)): #most of one frame period left
            Resp.status = STOPPED
        if Resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Resp.keys = theseKeys[-1]  # just the last key pressed
                Resp.rt = Resp.clock.getTime()
            if 'C'in Letra and len(theseKeys)>0:
                Resp.corr = 1
            if 'M'in Letra and len(theseKeys)>0:
                Resp.corr = 2
                

        
        # *fix* updates
        if t >= .650 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (.200 + (ITI-win.monitorFramePeriod*0.75)): #most of one frame period left
            fix.setAutoDraw(False)
        
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
    if Resp.keys in ['', [], None]:  # No response was made
       Resp.keys=None
    if 'C' in Letra and Resp.keys == None:
        Resp.corr = 3
    # store data for GoNoGoLoop (TrialHandler)
    GoNoGoLoop.addData('Resp.keys',Resp.keys)
    if Resp.keys != None:  # we had a response
        GoNoGoLoop.addData('Resp.rt', Resp.rt)
    thisExp.nextEntry()

    
    
    if 'C' in Letra and Resp.corr == 1:
        HITS.append(1)
        HITSrt.append(Resp.rt)
    if Resp.corr == 2:
        FA.append(1)
        FArt.append(Resp.rt)
    if Resp.corr == 3:
        MISSES.append(1)
    if 'M' in Letra:
        NOGOTRIALS.append(1)
        
# completed 1 repeats of 'GoNoGoLoop'


#------Prepare to start Routine "Break"-------
t = 0
BreakClock.reset()  # clock 
frameN = -1
routineTimer.add(30.000000)
# update component parameters for each repeat
KeyBreak3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
KeyBreak3.status = NOT_STARTED
# keep track of which components have finished
BreakComponents = []
BreakComponents.append(Breaaak)
BreakComponents.append(Continue)
BreakComponents.append(KeyBreak3)
for thisComponent in BreakComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Break"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = BreakClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Breaaak* updates
    if t >= 0.0 and Breaaak.status == NOT_STARTED:
        # keep track of start time/frame for later
        Breaaak.tStart = t  # underestimates by a little under one frame
        Breaaak.frameNStart = frameN  # exact frame index
        Breaaak.setAutoDraw(True)
    elif Breaaak.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        Breaaak.setAutoDraw(False)
    
    # *Continue* updates
    if t >= 2 and Continue.status == NOT_STARTED:
        # keep track of start time/frame for later
        Continue.tStart = t  # underestimates by a little under one frame
        Continue.frameNStart = frameN  # exact frame index
        Continue.setAutoDraw(True)
    elif Continue.status == STARTED and t >= (2 + (28.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        Continue.setAutoDraw(False)
    
    # *KeyBreak3* updates
    if t >= 2 and KeyBreak3.status == NOT_STARTED:
        # keep track of start time/frame for later
        KeyBreak3.tStart = t  # underestimates by a little under one frame
        KeyBreak3.frameNStart = frameN  # exact frame index
        KeyBreak3.status = STARTED
        # keyboard checking is just starting
        KeyBreak3.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    elif KeyBreak3.status == STARTED and t >= (2 + (28-win.monitorFramePeriod*0.75)): #most of one frame period left
        KeyBreak3.status = STOPPED
    if KeyBreak3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            if KeyBreak3.keys == []:  # then this was the first keypress
                KeyBreak3.keys = theseKeys[0]  # just the first key pressed
                KeyBreak3.rt = KeyBreak3.clock.getTime()
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

#-------Ending Routine "Break"-------
for thisComponent in BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if KeyBreak3.keys in ['', [], None]:  # No response was made
   KeyBreak3.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('KeyBreak3.keys',KeyBreak3.keys)
if KeyBreak3.keys != None:  # we had a response
    thisExp.addData('KeyBreak3.rt', KeyBreak3.rt)
thisExp.nextEntry()

#------Prepare to start Routine "InitFix"-------
t = 0
InitFixClock.reset()  # clock 
frameN = -1
routineTimer.add(3.4)
# update component parameters for each repeat
# keep track of which components have finished
InitFixComponents = []
InitFixComponents.append(text_2)
for thisComponent in InitFixComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "InitFix"-------
continueRoutine = True


while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = InitFixClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    elif text_2.status == STARTED and t >= (0.0 + (3.4-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InitFixComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "InitFix"-------
for thisComponent in InitFixComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)




# set up handler to look after randomisation of conditions etc */*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*
GoNoGoLoop2 = data.TrialHandler(nReps=1, method=u'random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('gonogo.xlsx'),
    seed=None, name='GoNoGoLoop2')
thisExp.addLoop(GoNoGoLoop2)  # add the loop to the experiment
thisGoNoGoLoop2 = GoNoGoLoop2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisGoNoGoLoop2.rgb)
if thisGoNoGoLoop2 != None:
    for paramName in thisGoNoGoLoop2.keys():
        exec(paramName + '= thisGoNoGoLoop2.' + paramName)

for thisGoNoGoLoop2 in GoNoGoLoop2:
    currentLoop = GoNoGoLoop2
    # abbreviate parameter names if possible (e.g. rgb = thisGoNoGoLoop2.rgb)
    if thisGoNoGoLoop2 != None:
        for paramName in thisGoNoGoLoop2.keys():
            exec(paramName + '= thisGoNoGoLoop2.' + paramName)
    
    #------Prepare to start Routine "Trial"-------
    t = 0
    TrialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(ITI+.200)
    # update component parameters for each repeat
    Letter.setText(Letra)
    Resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Resp.status = NOT_STARTED
    # keep track of which components have finished
    TrialComponents = []
    TrialComponents.append(Letter)
    TrialComponents.append(Resp)
    TrialComponents.append(fix)
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
        
        # *Letter* updates
        if t >= 0.0 and Letter.status == NOT_STARTED:
            # keep track of start time/frame for later
            Letter.tStart = t  # underestimates by a little under one frame
            Letter.frameNStart = frameN  # exact frame index
            Letter.setAutoDraw(True)
        elif Letter.status == STARTED and t >= (0.0 + (.200-win.monitorFramePeriod*0.75)): #most of one frame period left
            Letter.setAutoDraw(False)
        
        # *Resp* updates
        if t >= 0.0 and Resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            Resp.tStart = t  # underestimates by a little under one frame
            Resp.frameNStart = frameN  # exact frame index
            Resp.status = STARTED
            # keyboard checking is just starting
            Resp.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif Resp.status == STARTED and t >= (0.0 + (.650-win.monitorFramePeriod*0.75)): #most of one frame period left
            Resp.status = STOPPED
        if Resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Resp.keys = theseKeys[-1]  # just the last key pressed
                Resp.rt = Resp.clock.getTime()
            if 'C'in Letra and len(theseKeys)>0:
                Resp.corr = 1
            if 'M'in Letra and len(theseKeys)>0:
                Resp.corr = 2

        # *fix* updates
        if t >= .650 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (.200 + (ITI-win.monitorFramePeriod*0.75)): #most of one frame period left
            fix.setAutoDraw(False)
        
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
    if Resp.keys in ['', [], None]:  # No response was made
       Resp.keys=None
    if 'C'in Letra and Resp.keys == None:
        Resp.corr = 3
    # store data for GoNoGoLoop (TrialHandler)
    GoNoGoLoop.addData('Resp.keys',Resp.keys)
    if Resp.keys != None:  # we had a response
        GoNoGoLoop.addData('Resp.rt', Resp.rt)
    thisExp.nextEntry()
    
    if 'C' in Letra and Resp.corr == 1:
        HITS.append(1)
        HITSrt.append(Resp.rt)
    if Resp.corr == 2:
        FA.append(1)
        FArt.append(Resp.rt)
    if Resp.corr == 3:
        MISSES.append(1)
    if 'M' in Letra:
        NOGOTRIALS.append(1)
    
# completed 1 repeats of 'GoNoGoLoop2'


#------Prepare to start Routine "Break"-------
t = 0
BreakClock.reset()  # clock 
frameN = -1
routineTimer.add(30.000000)
# update component parameters for each repeat
KeyBreak3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
KeyBreak3.status = NOT_STARTED
# keep track of which components have finished
BreakComponents = []
BreakComponents.append(Breaaak)
BreakComponents.append(Continue)
BreakComponents.append(KeyBreak3)
for thisComponent in BreakComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Break"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = BreakClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Breaaak* updates
    if t >= 0.0 and Breaaak.status == NOT_STARTED:
        # keep track of start time/frame for later
        Breaaak.tStart = t  # underestimates by a little under one frame
        Breaaak.frameNStart = frameN  # exact frame index
        Breaaak.setAutoDraw(True)
    elif Breaaak.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        Breaaak.setAutoDraw(False)
    
    # *Continue* updates
    if t >= 2 and Continue.status == NOT_STARTED:
        # keep track of start time/frame for later
        Continue.tStart = t  # underestimates by a little under one frame
        Continue.frameNStart = frameN  # exact frame index
        Continue.setAutoDraw(True)
    elif Continue.status == STARTED and t >= (2 + (28.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        Continue.setAutoDraw(False)
    
    # *KeyBreak3* updates
    if t >= 2 and KeyBreak3.status == NOT_STARTED:
        # keep track of start time/frame for later
        KeyBreak3.tStart = t  # underestimates by a little under one frame
        KeyBreak3.frameNStart = frameN  # exact frame index
        KeyBreak3.status = STARTED
        # keyboard checking is just starting
        KeyBreak3.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    elif KeyBreak3.status == STARTED and t >= (2 + (28-win.monitorFramePeriod*0.75)): #most of one frame period left
        KeyBreak3.status = STOPPED
    if KeyBreak3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            if KeyBreak3.keys == []:  # then this was the first keypress
                KeyBreak3.keys = theseKeys[0]  # just the first key pressed
                KeyBreak3.rt = KeyBreak3.clock.getTime()
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

#-------Ending Routine "Break"-------
for thisComponent in BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if KeyBreak3.keys in ['', [], None]:  # No response was made
   KeyBreak3.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('KeyBreak3.keys',KeyBreak3.keys)
if KeyBreak3.keys != None:  # we had a response
    thisExp.addData('KeyBreak3.rt', KeyBreak3.rt)
thisExp.nextEntry()


#------Prepare to start Routine "InitFix"-------
t = 0
InitFixClock.reset()  # clock 
frameN = -1
routineTimer.add(3.4)
# update component parameters for each repeat
# keep track of which components have finished
InitFixComponents = []
InitFixComponents.append(text_2)
for thisComponent in InitFixComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "InitFix"-------
continueRoutine = True


while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = InitFixClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    elif text_2.status == STARTED and t >= (0.0 + (3.4-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InitFixComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "InitFix"-------
for thisComponent in InitFixComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)



# set up handler to look after randomisation of conditions etc */*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/**/
GoNoGoLoop3 = data.TrialHandler(nReps=1, method=u'random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('gonogo.xlsx'),
    seed=None, name='GoNoGoLoop3')
thisExp.addLoop(GoNoGoLoop3)  # add the loop to the experiment
thisGoNoGoLoop3 = GoNoGoLoop3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisGoNoGoLoop3.rgb)
if thisGoNoGoLoop3 != None:
    for paramName in thisGoNoGoLoop3.keys():
        exec(paramName + '= thisGoNoGoLoop3.' + paramName)

for thisGoNoGoLoop3 in GoNoGoLoop3:
    currentLoop = GoNoGoLoop3
    # abbreviate parameter names if possible (e.g. rgb = thisGoNoGoLoop3.rgb)
    if thisGoNoGoLoop3 != None:
        for paramName in thisGoNoGoLoop3.keys():
            exec(paramName + '= thisGoNoGoLoop3.' + paramName)
    
    #------Prepare to start Routine "Trial"-------
    t = 0
    TrialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(ITI+.200)
    # update component parameters for each repeat
    Letter.setText(Letra)
    Resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Resp.status = NOT_STARTED
    # keep track of which components have finished
    TrialComponents = []
    TrialComponents.append(Letter)
    TrialComponents.append(Resp)
    TrialComponents.append(fix)
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
        
        # *Letter* updates
        if t >= 0.0 and Letter.status == NOT_STARTED:
            # keep track of start time/frame for later
            Letter.tStart = t  # underestimates by a little under one frame
            Letter.frameNStart = frameN  # exact frame index
            Letter.setAutoDraw(True)
        elif Letter.status == STARTED and t >= (0.0 + (.200-win.monitorFramePeriod*0.75)): #most of one frame period left
            Letter.setAutoDraw(False)
        
        # *Resp* updates
        if t >= 0.0 and Resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            Resp.tStart = t  # underestimates by a little under one frame
            Resp.frameNStart = frameN  # exact frame index
            Resp.status = STARTED
            # keyboard checking is just starting
            Resp.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif Resp.status == STARTED and t >= (0.0 + (.650-win.monitorFramePeriod*0.75)): #most of one frame period left
            Resp.status = STOPPED
        if Resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Resp.keys = theseKeys[-1]  # just the last key pressed
                Resp.rt = Resp.clock.getTime()
            if 'C'in Letra and len(theseKeys)>0:
                Resp.corr = 1
            if 'M'in Letra and len(theseKeys)>0:
                Resp.corr = 2
                

        
        # *fix* updates
        if t >= .650 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (.200 + (ITI-win.monitorFramePeriod*0.75)): #most of one frame period left
            fix.setAutoDraw(False)
        
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
    if Resp.keys in ['', [], None]:  # No response was made
       Resp.keys=None
    if 'C'in Letra and Resp.keys == None:
        Resp.corr = 3
    # store data for GoNoGoLoop (TrialHandler)
    GoNoGoLoop.addData('Resp.keys',Resp.keys)
    if Resp.keys != None:  # we had a response
        GoNoGoLoop.addData('Resp.rt', Resp.rt)
    thisExp.nextEntry()
    
    if 'C' in Letra and Resp.corr == 1:
        HITS.append(1)
        HITSrt.append(Resp.rt)
    if Resp.corr == 2:
        FA.append(1)
        FArt.append(Resp.rt)
    if Resp.corr == 3:
        MISSES.append(1)
    if 'M' in Letra:
        NOGOTRIALS.append(1)
# completed 1 repeats of 'GoNoGoLoop3'


#------Prepare to start Routine "Break"-------
t = 0
BreakClock.reset()  # clock 
frameN = -1
routineTimer.add(30.000000)
# update component parameters for each repeat
KeyBreak3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
KeyBreak3.status = NOT_STARTED
# keep track of which components have finished
BreakComponents = []
BreakComponents.append(Breaaak)
BreakComponents.append(Continue)
BreakComponents.append(KeyBreak3)
for thisComponent in BreakComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Break"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = BreakClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Breaaak* updates
    if t >= 0.0 and Breaaak.status == NOT_STARTED:
        # keep track of start time/frame for later
        Breaaak.tStart = t  # underestimates by a little under one frame
        Breaaak.frameNStart = frameN  # exact frame index
        Breaaak.setAutoDraw(True)
    elif Breaaak.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        Breaaak.setAutoDraw(False)
    
    # *Continue* updates
    if t >= 2 and Continue.status == NOT_STARTED:
        # keep track of start time/frame for later
        Continue.tStart = t  # underestimates by a little under one frame
        Continue.frameNStart = frameN  # exact frame index
        Continue.setAutoDraw(True)
    elif Continue.status == STARTED and t >= (2 + (28.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        Continue.setAutoDraw(False)
    
    # *KeyBreak3* updates
    if t >= 2 and KeyBreak3.status == NOT_STARTED:
        # keep track of start time/frame for later
        KeyBreak3.tStart = t  # underestimates by a little under one frame
        KeyBreak3.frameNStart = frameN  # exact frame index
        KeyBreak3.status = STARTED
        # keyboard checking is just starting
        KeyBreak3.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    elif KeyBreak3.status == STARTED and t >= (2 + (28-win.monitorFramePeriod*0.75)): #most of one frame period left
        KeyBreak3.status = STOPPED
    if KeyBreak3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            if KeyBreak3.keys == []:  # then this was the first keypress
                KeyBreak3.keys = theseKeys[0]  # just the first key pressed
                KeyBreak3.rt = KeyBreak3.clock.getTime()
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

#-------Ending Routine "Break"-------
for thisComponent in BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if KeyBreak3.keys in ['', [], None]:  # No response was made
   KeyBreak3.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('KeyBreak3.keys',KeyBreak3.keys)
if KeyBreak3.keys != None:  # we had a response
    thisExp.addData('KeyBreak3.rt', KeyBreak3.rt)
thisExp.nextEntry()

#------Prepare to start Routine "InitFix"-------
t = 0
InitFixClock.reset()  # clock 
frameN = -1
routineTimer.add(3.4)
# update component parameters for each repeat
# keep track of which components have finished
InitFixComponents = []
InitFixComponents.append(text_2)
for thisComponent in InitFixComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "InitFix"-------
continueRoutine = True


while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = InitFixClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    elif text_2.status == STARTED and t >= (0.0 + (3.4-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InitFixComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "InitFix"-------
for thisComponent in InitFixComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)



# set up handler to look after randomisation of conditions etc */*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*
GoNoGoLoop4 = data.TrialHandler(nReps=1, method=u'random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('gonogo.xlsx'),
    seed=None, name='GoNoGoLoop4')
thisExp.addLoop(GoNoGoLoop4)  # add the loop to the experiment
thisGoNoGoLoop4 = GoNoGoLoop4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisGoNoGoLoop4.rgb)
if thisGoNoGoLoop4 != None:
    for paramName in thisGoNoGoLoop4.keys():
        exec(paramName + '= thisGoNoGoLoop4.' + paramName)

for thisGoNoGoLoop4 in GoNoGoLoop4:
    currentLoop = GoNoGoLoop4
    # abbreviate parameter names if possible (e.g. rgb = thisGoNoGoLoop4.rgb)
    if thisGoNoGoLoop4 != None:
        for paramName in thisGoNoGoLoop4.keys():
            exec(paramName + '= thisGoNoGoLoop4.' + paramName)
    
    #------Prepare to start Routine "Trial"-------
    t = 0
    TrialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(ITI+.200)
    # update component parameters for each repeat
    Letter.setText(Letra)
    Resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Resp.status = NOT_STARTED
    # keep track of which components have finished
    TrialComponents = []
    TrialComponents.append(Letter)
    TrialComponents.append(Resp)
    TrialComponents.append(fix)
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
        
        # *Letter* updates
        if t >= 0.0 and Letter.status == NOT_STARTED:
            # keep track of start time/frame for later
            Letter.tStart = t  # underestimates by a little under one frame
            Letter.frameNStart = frameN  # exact frame index
            Letter.setAutoDraw(True)
        elif Letter.status == STARTED and t >= (0.0 + (.200-win.monitorFramePeriod*0.75)): #most of one frame period left
            Letter.setAutoDraw(False)
        
        # *Resp* updates
        if t >= 0.0 and Resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            Resp.tStart = t  # underestimates by a little under one frame
            Resp.frameNStart = frameN  # exact frame index
            Resp.status = STARTED
            # keyboard checking is just starting
            Resp.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif Resp.status == STARTED and t >= (0.0 + (.650-win.monitorFramePeriod*0.75)): #most of one frame period left
            Resp.status = STOPPED
        if Resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Resp.keys = theseKeys[-1]  # just the last key pressed
                Resp.rt = Resp.clock.getTime()
            if 'C'in Letra and len(theseKeys)>0:
                Resp.corr = 1
            if 'M'in Letra and len(theseKeys)>0:
                Resp.corr = 2
                

        # *fix* updates
        if t >= .650 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (.200 + (ITI-win.monitorFramePeriod*0.75)): #most of one frame period left
            fix.setAutoDraw(False)
        
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
    if Resp.keys in ['', [], None]:  # No response was made
       Resp.keys=None
    if 'C'in Letra and Resp.keys == None:
        Resp.corr = 3
    # store data for GoNoGoLoop (TrialHandler)
    GoNoGoLoop.addData('Resp.keys',Resp.keys)
    if Resp.keys != None:  # we had a response
        GoNoGoLoop.addData('Resp.rt', Resp.rt)
    thisExp.nextEntry()

    if 'C' in Letra and Resp.corr == 1:
        HITS.append(1)
        HITSrt.append(Resp.rt)
    if Resp.corr == 2:
        FA.append(1)
        FArt.append(Resp.rt)
    if Resp.corr == 3:
        MISSES.append(1)
    if 'M' in Letra:
        NOGOTRIALS.append(1)
    
# completed 1 repeats of 'GoNoGoLoop4'


#------Prepare to start Routine "Break"-------
t = 0
BreakClock.reset()  # clock 
frameN = -1
routineTimer.add(30.000000)
# update component parameters for each repeat
KeyBreak3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
KeyBreak3.status = NOT_STARTED
# keep track of which components have finished
BreakComponents = []
BreakComponents.append(Breaaak)
BreakComponents.append(Continue)
BreakComponents.append(KeyBreak3)
for thisComponent in BreakComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Break"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = BreakClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Breaaak* updates
    if t >= 0.0 and Breaaak.status == NOT_STARTED:
        # keep track of start time/frame for later
        Breaaak.tStart = t  # underestimates by a little under one frame
        Breaaak.frameNStart = frameN  # exact frame index
        Breaaak.setAutoDraw(True)
    elif Breaaak.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        Breaaak.setAutoDraw(False)
    
    # *Continue* updates
    if t >= 2 and Continue.status == NOT_STARTED:
        # keep track of start time/frame for later
        Continue.tStart = t  # underestimates by a little under one frame
        Continue.frameNStart = frameN  # exact frame index
        Continue.setAutoDraw(True)
    elif Continue.status == STARTED and t >= (2 + (28.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        Continue.setAutoDraw(False)
    
    # *KeyBreak3* updates
    if t >= 2 and KeyBreak3.status == NOT_STARTED:
        # keep track of start time/frame for later
        KeyBreak3.tStart = t  # underestimates by a little under one frame
        KeyBreak3.frameNStart = frameN  # exact frame index
        KeyBreak3.status = STARTED
        # keyboard checking is just starting
        KeyBreak3.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    elif KeyBreak3.status == STARTED and t >= (2 + (28-win.monitorFramePeriod*0.75)): #most of one frame period left
        KeyBreak3.status = STOPPED
    if KeyBreak3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            if KeyBreak3.keys == []:  # then this was the first keypress
                KeyBreak3.keys = theseKeys[0]  # just the first key pressed
                KeyBreak3.rt = KeyBreak3.clock.getTime()
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

#-------Ending Routine "Break"-------
for thisComponent in BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if KeyBreak3.keys in ['', [], None]:  # No response was made
   KeyBreak3.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('KeyBreak3.keys',KeyBreak3.keys)
if KeyBreak3.keys != None:  # we had a response
    thisExp.addData('KeyBreak3.rt', KeyBreak3.rt)
thisExp.nextEntry()

#------Prepare to start Routine "InitFix"-------
t = 0
InitFixClock.reset()  # clock 
frameN = -1
routineTimer.add(3.4)
# update component parameters for each repeat
# keep track of which components have finished
InitFixComponents = []
InitFixComponents.append(text_2)
for thisComponent in InitFixComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "InitFix"-------
continueRoutine = True


while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = InitFixClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    elif text_2.status == STARTED and t >= (0.0 + (3.4-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InitFixComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "InitFix"-------
for thisComponent in InitFixComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)



# set up handler to look after randomisation of conditions etc */*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
GoNoGoLoop5 = data.TrialHandler(nReps=1, method=u'random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('gonogo.xlsx'),
    seed=None, name='GoNoGoLoop5')
thisExp.addLoop(GoNoGoLoop5)  # add the loop to the experiment
thisGoNoGoLoop5 = GoNoGoLoop5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisGoNoGoLoop5.rgb)
if thisGoNoGoLoop5 != None:
    for paramName in thisGoNoGoLoop5.keys():
        exec(paramName + '= thisGoNoGoLoop5.' + paramName)

for thisGoNoGoLoop5 in GoNoGoLoop5:
    currentLoop = GoNoGoLoop5
    # abbreviate parameter names if possible (e.g. rgb = thisGoNoGoLoop5.rgb)
    if thisGoNoGoLoop5 != None:
        for paramName in thisGoNoGoLoop5.keys():
            exec(paramName + '= thisGoNoGoLoop5.' + paramName)
    
    #------Prepare to start Routine "Trial"-------
    t = 0
    TrialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(ITI+.200)
    # update component parameters for each repeat
    Letter.setText(Letra)
    Resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Resp.status = NOT_STARTED
    # keep track of which components have finished
    TrialComponents = []
    TrialComponents.append(Letter)
    TrialComponents.append(Resp)
    TrialComponents.append(fix)
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
        
        # *Letter* updates
        if t >= 0.0 and Letter.status == NOT_STARTED:
            # keep track of start time/frame for later
            Letter.tStart = t  # underestimates by a little under one frame
            Letter.frameNStart = frameN  # exact frame index
            Letter.setAutoDraw(True)
        elif Letter.status == STARTED and t >= (0.0 + (.200-win.monitorFramePeriod*0.75)): #most of one frame period left
            Letter.setAutoDraw(False)
        
        # *Resp* updates
        if t >= 0.0 and Resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            Resp.tStart = t  # underestimates by a little under one frame
            Resp.frameNStart = frameN  # exact frame index
            Resp.status = STARTED
            # keyboard checking is just starting
            Resp.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif Resp.status == STARTED and t >= (0.0 + (.650-win.monitorFramePeriod*0.75)): #most of one frame period left
            Resp.status = STOPPED
        if Resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Resp.keys = theseKeys[-1]  # just the last key pressed
                Resp.rt = Resp.clock.getTime()
            if 'C'in Letra and len(theseKeys)>0:
                Resp.corr = 1
            if 'M'in Letra and len(theseKeys)>0:
                Resp.corr = 2
                

        
        # *fix* updates
        if t >= .650 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (.200 + (ITI-win.monitorFramePeriod*0.75)): #most of one frame period left
            fix.setAutoDraw(False)
        
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
    if Resp.keys in ['', [], None]:  # No response was made
       Resp.keys=None
    if 'C'in Letra and Resp.keys == None:
        Resp.corr = 3
    # store data for GoNoGoLoop (TrialHandler)
    GoNoGoLoop.addData('Resp.keys',Resp.keys)
    if Resp.keys != None:  # we had a response
        GoNoGoLoop.addData('Resp.rt', Resp.rt)
    thisExp.nextEntry()
    
    if 'C' in Letra and Resp.corr == 1:
        HITS.append(1)
        HITSrt.append(Resp.rt)
    if Resp.corr == 2:
        FA.append(1)
        FArt.append(Resp.rt)
    if Resp.corr == 3:
        MISSES.append(1)
    if 'M' in Letra:
        NOGOTRIALS.append(1)
    
# completed 1 repeats of 'GoNoGoLoop5'




#==============================================================
# Saving of data   THIS IS FOR THE .PRT FILE NEEDED IN BRAIN VOYAGER!!!
#==============================================================

AverageHITSrt = (sum(HITSrt)/(len(HITSrt)+.0001))
AverageFArt = (sum(FArt)/(len(FArt)+.001))

#compose prt files #AATrun2
header = \
'FileVersion: \n' + \
'ResolutionOfTime: Volumes\n' + \
'Experiment:  GoNoGo1 \n' + \
'BackgroundColor: 0 0 0\n' + \
'TextColor:   255 255 217\n' + \
'TimeCourseColor: 255 255 255\n' + \
'TimeCourseThick: 3\n' + \
'ReferenceFuncColor:  255 255 51\n' + \
'ReferenceFuncThick:  2\n' + \
'ParametricWeights:  0\n' + \
'NrOfConditions:  7\n'

output = open (prtFile + '.prt', 'w')
output.write(header)
for name,list in zip(
        ['HITS','HITSrt','NOGOTRIALS','FA','FArt','MISSES'],
        [HITS,HITSrt,NOGOTRIALS,FA,FArt,MISSES],):
    output.write('\n' + \
    name + '\n' + 'Freq: ' +
    str(len(list)) + '\n' )
    for x in list:
        output.write(str(x) + '\n')         
output.write('\n' + 'HITSrt: ' + str(AverageHITSrt))
output.write('\n' + 'FArt: ' + str(AverageFArt))
output.close()


#------Prepare to start Routine "Thanx"-------
t = 0
ThanxClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
ThanxComponents = []
ThanxComponents.append(ThankYou)
for thisComponent in ThanxComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Thanx"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ThanxClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ThankYou* updates
    if t >= 0.0 and ThankYou.status == NOT_STARTED:
        # keep track of start time/frame for later
        ThankYou.tStart = t  # underestimates by a little under one frame
        ThankYou.frameNStart = frameN  # exact frame index
        ThankYou.setAutoDraw(True)
    elif ThankYou.status == STARTED and t >= (0.0 + (5-win.monitorFramePeriod*0.75)): #most of one frame period left
        ThankYou.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThanxComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Thanx"-------
for thisComponent in ThanxComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)




win.close()
core.quit()
