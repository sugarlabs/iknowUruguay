# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL2 = [
        1,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('the city of %s') % _('Paysandú'), 2, _('Paysandú'), _("It's the capital of\nthe department")),
    (_('the town of %s') % _('Chapicuy'), 2, _('Chapicuy'), _("It's in the northwest")),
    (_('the town of %s') % _('Bella Vista'), 2, _('Bella Vista'), _("It's in the northwest")),
    (_('the town of %s') % _('Pueblo Gallinal'), 2, _('Pueblo Gallinal'), _("It's in the northwest")),
    (_('the city of %s') % _('Cerro Chato'), 2, _('Cerro Chato'), _("It's in the northwest")),
    (_('the city of %s') % _('Quebracho'), 2, _('Quebracho'), _("It's in the northwest")),
    (_('the town of %s') % _('Soto'), 2, _('Soto'), _("It's in the northwest")),
    (_('the town of %s') % _('El Eucalipto'), 2, _('El Eucalipto'), _("It's in the north")),
    (_('the town of %s') % _('Tambores'), 2, _('Tambores'), _("It's in the northeast")),
    (_('the town of %s') % _('Guarapirú'), 2, _('Guarapirú'), _("It's in the north")),
    (_('the town of %s') % _('Queguayar'), 2, _('Queguayar'), _("It's in the west")),
    (_('the town of %s') % _('Lorenzo Geyres'), 2, _('Lorenzo Geyres'), _("It's in the west")),
    (_('the town of %s') % _('Cuchilla del Fuego'), 2, _('Cuchilla del Fuego'), _("It's in the center")),
    (_('the town of %s') % _('Piedra Sola'), 2, _('Piedra Sola'), _("It's in the east")),
    (_('the town of %s') % _('Constancia'), 2, _('Constancia'), _("It's in the southwest")),
    (_('the town of %s') % _('Curapí'), 2, _('Curapí'), _("It's in the southwest")),
    (_('the town of %s') % _('Esperanza'), 2, _('Esperanza'), _("It's in the southwest")),
    (_('the town of %s') % _('Porvenir'), 2, _('Porvenir'), _("It's in the southwest")),
    (_('the city of %s') % _('Piedras Coloradas'), 2, _('Piedras Coloradas'), _("It's in the south")),
    (_('the town of %s') % _('Orgoroso'), 2, _('Orgoroso'), _("It's in the south")),
    (_('the town of %s') % _('Arroyo Negro'), 2, _('Arroyo Negro'), _("It's in the south")),
    (_('the town of %s') % _('La Tentación'), 2, _('La Tentación'), _("It's in the southwest")),
    (_('the city of %s') % _('Guichón'), 2, _('Guichón'), _("It's in the south")),
    (_('the town of %s') % _('Beisso'), 2, _('Beisso'), _("It's in the south")),
    (_('the town of %s') % _('Tres Arboles'), 2, _('Tres Arboles'), _("It's in the southeast")),
    (_('the town of %s') % _('Tiatucurá'), 2, _('Tiatucurá'), _("It's in the southeast"))
]
]

LEVEL3 = [
        15,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('Río Uruguay'), _("It's in the west")),
    (_('Río Daymán'), _("It's in the northwest")),
    (_('Río Queguay Grande'), _("It's in the west")),
    (_('Río Queguay Chico'), _("It's in the center")),
    (_('Arroyo Guaviyú'), _("It's in the northwest")),
    (_('Arroyo Quebracho Grande'), _("It's in the west")),
    (_('Arroyo Araujo'), _("It's in the west")),
    (_('Arroyo de Soto'), _("It's in the west")),
    (_('Arroyo Buricayupí'), _("It's in the center")),
    (_('Arroyo Carumbé'), _("It's in the northwest")),
    (_('Arroyo San Francisco Grande'), _("It's in the southwest")),
    (_('Arroyo Negro'), _("It's in the southwest")),
    (_('Arroyo Rabón'), _("It's in the southwest")),
    (_('Arroyo Valdés'), _("It's in the southwest")),
    (_('Arroyo Celestina'), _("It's in the southwest")),
    (_('Arroyo Bacacuá Grande'), _("It's in the center")),
    (_('Arroyo Ñacurutú Grande'), _("It's in the south")),
    (_('Arroyo de la Capilla'), _("It's in the center")),
    (_('Arroyo Guayabos'), _("It's in the south")),
    (_('Arroyo Santa Ana'), _("It's in the south")),
    (_('Arroyo de los Corrales'), _("It's in the southeast")),
    (_('Arroyo de los Molles'), _("It's in the center")),
    (_('Arroyo Zapatero'), _("It's in the east")),
    (_('Arroyo Juan Tomás'), _("It's in the southeast")),
    (_('Arroyo Salsipuedes Grande'), _("It's in the southeast")),
    (_('Arroyo Molles Grande'), _("It's in the center")),
    (_('Arroyo Molles Chico'), _("It's in the north")),
    (_('Arroyo Gualeguay'), _("It's in the center")),
    (_('Arroyo Guarapirú'), _("It's in the center"))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %(f)s') % {'f': _('Cuchilla del Queguay')}, 4, _('Cuchilla del Queguay'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla de Haedo')}, 4, _('Cuchilla de Haedo'), _('Try again')),
    (_('the %(m)s') % {'m': _('Cerro de los Difuntos')}, 5, _('Cerro de los Difuntos'), _("It's in the west")),
    (_('the %(m)s') % {'m': _('Cerro Buricayupí')}, 5, _('Cerro Buricayupí'), _("It's in the center")),
    (_('the %(m)s') % {'m': _('Cerro de la Glorieta')}, 5, _('Cerro de la Glorieta'), _("It's in the north")),
    (_('the %(m)s') % {'m': _('Cerro del Vigía')}, 5, _('Cerro del Vigía'), _("It's in the northeast")),
    (_('the %(m)s') % {'m': _('Cerro Campana')}, 5, _('Cerro Campana'), _("It's in the northeast")),
    (_('the %(m)s') % {'m': _('Cerro Arbolito')}, 5, _('Cerro Arbolito'), _("It's in the east")),
    (_('the %(m)s') % {'m': _('Cerro del Toro')}, 5, _('Cerro del Toro'), _("It's in the south")),
    (_('the %(m)s') % {'m': _('Cerro Palmera Sola')}, 5, _('Cerro Palmera Sola'), _("It's in the south")),
    (_('the %(f)s') % {'f': _('Meseta de Artigas')}, 5, _('Meseta de Artigas'), _("It's in the west"))
]
]

LEVEL5 = [
        5,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('Route %s') % 3, _('Try again')),
    (_('Route %s') % 26, _("It's in the north")),
    (_('Route %s') % 4, _('Try again')),
    (_('Route %s') % 90, _('Try again')),
    (_('Route %s') % 24, _('Try again'))
]
]

LEVELS = [LEVEL2, LEVEL3, LEVEL4, LEVEL5]

