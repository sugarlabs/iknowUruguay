# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL2 = [
        1,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('the city of %s') % _('Rivera'), 1, _('Rivera'), _("It's the capital of\nthe department")),
    (_('the town of %s') % _('Curticeiras'), 2, _('Curticeiras'), _("It's in the north")),
    (_('the city of %s') % _('Tranqueras'), 2, _('Tranqueras'), _("It's in the northwest")),
    (_('the town of %s') % _('La Calera'), 2, _('La Calera'), _("It's in the center")),
    (_('the town of %s') % _('Lapuente'), 2, _('Lapuente'), _("It's in the center")),
    (_('the town of %s') % _('Cerrillada'), 2, _('Cerrillada'), _("It's in the north")),
    (_('the town of %s') % _('Cerro Pelado'), 2, _('Cerro Pelado'), _("It's in the center")),
    (_('the town of %s') % _('Minas de Corrales'), 2, _('Minas de Corrales'), _("It's in the center")),
    (_('the town of %s') % _('Hospital'), 2, _('Hospital'), _("It's in the southeast")),
    (_('the town of %s') % _('Las Flores'), 2, _('Las Flores'), _("It's in the southeast")),
    (_('the town of %s') % _('Vichadero'), 2, _('Vichadero'), _("It's in the southeast"))
]
]

LEVEL3 = [
        15,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('Río Tacuarembó'), _("It's in the northwest")),
    (_('Río Negro'), _("It's in the southeast")),
    (_('Arroyo Laureles'), _("It's in the northwest")),
    (_('Arroyo Tigre'), _("It's in the northwest")),
    (_('Arroyo Médanos'), _("It's in the west")),
    (_('Arroyo Mangueras'), _("It's in the northeast")),
    (_('Arroyo del Ataque'), _("It's in the northeast")),
    (_('Arroyo Batoví Dorado'), _("It's in the northeast")),
    (_('Arroyo Cuñapirú'), _("It's in the north")),
    (_('Arroyo Corrales'), _("It's in the center")),
    (_('Arroyo J. Amarillas'), _("It's in the center")),
    (_('Arroyo Coronilla'), _("It's in the center")),
    (_('Arroyo Carpintería'), _("It's in the south")),
    (_('Arroyo Yaguarí'), _("It's in the center")),
    (_('Arroyo Amarillo'), _("It's in the center")),
    (_('Arroyo Cerro'), _("It's in the center")),
    (_('Arroyo del Hospital'), _("It's in the east")),
    (_('Arroyo San Luis'), _("It's in the east")),
    (_('Arroyo Ceibal'), _("It's in the southeast")),
    (_('Arroyo Zanja Honda'), _("It's in the southeast")),
    (_('Arroyo Blanco'), _("It's in the east")),
    (_('Arroyo Molles'), _("It's in the east")),
    (_('Arroyo Caraguatá'), _("It's in the southeast")),
    (_('Arroyo Cerro Chato'), _("It's in the south"))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %(f)s') % {'f': _('Cuchilla de Cuñapirú')}, 4, _('Cuchilla de Cuñapirú'), _("It's in the center")),
    (_('the %(f)s') % {'f': _('Cuchilla del Yaguarí')}, 4, _('Cuchilla del Yaguarí'), _("It's in the south")),
    (_('the %(f)s') % {'f': _('Cuchilla Negra')}, 4, _('Cuchilla Negra'), _("It's on the border\nwith %s") % _('Artigas')),
    (_('the %(f)s') % {'f': _('Cuchilla de Haedo')}, 4, _('Cuchilla de Haedo'), _("It's in the west")),
    (_('the %(f)s') % {'f': _('Cuchilla de Santa Ana')}, 4, _('Cuchilla de Santa Ana'), _("It's on the border\nwith %s") % _('Brasil')),
    (_('the %(m)s') % {'m': _('Cerro del Hospital')}, 5, _('Cerro del Hospital'), _("It's in the east")),
    (_('the %(m)s') % {'m': _('Cerro Bonito')}, 5, _('Cerro Bonito'), _("It's in the east")),
    (_('the %(m)s') % {'m': _('Cerro de la Cruz')}, 5, _('Cerro de la Cruz'), _("It's in the south")),
    (_('the %(m)s') % {'m': _('Cerro del Medio')}, 5, _('Cerro del Medio'), _("It's on the border\nwith %s") % _('Tacuarembó')),
    (_('the %(m)s') % {'m': _('Cerro de los Peludos')}, 5, _('Cerro de los Peludos'), _("It's in the northwest"))
]
]

LEVEL5 = [
        5,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('Route %s') % 5, _('Passes through %s') % _('the capital')),
    (_('Route %s') % 30, _('Passes through %s') % _('Tranqueras')),
    (_('Route %s') % 29, _('Ends in %s') % _('Minas de Corrales')),
    (_('Route %s') % 27, _('Passes through %s') % _('Cerro Pelado')),
    (_('Route %s') % 6, _('Try again')),
    (_('Route %s') % 28, _('Try again')),
    (_('Route %s') % 44, _('Try again'))
]
]

LEVELS = [LEVEL2, LEVEL3, LEVEL4, LEVEL5]

