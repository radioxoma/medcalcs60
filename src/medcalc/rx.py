#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import with_statement

from medcalc.geralclass import *


class RxTorax(MedImage):
    def __init__(self):
        self.fname = 'chest-xray.png'


class RxToraxLat(MedImage):
    def __init__(self):
        self.fname = 'chest-xray-lat-nl.png'


class RxToraxFem(MedImage):
    def __init__(self):
        self.fname = 'chest-xr-normal.png'


class RxToraxPneumonia(MedImage):
    def __init__(self):
        self.fname = 'chest-xr-pneumoPA.png'


class RxToraxPneumonia2(MedImage):
    def __init__(self):
        self.fname = 'chest-xr-pneumoPA2.png'


class RxToraxAntrax(MedImage):
    def __init__(self):
        self.fname = 'chest-xr-antrax.png'


class RxMarfan(MedImage):
    def __init__(self):
        self.fname = 'chest-xr-antrax.png'


class RxCancer(MedImage):
    def __init__(self):
        self.fname = 'rx-cancer.png'
