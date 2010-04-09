# -*- coding: latin-1 -*-
# ###########################################################
#           Teste Neuro                                     #
# ###########################################################
from geralclass import *
'''
The Abbreviated Mental Test can be used to quickly test the cognitive function in elderly patients. This is also referred to as the Hodkinson's Mental Test Score.
Item Score (each one point)
age, time to the nearest hour, year, name of place, recognition of 2 persons, birthday (date and month), date of World War I, name of your country's President, able to count from 20 to 1 backwards, address - 42 West Street, 
Interpretation: • minimum score: 0, • maximum score: 10
• A higher score indicates greater cognitive function. • A score of 6 is used as the cutoff to separate normal elderly persons from those who are confused or demented with a correct assignment of 81.5%.
'''
class AbbreviatedMentalTest (MedCalcList):
	def __init__ (self):
		self.data = [u'idade',u'minutos para próxima hora',u'nome do lugar',u'reconhecer 2 pessoas',u'data 1a guerra',u'presidente da república',u'conta 20 a 1?',u'endereço',u'aniversário',u'ano em que estamos']
		
	def show (self):
		soma = 0
		for i in self._f: soma += 1
		if soma > 6:
			appuifw.note(u"Pontos %d- Não demenciado"%soma,"info")
		else:
			appuifw.note(u"Pontos %d- Demenciado"%soma,"info")


class GCS (MedCalc):
	def __init__ (self):
		self.Eye   = [u'Espontaneamente',u'Estímulo Verbal',u'A dor',u'nunca']
		self.Lang  = [u'orientado e falando',u'desorientado e falando',u'palavras confusas',u'sons incompreensiveis',u'sem resposta']
		self.Motor = [u'Obedece comandos', u'Localiza a dor', u'flexão normal', u'flexão anormal', u'extensão', u'sem resposta']
		self.data = [(u'Olhos', 'combo', ( self.Eye, 0 )),(u'Verbal', 'combo', ( self.Lang, 0 )),(u'Motor', 'combo', ( self.Motor, 0 ))]
	
	def show (self):
		def prob(i):
			if i > 10: return 82
			if i > 7:  return 68
			if i > 4:  return 34
			return 7
		E = self.getform()[0][2][1]	
		L = self.getform()[1][2][1]
		M = self.getform()[2][2][1]
		GCS = 4 - E + 5 - L + 6 - M
		appuifw.note(u"GCS = %d\nProb. recuperação: %d%%"%(GCS,prob(GCS)), "info")
		
class NINDS3 (MedCalc):
	def __init__ (self):
		self.volume   = [u'<= 14.1 mL',u'> 14.1 mL']
		self.nihss = [u' <= 3', u'4 a 15', u'> 15']
		self.horas  = [u'<= 3 horas',u'3 a 6 horas',u'> 6 horas']
		self.data = [(u'Volume da lesão MR-DWI', 'combo', ( self.volume, 0 )),(u'NIHSS score', 'combo', ( self.nihss, 0 )),(u'Tempo em horas desde o começo','combo', ( self.horas, 0 ))]
	
	def show (self):
		def prob(i):
			if i < 3: return "Baixa"
			if i < 5:  return "Média"
			return "Alta"
		V = self.getform()[0][2][1]	
		N = self.getform()[1][2][1]
		H = self.getform()[2][2][1]
		ninds3 = 1 - V + 4 - 2*N + H
		appuifw.note(u"NINDS3 = %d\nProb. recuperação: %s"%(ninds3,prob(ninds3)), "info")
		
