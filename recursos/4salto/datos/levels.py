# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL2 = [
        1,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('the city of %s') % _('Salto'), 1, _('Salto'), _("It's the capital of\nthe department")),
    (_('the city of %s') % _('Belén'), 2, _('Belén'), _("It's in the northwest")),
    (_('the city of %s') % _('Constitución'), 2, _('Constitución'), _("It's in the west")),
    (_('the town of %s') % _('Palomas'), 2, _('Palomas'), _("It's in the northwest")),
    (_('the town of %s') % _('Colonia Lavalleja'), 2, _('Colonia Lavalleja'), _("It's in the north")),
    (_('the town of %s') % _('Saucedo'), 2, _('Saucedo'), _("It's in the northwest")),
    (_('the city of %s') % _('Masoller'), 2, _('Masoller'), _("It's in the northeast")),
    (_('the town of %s') % _('Cayetano'), 2, _('Cayetano'), _("It's in the north")),
    (_('the town of %s') % _('Biassini'), 2, _('Biassini'), _("It's in the center")),
    (_('the town of %s') % _('Rincón de Valentín'), 2, _('Rincón de Valentín'), _("It's in the center")),
    (_('the town of %s') % _('Celeste'), 2, _('Celeste'), _("It's in the center")),
    (_('the town of %s') % _('San Antonio'), 2, _('San Antonio'), _("It's in the southwest")),
    (_('the town of %s') % _('Albisu'), 2, _('Albisu'), _("It's in the southwest")),
    (_('the town of %s') % _('Laureles'), 2, _('Laureles'), _("It's in the southwest")),
    (_('the town of %s') % _('Puntas de Valentín'), 2, _('Puntas de Valentín'), _("It's in the center")),
    (_('the town of %s') % _('Cerros de Vera'), 2, _('Cerros de Vera'), _("It's in the south")),
    (_('the town of %s') % _('Paso del Parque'), 2, _('Paso del Parque'), _("It's in the south")),
    (_('the town of %s') % _('Arerunguá'), 2, _('Arerunguá'), _("It's in the southeast")),
    (_('the health resort of %s') % _('Termas del Arapey'), 2, _('Termas del Arapey'), _("It's in the northwest")),
    (_('the town of %s') % _('Olivera'), 2, _('Olivera'), _("It's in the north")),
    (_('the town of %s') % _('Mataojo'), 2, _('Mataojo'), _("It's in the northeast"))
]
]

LEVEL3 = [
        15,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('Río Uruguay'), _("It's in the west")),
    (_('Río Arapey Grande'), _("It's in the north")),
    (_('Río Arapey Chico'), _("It's in the north")),
    (_('Río Daymán'), _("It's in the south")),
    (_('Arroyo Laureles Grande'), _("It's in the southwest")),
    (_('Arroyo Laureles Chico'), _("It's in the south")),
    (_('Arroyo de las Cañas'), _("It's in the center")),
    (_('Arroyo Sopas'), _("It's in the east")),
    (_('Arroyo del Sauce'), _("It's in the center")),
    (_('Arroyo S. Mataojito'), _("It's in the northeast")),
    (_('Arroyo Mataojo Grande'), _("It's in the east")),
    (_('Arroyo Mataojo Chico'), _("It's in the east")),
    (_('Arroyo Paloma Grande'), _("It's in the northwest")),
    (_('Arroyo Tangarupá'), _("It's in the northwest")),
    (_('Arroyo Valentín Grande'), _("It's in the center")),
    (_('Arroyo Arerunguá'), _("It's in the southeast")),
    (_('Arroyo Sarandí'), _("It's in the southeast")),
    (_('Arroyo Guayabos'), _("It's in the southeast")),
    (_('Arroyo Tapado'), _("It's in the southeast")),
    (_('Arroyo de los Talas'), _("It's in the center")),
    (_('Arroyo Valentín Chico'), _("It's in the center")),
    (_('Arroyo Tunas'), _("It's in the northwest")),
    (_('Arroyo S. del Arapey'), _("It's in the northeast")),
    (_('Arroyo Sarandí Chico'), _("It's in the northeast")),
    (_('Arroyo Moisés'), _("It's in the northeast")),
    (_('Arroyo Itapeby Grande'), _("It's in the west")),
    (_('Arroyo Itapeby Chico'), _("It's in the west")),
    (_('Arroyo San Antonio'), _("It's in the west")),
    (_('Arroyo Yacuy'), _("It's in the north"))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %(f)s') % {'f': _('Cuchilla de los Arapeyes')}, 4, _('Cuchilla de los Arapeyes'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla del Daymán')}, 4, _('Cuchilla del Daymán'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla de Haedo')}, 4, _('Cuchilla de Haedo'), _('Try again')),
    (_('the %(m)s') % {'m': _('Cerro Fortaleza')}, 5, _('Cerro Fortaleza'), _("It's in the center")),
    (_('the %(m)s') % {'m': _('Cerro de Corumbé')}, 5, _('Cerro de Corumbé'), _("It's in the east")),
    (_('the %(m)s') % {'m': _('Cerro Charrúa')}, 5, _('Cerro Charrúa'), _("It's in the east"))
]
]

LEVEL5 = [
        5,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('Route %s') % 3, _('Try again')),
    (_('Route %s') % 31, _('Try again')),
    (_('Route %s') % 4, _('Try again')),
    (_('Route %s') % 30, _('Try again'))
]
]

LEVELS = [LEVEL2, LEVEL3, LEVEL4, LEVEL5]

