# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL1 = [
        7,
        _('Departments'),
        ['lineasDepto'],
        [],
[
    (_('Tacuarembó'), _("It's easy")),
    (_('Río Negro'), _("It's easy")),
    (_('Durazno'), _("It's easy")),
    (_('Flores'), _("It's easy")),
    (_('Florida'), _("It's easy")),
    (_('Cerro Largo'), _("It's easy")),
    (_('Lavalleja'), _("It's easy")),
    (_('Treinta y Tres'), _("It's easy"))
]
]

LEVEL2 = [
        1,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('the city of %s') % _('Durazno'), 2, _('Durazno'), _("It's the capital of\nthe department")),
    (_('the city of %s') % _('Sarandí del Yi'), 2, _('Sarandí del Yi'), _("It's in the south")),
    (_('the town of %s') % _('Blanquillo'), 2, _('Blanquillo'), _("It's in the west")),
    (_('the town of %s') % _('La Paloma'), 2, _('La Paloma'), _("It's in the northeast")),
    (_('the town of %s') % _('Carlos Reyles'), 2, _('Carlos Reyles'), _("It's in the west")),
    (_('the town of %s') % _('Centenario'), 2, _('Centenario'), _("It's in the north")),
    (_('the town of %s') % _('Baygorria'), 2, _('Baygorria'), _("It's in the northwest")),
    (_('the town of %s') % _('Aguas Buenas'), 2, _('Aguas Buenas'), _("It's in the north")),
    (_('the town of %s') % _('Alvarez'), 2, _('Pueblo de Alvarez'), _("It's in the northeast")),
    (_('the town of %s') % _('Feliciano'), 2, _('Feliciano'), _("It's in the west")),
    (_('the town of %s') % _('Ombúes de Oribe'), 2, _('Ombúes de Oribe'), _("It's in the center")),
    (_('the town of %s') % _('Rossell y Rius'), 2, _('Rossell y Rius'), _("It's in the southeast")),
    (_('the town of %s') % _('San Jorge'), 2, _('San Jorge'), _("It's in the north")),
    (_('the town of %s') % _('Carmen'), 2, _('Carmen'), _("It's in the south")),
    (_('the city of %s') % _('Cerro Chato'), 2, _('Cerro Chato'), _("It's in the southeast")),
    (_('the town of %s') % _('Santa Bernardina'), 2, _('Santa Bernardina'), _("It's in the southwest")),
    (_('the town of %s') % _('Puntas de Malbajar'), 2, _('Puntas de Malbajar'), _("It's in the southeast"))
]
]

LEVEL3 = [
        15,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('Río Negro'), _("It's in the north")),
    (_('Río Yí'), _("It's in the south")),
    (_('Arroyo de Caballero'), _("It's in the west")),
    (_('Arroyo Villasboas'), _("It's in the southwest")),
    (_('Arroyo Maciel'), _("It's in the south")),
    (_('Arroyo de Tejera'), _("It's in the south")),
    (_('Arroyo Tomás Cuadra'), _("It's in the south")),
    (_('Arroyo Maestre de Campo'), _("It's in the south")),
    (_('Arroyo Antonio Herrera'), _("It's in the south")),
    (_('Arroyo Malbajar'), _("It's in the southeast")),
    (_('Arroyo del Cordobés'), _("It's in the east")),
    (_('Arroyo Palmas'), _("It's in the east")),
    (_('Arroyo Blanquillo'), _("It's in the northeast")),
    (_('Arroyo de las Cañas'), _("It's in the northeast"))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %(f)s') % {'f': _('Cuchilla Ramírez')}, 4, _('Cuchilla Ramírez'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla Grande del Durazno')}, 4, _('Cuchilla Grande del Durazno'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla Villasboas')}, 4, _('Cuchilla Villasboas'), _('Try again')),
    (_('the %(m)s') % {'m': _('Cerro Dos Hermanos')}, 5, _('Cerro Dos Hermanos'), _("It's in the east"))
]
]

LEVEL5 = [
        5,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('Route %s') % 5, _('Passes through %s') % _('Durazno')),
    (_('Route %s') % 4, _('Passes through %s') % _('Baygorria')),
    (_('Route %s') % 14, _('Passes through %s') % _('Villa del Carmen')),
    (_('Route %s') % 6, _('Passes through %s') % _('Sarandí del Yi')),
    (_('Route %s') % 43, _('Passes through %s') % _('Blanquillo')),
    (_('Route %s') % 19, _('Passes through %s') % _('Rossell y Rius')),
    (_('Route %s') % 100, _('Try again'))
]
]

LEVELS = [LEVEL1, LEVEL2, LEVEL3, LEVEL4, LEVEL5]