class Zung (MedCalc):
	def __init__(self):
		alist = [u'Poucas Vezes',u'Algumas Vezes',u'Boa Parte das Vezes',u'Quase Sempre']
		self.data = [
(u'Sinto desanimo e tristeza?','combo',(alist,0)),
(u'Sinto melhor de manhã?','combo',(alist,0)),
(u'Choro ou tenho vontade?','combo',(alist,0)),
(u'Problemas para dormir?','combo',(alist,0)),
(u'Como o habitual?','combo',(alist,0)),
(u'Vida sexual normal?','combo',(alist,0)),
(u'Estou perdendo peso?','combo',(alist,0)),
(u'Problemas de constipação?','combo',(alist,0)),
(u'Coração batendo mais acelerado?','combo',(alist,0)),
(u'Cansado sem razão?','combo',(alist,0)),
(u'Pensamento claro como de costume?','combo',(alist,0)),
(u'É fácil fazer o que estou acostumado?','combo',(alist,0)),
(u'Sinto-me inquieto?','combo',(alist,0)),
(u'Sinto-me esperançoso com relação ao futuro?','combo',(alist,0)),
(u'Mais irritável que o usual?','combo',(alist,0)),
(u'É fácil tomar decisões?','combo',(alist,0)),
(u'Sinto-me útil e necessário?','combo',(alist,0)),
(u'Minha vida está plena?','combo',(alist,0)),
(u'Sinto que os outros estariam melhor com eu morto?','combo',(alist,0)),
(u'Gosto das coisas que costumava gostar?','combo',(alist,0))
]
	def show (self):
		def prob(i,j):
			if i%2 == 1: return 4 - j
			else: return 1 + j
		def diag(i):
			if i < 36: return "Normal"
			if i < 57: return "Limiar"
			return "Limiar"
		f = self.getform()	
		ZNG = 0
		for i in range(20):
			ZNG += prob (i,f[i][2][1])
		appuifw.note(u"Zung = %d\nProvavelmente:%s"%(ZNG,diag(GCS)), "info")

class Hachinski (MedCalcList):
	def __init__ (self):
		self.data = [
		u'stepwise deterioration',
		u'fluctuating course',
		u'nocturnal confusion',
		u'relative preservation of personality',
		u'depression',
		u'somatic complaints',
		u'emotional incontinence',
		u'history of hypertension',
		u'history of strokes',
		u'evidence of associated atherosclerosis',
		u'focal neurological symptoms',
		u'focal neurological signs']
		self.pontos = [2,1,2,1,1,1,1,1,1,2,1,2,2]
		
	def show (self):
		soma = 0
		for i in self._f: soma += self.pontos[i]
		if soma > 7:
			appuifw.note(u"Pontos %d- demencia vascular "%soma,"info")
		if soma < 4:
			appuifw.note(u"Pontos %d- Demencia Primária"%soma,"info")
		if soma > 3 and soma < 8:
			appuifw.note(u"Pontos %d- Limiar / Mixed"%soma,"info")

def show_dummy (texto):
	t = appuifw.Text()
	appuifw.app.body = t
	t.color = 0xFF00FF
	t.font = (u"Nokia Hindi S60", 14, None)
	t.add(u"Resultado - Novo Estilo\n")
	t.font = (u"Nokia Hindi S60", 12, None)
	t.add(u"Diga o que achou deste estilo...\n")
	t.color = 0xFF0000
	t.add(texto)

			
class CHADS2 (MedCalcList):
	def __init__ (self):
		self.data = [
		u'Historico de ICC',
		u'Hipertensão',
		u'Mais de 75 anos',
		u'Diabete mellitus',
		u'Histórico de AVC ou TIA'
		]
		self.pontos = [1,1,1,1,2]
		self.rate = [
		(0,1.9,u"1.2 a 3.0"),
		(1,2.8,u"2.0 a 3.8"),
		(2,4.0,u"3.1 a 5.1"),
		(3,5.9,u"4.6 a 7.3"),
		(4,8.5,u"6.3 a 11.1"),
		(5,12.5,u"8.2 a 17.5"),
		(6,18.2,u"10.5 a 27.4")]
	
	def show (self):
		soma = 0
		for i in self._f: soma += self.pontos[i]
		rt = self.rate[soma]
		print rt
		msg = u"%d Pontos\nProb AVC: %.1f%%\n(%s)"%(rt[0],rt[1],rt[2])
		print msg
		#appuifw.note(msg,"info")
		show_dummy(msg)