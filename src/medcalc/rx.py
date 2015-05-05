#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import with_statement

from medcalc.geralclass import *


CATEGORY = _(u"RX")


class RxTorax(MedImage):
    def __init__(self):
        super(RxTorax, self).__init__()
        self.category = CATEGORY
        self.name = _(u"Raio-X Torax PA")
        self.fname = 'chest-xray.png'


class RxToraxLat(MedImage):
    def __init__(self):
        super(RxToraxLat, self).__init__()
        self.category = CATEGORY
        self.name = _(u"Raio-X Torax Lat")
        self.fname = 'chest-xray-lat-nl.png'


class RxToraxFem(MedImage):
    def __init__(self):
        super(RxToraxFem, self).__init__()
        self.category = CATEGORY
        self.name = _(u"Raio-X Torax PA (F)")
        self.fname = 'chest-xr-normal.png'


class RxToraxPneumonia(MedImage):
    def __init__(self):
        super(RxToraxPneumonia, self).__init__()
        self.category = CATEGORY
        self.name = _(u"Raio-X Pneumonia")
        self.fname = 'chest-xr-pneumoPA.png'


class RxToraxPneumonia2(MedImage):
    def __init__(self):
        super(RxToraxPneumonia2, self).__init__()
        self.category = CATEGORY
        self.name = _(u"Outro Raio-X Pneumonia")
        self.fname = 'chest-xr-pneumoPA2.png'


class RxToraxAntrax(MedImage):
    def __init__(self):
        super(RxToraxAntrax, self).__init__()
        self.category = CATEGORY
        self.name = _(u"Raio-X Antrax")
        self.fname = 'chest-xr-antrax.png'


class RxMarfan(MedImage):
    def __init__(self):
        super(RxMarfan, self).__init__()
        self.category = CATEGORY
        self.name = _(u"Raio-X Marfan")
        self.fname = 'chest-xr-antrax.png'


class RxCancer(MedImage):
    def __init__(self):
        super(RxCancer, self).__init__()
        self.category = CATEGORY
        self.name = _(u"Raio-X Câncer")
        self.fname = 'rx-cancer.png'
