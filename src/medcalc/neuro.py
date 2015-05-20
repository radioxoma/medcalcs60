#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import with_statement


from medcalc.geralclass import *


CATEGORY = _(u"Neurology")


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
        self.name = _(u'Abbreviated mental test')
        self.data = [
            _(u'Current age'),
            _(u'Date of birth'),
            _(u'Can remember an address'),
            _(u'Where are you now'),
            _(u'What is the year'),
            _(u'Time to the nearest hour'),
            _(u'Recognize two persons'),
            _(u'Any historical data'),
            _(u'Present president'),
            _(u'Count from 20 to 1')]

    def show(self):
        soma = 0
        for i in self._f:
            soma += 1
        if soma > 6:
            self.notify(_(u"%d points, no dementia") % soma)
        else:
            self.notify(_(u"%d points, dementia probability 81.5 %%") % soma)


class GCS(MedCalc):
    """Glasgow Coma Scale.

    https://en.wikipedia.org/wiki/Glasgow_Coma_Scale
    """
    def __init__(self):
        super(GCS, self).__init__()
        self.category = CATEGORY
        self.name = _(u"Glasgow coma scale")
        # self.desc = _(u"")
        self.Eye = [
            _(u'Opens spontaneously'),
            _(u'In response to voice'),
            _(u'Pain'),
            _(u'None')]
        self.Lang = [
            _(u'Oriented, converses normally'),
            _(u'Confused, disoriented'),
            _(u'Utters inappropriate words'),
            _(u'Incomprehensible sounds'),
            _(u'No reaction')]
        self.Motor = [
            _(u'Obeys commands'),
            _(u'Localizes painful stimuli'),
            _(u'Withdrawal to painful stimuli'),
            _(u'Flexion to pain (decorticate)'),
            _(u'Extension to pain (decerebrate)'),
            _(u'No reaction')]
        self.data = [
            (_(u'Eye'), 'combo', (self.Eye, 0)),
            (_(u'Verbal'), 'combo', (self.Lang, 0)),
            (_(u'Motor'), 'combo', (self.Motor, 0))]

    def prob(self, i):
        """Recuperation probability.
        """
        if i > 10:
            return 82
        if i > 7:
            return 68
        if i > 4:
            return 34
        return 7

    def conscience(self, points):
        """Conscience level.
        """
        if points == 15:
            return _(u'clear mind')  # Ясное сознание
        elif 13 <= points <= 14:
            return _(u'moderate lightheadedness')  # Оглушение умеренное
        elif 10 <= points <= 12:
            return _(u'deep lightheadedness')  # Оглушение глубокое
        elif 8 <= points <= 9:
            return _(u'sopor')  # Сопор
        elif 6 <= points <= 7:
            return _(u'moderate coma')  # Кома умеренная
        elif 4 <= points <= 5:
            return _(u'deep coma')  # Кома глубокая
        elif points <= 3:
            return _(u'terminal coma, brain death')  # Кома терминальная, смерть мозга

    def show(self):
        E = self.getform()[0][2][1]
        L = self.getform()[1][2][1]
        M = self.getform()[2][2][1]
        GCS = 4 - E + 5 - L + 6 - M
        self.notify(_(u"%(GCS)d points (%(conscience)s), recovery prob. %(pGCS)d%%") % {
            'GCS': GCS, 'conscience': self.conscience(GCS), 'pGCS': self.prob(GCS)})


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
        self.name = _(u'NINDS 3-item')
        # Magnetic resonance diffusion-weighted imaging
        self.volume = [
            _(u'≤ 14.1 mL'),
            _(u'> 14.1 mL')]
        # NIH stroke scale
        self.nihss = [
            u'≤ 3',
            u'4-15',
            u'> 15']
        # Time from onset
        self.horas = [
            _(u'≤ 3 hours'),
            _(u'3-6 hours'),
            _(u'> 6 hours')]
        self.data = [
            (_(u'MR-DWI lesion volume'), 'combo', (self.volume, 0)),
            (_(u'NIHSS score'), 'combo', (self.nihss, 0)),
            (_(u'Time from onset'), 'combo', (self.horas, 0))]

    def show(self):
        def prob(i):
            if i < 3:
                return _(u"low")
            if i < 5:
                return _(u"medium")
            return _(u"high")
        V = self.getform()[0][2][1]
        N = self.getform()[1][2][1]
        H = self.getform()[2][2][1]
        ninds3 = 1 - V + 4 - 2 * N + H
        self.notify(
            _(u"%(ninds3)d points, recovery prob. %(pninds3)s") % {
                'ninds3': ninds3, 'pninds3': prob(ninds3)})


