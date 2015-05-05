#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import with_statement


from medcalc.geralclass import *


CATEGORY = _(u"Neuro")


class AbbreviatedMentalTest(MedCalcList):
    """Abbreviated mental test score.

    The Abbreviated Mental Test can be used to quickly test the cognitive
    function in elderly patients.

    * A higher score indicates greater cognitive function.
    * A score of 6 is used as the cutoff to separate normal elderly persons
        from those who are confused or demented with a correct assignment of 81.5%.

    https://en.wikipedia.org/wiki/Abbreviated_mental_test_score
    """
    def __init__(self):
        super(AbbreviatedMentalTest, self).__init__()
        self.category = CATEGORY
        self.name = _(u'Teste Mental Abreviado')
        self.data = [
            _(u'Idade'),
            _(u'Minutos para próxima hora'),
            _(u'Nome do lugar'),
            _(u'Reconhecer 2 pessoas'),
            _(u'Data 1a guerra'),
            _(u'Presidente da república'),
            _(u'Conta 20 a 1?'),
            _(u'Endereço'),
            _(u'Aniversário'),
            _(u'Ano em que estamos')]

    def show(self):
        soma = 0
        for i in self._f:
            soma += 1
        if soma > 6:
            self.notify(_(u"Pontos %d- Não demenciado" % soma))
        else:
            self.notify(_(u"Pontos %d- Demenciado 81.5 %%" % soma))


class GCS(MedCalc):
    """Glasgow Coma Scale.

    https://en.wikipedia.org/wiki/Glasgow_Coma_Scale
    """
    def __init__(self):
        super(GCS, self).__init__()
        self.category = CATEGORY
        self.name = _(u"Glasgow CS")
        self.Eye = [
            _(u'Espontaneamente'),
            _(u'Estímulo Verbal'),
            _(u'A dor'),
            _(u'Nunca')]
        self.Lang = [
            _(u'Orientado e falando'),
            _(u'Desorientado e falando'),
            _(u'Palavras confusas'),
            _(u'Sons incompreensiveis'),
            _(u'Sem resposta')]
        self.Motor = [
            _(u'Obedece comandos'),
            _(u'Localiza a dor'),
            _(u'Flexão normal'),
            _(u'Flexão anormal'),
            _(u'Extensão'),
            _(u'Sem resposta')]
        self.data = [
            (_(u'Olhos'), 'combo', (self.Eye, 0)),
            (_(u'Verbal'), 'combo', (self.Lang, 0)),
            (_(u'Motor'), 'combo', (self.Motor, 0))]

    def show(self):
        def prob(i):
            if i > 10:
                return 82
            if i > 7:
                return 68
            if i > 4:
                return 34
            return 7
        E = self.getform()[0][2][1]
        L = self.getform()[1][2][1]
        M = self.getform()[2][2][1]
        GCS = 4 - E + 5 - L + 6 - M
        self.notify(_(u"GCS = %(GCS)d\nProb. recuperação: %(pGCS)d%%" % {
            'GCS': GCS, 'pGCS': prob(GCS)}))


class NINDS3(MedCalc):
    """National Institutes of Health Stroke Scale.

    https://en.wikipedia.org/wiki/National_Institutes_of_Health_Stroke_Scale
    http://www.ninds.nih.gov/doctors/nih_stroke_scale.pdf

    Three item scale for prediction of stroke recovery.
    http://www.medicine.ox.ac.uk/bandolier/booth/diagnos/stroked.html
    """
    def __init__(self):
        super(NINDS3, self).__init__()
        self.category = CATEGORY
        self.name = _(u'NINDS 3-Item')
        # Magnetic resonance diffusion-weighted imaging
        self.volume = [
            _(u'<= 14.1 mL'),
            _(u'> 14.1 mL')]
        # NIH stroke scale
        self.nihss = [
            _(u'<= 3'),
            _(u'4 a 15'),
            _(u'> 15')]
        # Time from onset
        self.horas = [
            _(u'<= 3 horas'),
            _(u'3 a 6 horas'),
            _(u'> 6 horas')]
        self.data = [
            (_(u'Volume da lesão MR-DWI'), 'combo', (self.volume, 0)),
            (_(u'NIHSS score'), 'combo', (self.nihss, 0)),
            (_(u'Tempo em horas desde o começo'), 'combo', (self.horas, 0))]

    def show(self):
        def prob(i):
            if i < 3:
                return _("Baixa")
            if i < 5:
                return _("Média")
            return _("Alta")
        V = self.getform()[0][2][1]
        N = self.getform()[1][2][1]
        H = self.getform()[2][2][1]
        ninds3 = 1 - V + 4 - 2 * N + H
        self.notify(
            _(u"NINDS3 = %(ninds3)d\nProb. recuperação: %(pninds3)s" % {
                'ninds3': ninds3, 'pninds3': prob(ninds3)}))


