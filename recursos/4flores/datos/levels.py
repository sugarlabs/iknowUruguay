# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL1 = [
        7,
        _('Departments'),
        ['lineasDepto'],
        [],
[
    (_('Durazno'), _("It's easy")),
    (_('Soriano'), _("It's easy")),
    (_('Flores'), _("It's easy")),
    (_('Colonia'), _("It's easy")),
    (_('San José'), _("It's easy")),
    (_('Florida'), _("It's easy"))
]
]

LEVEL2 = [
        1,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('the city of %s') % _('Trinidad'), 2, _('Trinidad'), _("It's the capital of\nthe department")),
    (_('the town of %s') % _('Andresito'), 2, _('Andresito'), _("It's in the north")),
    (_('the town of %s') % _('Juan José Castro'), 2, _('Juan José Castro'), _("It's in the center")),
    (_('the town of %s') % _('Cerro Colorado'), 2, _('Cerro Colorado'), _("It's in the center")),
    (_('the town of %s') % _('La Casilla'), 2, _('La Casilla'), _("It's in the south")),
    (_('the town of %s') % _('San Gregorio'), 2, _('San Gregorio'), _("It's in the south")),
    (_('the town of %s') % _('Ismael Cortinas'), 2, _('Ismael Cortinas'), _("It's in the southwest"))
]
]

LEVEL3 = [
        15,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('Río San José'), _("It's in the south")),
    (_('Río Yí'), _("It's in the northeast")),
    (_('Río Negro'), _("It's in the north")),
    (_('Arroyo Grande'), _("It's in the west")),
    (_('Arroyo Marincho'), _("It's in the northwest")),
    (_('Arroyo Coronilla'), _("It's in the north")),
    (_('Arroyo Sarandi'), _("It's in the north")),
    (_('Arroyo Porongos'), _("It's in the northeast")),
    (_('Arroyo del Sarandí'), _("It's in the center")),
    (_('Arroyo del Tala'), _("It's in the east")),
    (_('Arroyo San Gregorio'), _("It's in the south")),
    (_('Arroyo Pintos'), _("It's in the south")),
    (_('Arroyo Bolas Grande'), _("It's in the south")),
    (_('Arroyo Juncal'), _("It's in the south")),
    (_('Arroyo del Sauce'), _("It's in the southwest")),
    (_('Arroyo Ojosmín'), _("It's in the southwest")),
    (_('Arroyo Guardia Vieja'), _("It's in the west")),
    (_('Arroyo Manantiales'), _("It's in the west")),
    (_('Arroyo Arenal Chico'), _("It's in the west")),
    (_('Arroyo Sauce'), _("It's in the northwest")),
    (_('Arroyo Tala'), _("It's in the north")),
    (_('Arroyo Malo'), _("It's in the north")),
    (_('Arroyo de la Cordobesa'), _("It's in the east")),
    (_('Arroyo Duraznito'), _("It's in the east")),
    (_('Arroyo Chamangá'), _("It's in the east")),
    (_('Arroyo de los Ahogados'), _("It's in the southeast")),
    (_('Arroyo Piedra Sola'), _("It's in the southeast")),
    (_('Arroyo Maciel'), _("It's in the east")),
    (_('Arroyo Manguera'), _("It's in the northeast"))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %(f)s') % {'f': _('Cuchilla Marincho')}, 4, _('Cuchilla Marincho'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla Villasboas')}, 4, _('Cuchilla Villasboas'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla Grande Inferior')}, 4, _('Cuchilla Grande Inferior'), _('Try again')),
    (_('the %(m)s') % {'m': _('Cerros de Ojosmín')}, 5, _('Cerros de Ojosmín'), _('Try again'))
]
]

LEVEL5 = [
        5,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('Route %s') % 3, _('Try again')),
    (_('Route %s') % 14, _('Try again')),
    (_('Route %s') % 57, _('Try again')),
    (_('Route %s') % 23, _('Passes through %s') % _('Ismael Cortinas'))
]
]

LEVELS = [LEVEL1, LEVEL2, LEVEL3, LEVEL4, LEVEL5]

