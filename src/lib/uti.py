# -*- coding: latin-1 -*-
from geralclass import *

class OxygenContent (MedCalc):
	def __init__ (self):
		self.data = [(u'Hemoglobina (g/dl)','number',0),(u'Sa02 (%)','number',0),(u'Pa02 (torr)','number',0)]
		
	def show (self):
		Hgb = self.getform()[0][2]
		SaO2 = self.getform()[1][2]
		PaO2 = self.getform()[2][2]
		CaO2 = 1.36 * Hgb *	SaO2/100 + 0.0031 * PaO2
		appuifw.note(u"CaO2 = %.2f"%CaO2,"info")			
		
class SatO2 (MedCalc):
	def __init__ (self):
		self.data = [(u'pO2 - Entrada','number',0)]
		
	def show (self):
		pO2 = self.getform()[0][2]
		SO2 = (23400.0 * (pO2**3 + 150 * pO2)**(-1) + 1)**(-1)
		appuifw.note(u"Sat. O2 = %.2f"%SO2,"info")			

class OsmSerica (MedCalc):
	def __init__ (self):
		self.data = [(u'Na (mEq/L)','number',0),(u'Glucose (mg/dL)','number',0),(u'BUN (mg/dL)','number',0)]
		
	def show (self):
		Na  = self.getform()[0][2]
		Glu = self.getform()[1][2]
		BUN = self.getform()[2][2]
		Osmolality = 2 * Na + Glu / 18 + BUN / 2.8
		appuifw.note(u"Osmolaridade Sérica = %.2f"%Osmolality,"info")		
		
class VentIndex(MedCalc):
	def __init__ (self):
		self.data = [(u'Ritmo Resp. Vent. (bpm)','number',0),(u'Pico Pressão Insp.(torr)','number',0),(u'PEEP (torr)','number',0),(u'PaCO2 (torr)','number',0)]

	def show (self):
		RR = self.getform()[0][2]
		PIP = self.getform()[1][2]
		PEEP = self.getform()[2][2]
		PaCO2 = self.getform()[3][2]
		VI = (RR * (PIP - PEEP) * PaCO2)/1000.0
		appuifw.note(u"Indice Ventilação %.2f"%VI,'info')

class AaGrad (MedCalc):
	def __init__ (self):
		self.data = [(u'In FiO2 (dec)','number',0),(u'In PaC02 (torr)','number',0),(u'In Pa02 (torr)','number',0)]
		
	def show (self):
		PAO2 = self.getform()[0][2]*(760-47) - self.getform()[1][2]/0.8
		PAO2 -= self.getform()[2][2]
		appuifw.note(u"Gradiente Arterial Alveolar = %.2f"%PAO2,"info")
		
class Bicarb (MedCalc):
	def __init__ (self):
		self.data = [(u'Valor pH','number',0),(u'Valor PaC02','number',0)]
		
	def show (self):
		pH = self.getform()[0][2]
		pCO2 = self.getform()[1][2]
		HCO3 = 0.03 * pCO2 * 10 ** (pH - 6.1)
		BE = 0.02786 * pCO2 * 10 ** (pH - 6.1) + 13.77 * pH - 124.58
		appuifw.note(u"HCO3 = %.2f\nDesbalanceamento Base: %.2f"%(HCO3,BE),"info")	
