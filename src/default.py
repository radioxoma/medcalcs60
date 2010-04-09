# -*- coding: latin-1 -*-
# Medic Calculator
#
# Ref: http://www-users.med.cornell.edu/~spon/picu/calc/index.htm
# Ref: http://www.medcalc.com/
# Ref: http://www.medal.org/
#
#ensymble_python2.5-0.27.py py2sis --appname=medcalc --version=0.4.1 -l EN -t H:\S60\devices\S60_3rd_FP2_SDK_v1.1\epoc32\winscw\c\python\disclaimer.txt --icon=H:\S60\devices\S60_3rd_FP2_SDK_v1.1\epoc32\winscw\c\python\logo2.svg --extrasdir=python --caption="Medic Calc" --shortcaption="Med Calc" --vendor="NF.org" H:\S60\devices\S60_3rd_FP2_SDK_v1.1\epoc32\winscw\c\python medcalc
#ensymble.py mergesis  medcalc.sis PythonForS60_1_4_5_3rdEd.SIS medcalc_standalone_v1_0_0.sis
#H:/S60/devices/S60_3rd_FP2_SDK_v1.1/epoc32/winscw/c/python/
#-l EN -t H:\S60\devices\S60_3rd_FP2_SDK_v1.1\epoc32\winscw\c\python\disclaimer.appuifwtxt --icon=H:\S60\devices\S60_3rd_FP2_SDK_v1.1\epoc32\winscw\c\python\logo2.svg --extrasdir=python --caption="Medic Calc" --shortcaption=MedCalc --vendor="NF.org" 
def to_unicode():
    return lambda x:x.encode('utf-8')
import sys
from e32 import in_emulator
if in_emulator():
    sys.path.append('c:/data/python/')

# install only in memory phone
sys.path.append(u"c:\\data\\python\\medcalc\\")

import os
import e32, graphics
from audio import say

from geralclass import *
from geral import *
from neuro import *
from uti import *
from rx import *

# Level 1 Menu
        
class MenuGeral (MenuFilho):
    def __init__(self):
        self.Children = [u"BSA",u"BMI",u"BEE"]
        #self.Children = [u"BSA",u"BMI",u"BEE",u"Risco Cirúrgico"]
        self.Title = u"Geral"
        self.MenuKid = [BSA(),BMI(),BEE()]
        #self.MenuKid = [BSA(),BMI(),BEE(),AnestesiaRisk()]
        
class MenuNeuro (MenuFilho):
    def __init__(self):
        self.Children = [u"Glasgow CS",u'Teste Mental Abreviado',u'Zung Depressão',u'NINDS 3-Item',u'Hachinski Indice Isquemico',u'CHADS2 - AVC/AFib']
        self.Title = u"Neuro"
        self.MenuKid = [GCS(),AbbreviatedMentalTest(),Zung(),NINDS3(),Hachinski(),CHADS2()]
        
class MenuUTI (MenuFilho):
    def __init__(self):
        self.Children = [u"Gradiente Arterial Alveolar",u"Bicarbonato e base excesso ",u"Indíce de Ventilação", u"Osmolaridade Sérica",u"Quantidade Oxigênio",u"Saturação Oxigênio"]
        self.Title = u"UTI"
        self.MenuKid = [AaGrad(),Bicarb(),VentIndex(),OsmSerica(),OxygenContent(),SatO2()]	

class MenuRX (MenuFilho):
    def __init__(self):
        self.Children = [u"Raio-X Torax PA",u"Raio-X Torax Lat",u"Raio-X Torax PA (F)",u"Raio-X Pneumonia",u"Outro Raio-X Pneumonia",u"Raio-X Antrax",u"Raio-X Marfan",u"Raio-X Câncer"]
        self.Title = u"RX"
        self.MenuKid = [RxTorax(),RxToraxLat(),RxToraxFem(),RxToraxPneumonia(),RxToraxPneumonia2(),RxToraxAntrax(),RxMarfan(),RxCancer()]
        
class MRI (MenuFilho):
    def __init__(self):
        self.Children = []
        self.Title = u"MRI"
        self.MenuKid = []


class MenuStruct:
    def __init__(self):
        self.script_lock = e32.Ao_lock()	
        self.Parent = None
        self.Children = [u"Geral",u"Neuro",u"UTI",u"RX"]
        self.MenuKid = [MenuGeral(),MenuNeuro(),MenuUTI(),MenuRX()]
    
    def run(self):
        from key_codes import EKeyLeftArrow
        self.lb = appuifw.Listbox(self.Children, self.lbox_observe)
        self.lb.bind(EKeyLeftArrow, lambda: self.lbox_observe(0))
        old_title = appuifw.app.title
        self.refresh()
        self.script_lock.wait()
        appuifw.app.title = old_title
        appuifw.app.body = None
        self.lb = None
        
    def refresh(self):
        appuifw.app.title = u"Medical"
        appuifw.app.menu = []
        appuifw.app.exit_key_handler = self.exit_key_handler
        appuifw.app.body = self.lb

    def do_exit(self):
        self.exit_key_handler()

    def exit_key_handler(self):
        appuifw.app.exit_key_handler = None
        self.script_lock.signal()
        sys.exit()
        
    def lbox_observe(self, ind = None):
        if not ind == None:
            index = ind
        else:
            index = self.lb.current()
        focused_item = 0
        self.MenuKid[index].run(self)
        appuifw.app.screen='normal'
    
    def back(self):
        pass	
        
def splash ():
    
    possible_locations = ["E:\\python\\logo.png", "C:\\data\\python\\medcalc\\logo.png", "logo.png"]
    possible_locations.append(os.path.join(sys.path[0], "logo.png"))
    appuifw.app.screen='full' #(a full screen)
    for location in possible_locations:
        if os.path.exists(location):
            try:
                img1 = graphics.Image.open(location)
            except:
                print "Error"
    def handle_redraw(rect): canvas.blit(img1)                
    canvas=appuifw.Canvas(event_callback=None, redraw_callback=handle_redraw)
    canvas.blit(img1)
    appuifw.app.body=canvas
    e32.ao_sleep(3)
    appuifw.app.screen='normal' #(a full screen)
    
try:
    splash()
    MenuStruct().run()
except Exception, e:
    import appuifw
    import traceback
    import sys

    e1,e2,e3 = sys.exc_info()
    err_msg = unicode(repr(e)) + u"\u2029"*2
    err_msg += u"Call stack:\u2029" + unicode(traceback.format_exception(e1,e2,e3))
    lock = e32.Ao_lock()      

    appuifw.app.body = appuifw.Text(err_msg)
    appuifw.app.menu = [(u"Exit", lambda: lock.signal())]
    appuifw.app.title = u"Error log"
    lock.wait()
