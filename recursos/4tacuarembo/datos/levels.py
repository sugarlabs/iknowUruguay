# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL1 = [
        7,
        _('Departments'),
        ['lineasDepto'],
        [],
[
    (_('Artigas'), _("It's easy")),
    (_('Rivera'), _("It's easy")),
    (_('Cerro Largo'), _("It's easy")),
    (_('Durazno'), _("It's easy")),
    (_('Río Negro'), _("It's easy")),
    (_('Paysandú'), _("It's easy")),
    (_('Salto'), _("It's easy")),
    (_('Tacuarembó'), _("It's easy")),
    (_('Treinta y Tres'), _("It's easy"))
]
]

LEVEL2 = [
        1,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('the city of %s') % _('Tacuarembó'), 2, _('Tacuarembó'), _("It's the capital of\nthe department")),
    (_('the town of %s') % _('Paso del Cerro'), 2, _('Paso del Cerro'), _("It's in the north")),
    (_('the city of %s') % _('Ansina'), 2, _('Ansina'), _("It's in the northeast")),
    (_('the town of %s') % _('Piedra Sola'), 2, _('Piedra Sola'), _("It's in the west")),
    (_('the town of %s') % _('Curtina'), 2, _('Curtina'), _("It's in the center")),
    (_('the town of %s') % _('Achar'), 2, _('Achar'), _("It's in the southwest")),
    (_('the town of %s') % _('Peralta'), 2, _('Peralta'), _("It's in the southwest")),
    (_('the resort of %s') % _('San Gregorio de Polanco'), 2, _('San Gregorio de Polanco'), _("It's in the south")),
    (_('the town of %s') % _('Rincón de Pereira'), 2, _('Rincón de Pereira'), _("It's in the southeast")),
    (_('the city of %s') % _('Paso de los Toros'), 2, _('Paso de los Toros'), _("It's in the southwest")),
    (_('the town of %s') % _('Cuchilla de Caraguatá'), 2, _('Cuchilla de Caraguatá'), _("It's in the southeast")),
    (_('the town of %s') % _('Picada de Cuello'), 2, _('Picada de Cuello'), _("It's in the east")),
    (_('the town of %s') % _('Valle Edén'), 2, _('Valle Edén'), _("It's in the west")),
    (_('the town of %s') % _('Martinote'), 2, _('Martinote'), _("It's in the center"))
]
]

LEVEL3 = [
        15,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('Río Tacuarembó'), _("It's in the center")),
    (_('Río Negro'), _("It's in the south")),
    (_('Arroyo Salsipuedes Grande'), _("It's in the southwest")),
    (_('Arroyo Salsipuedes Chico'), _("It's in the southeast")),
    (_('Arroyo Cardoso'), _("It's in the southwest")),
    (_('Arroyo Malo'), _("It's in the west")),
    (_('Arroyo de la Quebrada'), _("It's in the center")),
    (_('Arroyo Rolón'), _("It's in the southwest")),
    (_('Arroyo de Clara'), _("It's in the south")),
    (_('Arroyo Caraguatá'), _("It's in the southeast")),
    (_('Arroyo Yaguarí'), _("It's in the east")),
    (_('Arroyo de los Sauces'), _("It's in the east")),
    (_('Arroyo Laureles'), _("It's in the north")),
    (_('Arroyo Tacuarembó Chico'), _("It's in the northwest")),
    (_('Arroyo Tranqueras'), _("It's in the northwest")),
    (_('Arroyo Batoví'), _("It's in the center")),
    (_('Arroyo Tres Cruces'), _("It's in the northwest")),
    (_('Arroyo Cañas'), _("It's in the north"))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %(f)s') % {'f': _('Cuchilla de las Tres Cruces')}, 4, _('Cuchilla de las Tres Cruces'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla de Yaguarí')}, 4, _('Cuchilla de Yaguarí'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla del Caraguata')}, 4, _('Cuchilla del Caraguata'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla de Peralta')}, 4, _('Cuchilla de Peralta'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla de Haedo')}, 4, _('Cuchilla de Haedo'), _('Try again')),
    (_('the %(m)s') % {'m': _('Cerro de las Minas')}, 5, _('Cerro de las Minas'), _("It's in the west")),
    (_('the %(m)s') % {'m': _('Cerros de Batoví')}, 5, _('Cerros de Batoví'), _('Try again')),
    (_('the %(m)s') % {'m': _('Cerro Lambaré')}, 5, _('Cerro Lambaré'), _("It's in the northwest")),
    (_('the %(m)s') % {'m': _('Cerro del Ñandubal')}, 5, _('Cerro del Ñandubal'), _("It's in the northeast"))
]
]

LEVEL5 = [
        5,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('Route %s') % 5, _('Try again')),
    (_('Route %s') % 6, _("Ends in %s") % _('Cuchilla de Caraguatá')),
    (_('Route %s') % 26, _('Passes through %s') % _('Ansina')),
    (_('Route %s') % 31, _('Try again')),
    (_('Route %s') % 43, _("Ends in %s") % _('San Gregorio de Polanco')),
    (_('Route %s') % 20, _('Try again'))
]
]

LEVELS = [LEVEL1, LEVEL2, LEVEL3, LEVEL4, LEVEL5]