class Zung(MedCalc):
    """Zung Self-Rating Depression Scale.

    https://en.wikipedia.org/wiki/Zung_Self-Rating_Depression_Scale
    http://psychology-tools.com/zung-depression-scale/
    """
    def __init__(self):
        super(Zung, self).__init__()
        self.category = CATEGORY
        self.name = _(u'Zung depression scale')
        alist = [
            _(u'A little of the time'),
            _(u'Some of the time'),
            _(u'Good part of the time'),
            _(u'Most of the time')]
        self.data = [
            (_(u'I feel down hearted and blue.'), 'combo', (alist, 0)),
            (_(u'Morning is when I feel the best.'), 'combo', (alist, 0)),
            (_(u'I have crying spells or feel like it.'), 'combo', (alist, 0)),
            (_(u'I have trouble sleeping at night.'), 'combo', (alist, 0)),
            (_(u'I eat as much as I used to.'), 'combo', (alist, 0)),
            (_(u'I still enjoy sex.'), 'combo', (alist, 0)),
            (_(u'I notice that I am losing weight.'), 'combo', (alist, 0)),
            (_(u'I have trouble with constipation.'), 'combo', (alist, 0)),
            (_(u'My heart beats faster than usual.'), 'combo', (alist, 0)),
            (_(u'I get tired for no reason.'), 'combo', (alist, 0)),
            (_(u'My mind is as clear as it used to be.'), 'combo', (alist, 0)),
            (_(u'I find it easy to do the things I used to.'), 'combo', (alist, 0)),
            (_(u'I am restless and can’t keep still.'), 'combo', (alist, 0)),
            (_(u'I feel hopeful about the future.'), 'combo', (alist, 0)),
            (_(u'I am more irritable than usual.'), 'combo', (alist, 0)),
            (_(u'I find it easy to make decisions.'), 'combo', (alist, 0)),
            (_(u'I feel that I am useful and needed.'), 'combo', (alist, 0)),
            (_(u'My life is pretty full.'), 'combo', (alist, 0)),
            (_(u'I feel that others would be better off if I were dead.'), 'combo', (alist, 0)),
            (_(u'I still enjoy the things I used to do.'), 'combo', (alist, 0))]

    def show(self):
        def prob(i, j):
            if i % 2 == 1:
                return 4 - j
            else:
                return 1 + j

        def diag(i):
            if i < 36:
                return _(u"normal")
            if i < 57:
                return _(u"threshold")
            return _(u"threshold")
        f = self.getform()
        ZNG = 0
        for i in range(20):
            ZNG += prob(i, f[i][2][1])
        self.notify(_(u"%(ZNG)d prob. %(dGCS)s") % {
            'ZNG': ZNG, 'dGCS': diag(GCS)})


class Hachinski(MedCalcList):
    """Hachinski ischemia score.

    http://www.strokecenter.org/wp-content/uploads/2011/08/hachinski.pdf
    http://www.ncbi.nlm.nih.gov/pubmed/1164215?dopt=Abstract
    """
    def __init__(self):
        super(Hachinski, self).__init__()
        self.category = CATEGORY
        self.name = _(u'Hachinski ischemia score')
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
            self.notify(_(u"%d points, vascular dementia") % soma)
        if soma < 4:
            self.notify(_(u"%d points, primary dementia") % soma)
        if 3 < soma < 8:
            self.notify(_(u"%d points, borderline / mixed") % soma)


class CHADS2(MedCalcList):
    """CHADS2 - stroke risk.

    CHADS2 Score for AF (atrial fibrillation)
    https://en.wikipedia.org/wiki/CHA2DS2%E2%80%93VASc_score

    http://reference.medscape.com/calculator/chads-2-af-stroke
    Gage BF, Waterman AD, Shannon W, et. al. Validation of clinical
    classification schemes for predicting stroke: results from the National
    Registry of Atrial Fibrillation. JAMA. 2001 Jun 13;285(22):2864-70.
    
    Go AS, Hylek EM, Chang Y, et. al. Anticoagulation therapy for stroke
    prevention in atrial fibrillation: how well do randomized trials translate
    into clinical practice?. JAMA. 2003 Nov 26;290(20):2685-92.

    http://www.gpnotebook.co.uk/simplepage.cfm?ID=x20110126111352933383

    Russian translation:
        http://athero.ru/AF_risk-assessment_1.pdf#2
    """
    def __init__(self):
        super(CHADS2, self).__init__()
        self.category = CATEGORY
        self.name = _(u'CHADS2 - stroke risk')
        self.data = [
            _(u'Heart failure, past or current'),
            _(u'Hypertension'),
            _(u'Age ≥ 75 years'),
            _(u'Diabetes mellitus'),
            _(u'Prior ischemic stroke, TIA or thromboembolism')]
        self.pontos = [1, 1, 1, 1, 2]
        self.rate = [
            (0, 1.9, u"1.2-3.0"),
            (1, 2.8, u"2.0-3.8"),
            (2, 4.0, u"3.1-5.1"),
            (3, 5.9, u"4.6-7.3"),
            (4, 8.5, u"6.3-11.1"),
            (5, 12.5, u"8.2-17.5"),
            (6, 18.2, u"10.5-27.4")]

    def show(self):
        soma = 0
        for i in self._f:
            soma += self.pontos[i]
        rt = self.rate[soma]
        msg = _(u"%(rt0)d points, stroke prob. %(rt1).1f%% (%(rt2)s)") % {
            'rt0': rt[0],
            'rt1': rt[1],
            'rt2': rt[2]}
        self.notify(msg)
