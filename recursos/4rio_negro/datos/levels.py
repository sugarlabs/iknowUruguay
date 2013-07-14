# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL2 = [
        1,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('the city of %s') % _('Fray Bentos'), 2, _('Fray Bentos'), _("It's the capital of\nthe department")),
    (_('the town of %s') % _('Merinos'), 2, _('Merinos'), _("It's in the northeast")),
    (_('the town of %s') % _('Algorta'), 2, _('Algorta'), _("It's in the north")),
    (_('the town of %s') % _('P. de los Mellizos'), 2, _('P. de los Mellizos'), _("It's in the northeast")),
    (_('the town of %s') % _('Sarandí de Navarro'), 2, _('Sarandí de Navarro'), _("It's in the northeast")),
    (_('the town of %s') % _('Paso de la Cruz'), 2, _('Paso de la Cruz'), _("It's in the north")),
    (_('the town of %s') % _('San Javier'), 2, _('San Javier'), _("It's in the northwest")),
    (_('the town of %s') % _('Young'), 2, _('Young'), _("It's in the center")),
    (_('the town of %s') % _('Tres Quintas'), 2, _('Tres Quintas'), _("It's in the west")),
    (_('the town of %s') % _('Bellaco'), 2, _('Bellaco'), _("It's in the west")),
    (_('the town of %s') % _('Grecco'), 2, _('Grecco'), _("It's in the southeast")),
    (_('the town of %s') % _('Nuevo Berlín'), 2, _('Nuevo Berlín'), _("It's in the southwest"))
]
]

LEVEL3 = [
        15,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('Río Uruguay'), _("It's in the west")),
    (_('Río Negro'), _("It's in the south")),
    (_('Arroyo Grande'), _("It's in the south")),
    (_('Arroyo de las Flores'), _("It's in the southeast")),
    (_('Arroyo Averías Grande'), _("It's in the northeast")),
    (_('Arroyo Averías Chico'), _("It's in the center")),
    (_('Arroyo Ñandubay'), _("It's in the south")),
    (_('Arroyo Don Esteban'), _("It's in the north")),
    (_('Arroyo Santa María'), _("It's in the north")),
    (_('Arroyo Negro'), _("It's in the northwest")),
    (_('Arroyo Bellaco'), _("It's in the northwest")),
    (_('Arroyo Gutiérrez'), _("It's in the northwest")),
    (_('Arroyo Coladeras'), _("It's in the southwest")),
    (_('Arroyo Sánchez'), _("It's in the southwest")),
    (_('Arroyo Salsipuedes Grande'), _("It's in the northeast")),
    (_('Arroyo Tres Árboles'), _("It's in the northeast")),
    (_('Arroyo Rolón'), _("It's in the northwest")),
    (_('Arroyo Molles'), _("It's in the southeast"))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %(f)s') % {'f': _('Cuchilla de Haedo')}, 4, _('Cuchilla de Haedo'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla de Navarro')}, 4, _('Cuchilla de Navarro'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cerro Pelado')}, 5, _('Cerro Pelado'), _("It's in the south")),
    (_('the %(m)s') % {'m': _('Cerro del Quebracho')}, 5, _('Cerro del Quebracho'), _("It's in the center"))
]
]

LEVEL5 = [
        5,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('Route %s') % 2, _('Comes from %s') % _('Mercedes')),
    (_('Route %s') % 24, _('Try again')),
    (_('Route %s') % 3, _('Passes through %s') % _('Young')),
    (_('Route %s') % 20, _('Try again')),
    (_('Route %s') % 25, _('Passes through %s') % _('Young')),
    (_('Route %s') % 4, _('Passes through %s') % _('Baygorria'))
]
]

LEVELS = [LEVEL2, LEVEL3, LEVEL4, LEVEL5]