class Zung(MedCalc):
    """Zung Self-Rating Depression Scale.

    https://en.wikipedia.org/wiki/Zung_Self-Rating_Depression_Scale
    """
    def __init__(self):
        super(Zung, self).__init__()
        self.category = CATEGORY
        self.name = _(u'Zung Depressão')
        alist = [
            _(u'Poucas Vezes'),         # A little of the time
            _(u'Algumas Vezes'),        # Some of the time
            _(u'Boa Parte das Vezes'),  # Good part of the time
            _(u'Quase Sempre')]         # Most of the time
        self.data = [
            (_(u'Sinto desanimo e tristeza?'), 'combo', (alist, 0)),
            (_(u'Sinto melhor de manhã?'), 'combo', (alist, 0)),
            (_(u'Choro ou tenho vontade?'), 'combo', (alist, 0)),
            (_(u'Problemas para dormir?'), 'combo', (alist, 0)),
            (_(u'Como o habitual?'), 'combo', (alist, 0)),
            (_(u'Vida sexual normal?'), 'combo', (alist, 0)),
            (_(u'Estou perdendo peso?'), 'combo', (alist, 0)),
            (_(u'Problemas de constipação?'), 'combo', (alist, 0)),
            (_(u'Coração batendo mais acelerado?'), 'combo', (alist, 0)),
            (_(u'Cansado sem razão?'), 'combo', (alist, 0)),
            (_(u'Pensamento claro como de costume?'), 'combo', (alist, 0)),
            (_(u'É fácil fazer o que estou acostumado?'), 'combo', (alist, 0)),
            (_(u'Sinto-me inquieto?'), 'combo', (alist, 0)),
            (_(u'Sinto-me esperançoso com relação ao futuro?'), 'combo',
                (alist, 0)),
            (_(u'Mais irritável que o usual?'), 'combo', (alist, 0)),
            (_(u'É fácil tomar decisões?'), 'combo', (alist, 0)),
            (_(u'Sinto-me útil e necessário?'), 'combo', (alist, 0)),
            (_(u'Minha vida está plena?'), 'combo', (alist, 0)),
            (_(u'Sinto que os outros estariam melhor com eu morto?'), 'combo',
                (alist, 0)),
            (_(u'Gosto das coisas que costumava gostar?'), 'combo',
                (alist, 0))]

    def show(self):
        def prob(i, j):
            if i % 2 == 1:
                return 4 - j
            else:
                return 1 + j

        def diag(i):
            if i < 36:
                return _(u"Normal")
            if i < 57:
                return _(u"Limiar")
            return _(u"Limiar")
        f = self.getform()
        ZNG = 0
        for i in range(20):
            ZNG += prob(i, f[i][2][1])
        self.notify(_(u"Zung = %(ZNG)d\nProvavelmente:%(dGCS)s" % {
            'ZNG': ZNG, 'dGCS': diag(GCS)}))


class Hachinski(MedCalcList):
    """Hachinski ischemia score.

    http://www.strokecenter.org/wp-content/uploads/2011/08/hachinski.pdf
    http://www.ncbi.nlm.nih.gov/pubmed/1164215?dopt=Abstract
    """
    def __init__(self):
        super(Hachinski, self).__init__()
        self.category = CATEGORY
        self.name = _(u'Hachinski Indice Isquemico')
        self.data = [
            _(u'Stepwise deterioration'),
            _(u'Fluctuating course'),
            _(u'Nocturnal confusion'),
            _(u'Relative preservation of personality'),
            _(u'Depression'),
            _(u'Somatic complaints'),
            _(u'Emotional incontinence'),
            _(u'History of hypertension'),
            _(u'History of strokes'),
            _(u'Evidence of associated atherosclerosis'),
            _(u'Focal neurological symptoms'),
            _(u'Focal neurological signs')]
        self.pontos = [2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2]

    def show(self):
        soma = 0
        for i in self._f:
            soma += self.pontos[i]
        if soma > 7:
            self.notify(_(u"Pontos %d- demencia vascular" % soma))
        if soma < 4:
            self.notify(_(u"Pontos %d- Demencia Primária" % soma))
        if soma > 3 and soma < 8:
            self.notify(_(u"Pontos %d- Limiar / Mixed" % soma))


class CHADS2(MedCalcList):
    """CHADS2 - AVC/AFib
    
    CHADS2 Score for AF (atrial fibrillation)
    Definetly not VAS

    http://reference.medscape.com/calculator/chads-2-af-stroke
    Gage BF, Waterman AD, Shannon W, et. al. Validation of clinical classification schemes for predicting stroke: results from the National Registry of Atrial Fibrillation. JAMA. 2001 Jun 13;285(22):2864-70.
    Go AS, Hylek EM, Chang Y, et. al. Anticoagulation therapy for stroke prevention in atrial fibrillation: how well do randomized trials translate into clinical practice?. JAMA. 2003 Nov 26;290(20):2685-92.
    
    http://www.gpnotebook.co.uk/simplepage.cfm?ID=x20110126111352933383

    Russian translation:
        http://athero.ru/AF_risk-assessment_1.pdf#2
    """
    def __init__(self):
        super(CHADS2, self).__init__()
        self.category = CATEGORY
        self.name = _(u'CHADS2 - AVC/AFib')
        self.data = [
            _(u'Historico de ICC'),
            _(u'Hipertensão'),
            _(u'Mais de 75 anos'),
            _(u'Diabete mellitus'),
            _(u'Histórico de AVC ou TIA')]
        self.pontos = [1, 1, 1, 1, 2]
        self.rate = [
            (0, 1.9, u"1.2 - 3.0"),
            (1, 2.8, u"2.0 - 3.8"),
            (2, 4.0, u"3.1 - 5.1"),
            (3, 5.9, u"4.6 - 7.3"),
            (4, 8.5, u"6.3 - 11.1"),
            (5, 12.5, u"8.2 - 17.5"),
            (6, 18.2, u"10.5 - 27.4")]

    def show(self):
        soma = 0
        for i in self._f:
            soma += self.pontos[i]
        rt = self.rate[soma]
        msg = _(u"%(rt0)d Pontos\nProb AVC: %(rt1).1f%%\n(%(rt2)s)" % {
            'rt0': rt[0],
            'rt1': rt[1],
            'rt2': rt[2]})
        self.notify(msg)
