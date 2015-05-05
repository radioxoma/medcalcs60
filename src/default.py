#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import with_statement

"""
Medical calculator

Ref: http://www-users.med.cornell.edu/~spon/picu/calc/medcalc.htm
Ref: http://www.medcalc.com/
Ref: http://www.medal.org/
"""


import os
import sys
import inspect
from operator import attrgetter
from itertools import groupby
import ConfigParser
import gettext

import e32
import graphics
import appuifw

import medcalc
from medcalc import geralclass


class Application(object):
    def __init__(self):
        # Configuration
        self._cfg = ConfigParser.RawConfigParser(defaults={'language': ''})
        self._cfg_section = 'DEFAULT'
        self._cfg_path = "C:/System/data/medcalc.ini"
        self._cfg.read(self._cfg_path)

        # Localization
        # mo files will be collected from `gettext._default_localedir` subdirs
        # There is no 'LANGUAGE', 'LC_ALL', 'LC_MESSAGES', 'LANG' system
        # variable or other normal way o detect system language/locale,
        # so we need to specify languages by yourself.
        if sys.platform == 'symbian_s60':
            self._localedir = None  # Parameter for function. not actual path
        else:
            # On desktop
            self._localedir = 'locale'
        self.set_language(self._cfg.get(self._cfg_section, 'language'))

        # Application runtime
        self._app_lock = e32.Ao_lock()
        self.Parent = None
        self.collect_calcs()

    def collect_calcs(self):
        """Collect all calculators and create menu structure.
        """
        from medcalc import geral, neuro, rx, uti
        classes = list()
        for modname, mod in inspect.getmembers(medcalc, inspect.ismodule):
            for clsname, cls in inspect.getmembers(mod, inspect.isclass):
                # mro = inspect.getmro(cls)
                mro = cls.__bases__
                if (geralclass.MedCalc in mro or
                    geralclass.MedCalcList in mro or
                    geralclass.MedImage in mro):
                    classes.append(cls())

        classes.sort(key=attrgetter('category'))

        self.categories = list()
        self.menu_items = list()
        for k, grp in groupby(classes, attrgetter('category')):
            self.categories.append(k)
            self.menu_items.append(medcalc.geralclass.MenuItem(list(grp)))

    def run(self):
        # from key_codes import EKeyLeftArrow
        self.lb = appuifw.Listbox(self.categories, self.lbox_observe)
        # self.lb.bind(EKeyLeftArrow, lambda: self.lbox_observe(0))
        old_title = appuifw.app.title
        self.refresh()
        self._app_lock.wait()
        appuifw.app.title = old_title
        appuifw.app.body = None
        self.lb = None

    def refresh(self):
        appuifw.app.screen = 'normal'
        appuifw.app.title = u"Medcalc"
        appuifw.app.menu = [
            # (u"Settings", (
            #     (u"Language", self.menu_language))),
            (_(u"Language"), self.menu_language),
            (_(u"About"), self.menu_about),
            (_(u"Exit"), self.exit_key_handler)]
        appuifw.app.exit_key_handler = self.exit_key_handler
        appuifw.app.body = self.lb

    def do_exit(self):
        self.exit_key_handler()

    def exit_key_handler(self):
        appuifw.app.exit_key_handler = None
        self._app_lock.signal()
        sys.exit()

    def lbox_observe(self, ind=None):
        if ind is not None:
            index = ind
        else:
            index = self.lb.current()
        focused_item = 0
        self.menu_items[index].run(self)
        appuifw.app.screen = 'normal'

    def back(self):
        pass

    def set_language(self, language):
        """Change interface language.

        :param str language: 'en', 'ru', etc.
        """
        l10n = gettext.translation(
            'medcalc', localedir=self._localedir, languages=[language],
            fallback=True)
        l10n.install(unicode=True)

    def save_cfg(self):
        """Write config to file.
        """
        with open(self._cfg_path, mode='wb') as f:
            self._cfg.write(f)

    def menu_language(self):
        """Show language list, save changes in config.
        """
        def find_translations():
            """Get list of language codes.

            `gettext.find()` can't do it without defined system variables
            """
            # __builtin__.__dict__['_'] = lambda x: x  # Monkey path
            all_translations = set()
            if self._localedir:
                localedir = self._localedir
            else:
                localedir = gettext._default_localedir
            for loc_folder in os.listdir(localedir):
                for mo in os.listdir(
                        os.path.join(localedir, loc_folder, 'LC_MESSAGES')):
                    if mo.endswith('.mo'):
                        all_translations.add(unicode(loc_folder))
            return list(all_translations)

        translations = find_translations()
        translations.append(u'Disable translation')
        idx = appuifw.popup_menu(translations, _(u"Select language:"))
        if idx is not None:
            self.set_language(translations[idx])
            self._cfg.set(self._cfg_section, 'language', translations[idx])
            self.save_cfg()
            appuifw.note(
                _(u"Please reload the program to apply the changes."), 'info')

    def menu_about(self):
        appuifw.note(
            _(u"Open source medical calculator v%s." % medcalc.__version__),
            'conf')


def splash():
    """Show splash image over the screen.
    """
    # Backslashes in file paths for compatibility with symbian native library
    if sys.platform == 'symbian_s60':
        img_share = os.path.join(sys.prefix, 'share\\medcalc', 'logo.png')
    else:
        img_share = os.path.join(os.getcwdu(), 'img', 'logo.png')
    img1 = graphics.Image.open(img_share)
    appuifw.app.screen = 'full'

    def handle_redraw(rect):
        canvas.blit(img1)

    canvas = appuifw.Canvas(event_callback=None, redraw_callback=handle_redraw)
    canvas.blit(img1)  # Causes error in wxwidgets pys60 emulator
    appuifw.app.body = canvas
    e32.ao_sleep(1)
    appuifw.app.screen = 'normal'


try:
    # if sys.platform == 'symbian_s60':
    #     splash()  # On windows it brokes pys60 emulation library
    Application().run()
except Exception, e:
    import traceback
    e1, e2, e3 = sys.exc_info()
    err_msg = repr(e) + u"\u2029" * 2 + u"Call stack:\u2029"
    err_msg + u''.join(traceback.format_exception(e1, e2, e3))

    lock = e32.Ao_lock()
    appuifw.app.title = u"Error log"
    appuifw.app.screen = 'full'
    appuifw.app.body = appuifw.Text(err_msg)
    appuifw.app.menu = [(u"Exit", lambda: lock.signal())]
    lock.wait()
