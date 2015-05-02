#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import with_statement

import os
import sys
import appuifw
import graphics
import sysinfo


class MedCalc(object):
    """Calculator item representation.
    """
    def run(self):
        flags = appuifw.FFormEditModeOnly + appuifw.FFormDoubleSpaced
        self._f = appuifw.Form(self.data, flags)
        self._f.save_hook = self.mark_saved
        self._f.flags = appuifw.FFormEditModeOnly + appuifw.FFormDoubleSpaced
        self._f.execute()

    def mark_saved(self, aBool):
        self._saved = aBool

    def getform(self):
        return self._f

    def is_saved(self):
        return self.bmi_saved


class MedCalcList(object):
    """Set of checkboxes item representation.
    """
    def run(self):
        self._f = appuifw.multi_selection_list(
            self.data, style='checkbox', search_field=1)

    def mark_saved(self, aBool):
        self._saved = aBool

    def getform(self):
        return self._f

    def is_saved(self):
        return True


class MedImage(object):
    """Image item representation.
    """
    def run(self):
        if sys.platform == 'symbian_s60':
            img_share = os.path.join(sys.prefix, 'share\\medcalc', self.fname)
        else:
            img_share = os.path.join(os.getcwdu(), 'img', self.fname)
        appuifw.app.screen = 'full'
        img1 = graphics.Image.open(img_share)
        w, h = sysinfo.display_pixels()
        if w > h:
            img1 = img1.transpose(graphics.ROTATE_270)

        def handle_redraw(rect):
            canvas.blit(img1)

        canvas = appuifw.Canvas(redraw_callback=handle_redraw)
        try:
            canvas.blit(img1)
            appuifw.app.body = canvas
        except:
            appuifw.note(u"Error %s" % img_share, "note")

    def mark_saved(self, aBool):
        self._saved = aBool

    def getform(self):
        return self._f


class MenuItem(object):
    """Submenu.
    """
    def run(self, menupai):
        from key_codes import EKeyLeftArrow
        self.lb = appuifw.Listbox(self.Children, self.lbox_observe)
        self.lb.bind(EKeyLeftArrow, lambda: self.lbox_observe(0))
        appuifw.app.title = self.Title
        appuifw.app.menu = []
        appuifw.app.exit_key_handler = self.exit_key_handler
        appuifw.app.body = self.lb
        self.menupai = menupai

    def lbox_observe(self, ind=None):
        if ind is not None:
            index = ind
        else:
            index = self.lb.current()
        focused_item = 0
        self.MenuKid[index].run()
        self.MenuKid[index].show()
        appuifw.app.screen = 'normal'

    def exit_key_handler(self):
        appuifw.app.exit_key_handler = None
        self.menupai.refresh()

    def do_exit(self):
        self.exit_key_handler()
