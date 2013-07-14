# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL2 = [
        1,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('the city of %s') % _('Treinta y Tres'), 2, _('Treinta y Tres'), _("It's the capital of\nthe department")),
    (_('the city of %s') % _('Santa Clara de Olimar'), 2, _('Santa Clara de Olimar'), _("It's in the northwest")),
    (_('the town of %s') % _('Rincón'), 2, _('Rincón'), _("It's in the northeast")),
    (_('the city of %s') % _('Vergara'), 2, _('Vergara'), _("It's in the northeast")),
    (_('the town of %s') % _('Isla Patrulla'), 2, _('Isla Patrulla'), _("It's in the center")),
    (_('the town of %s') % _('El Oro'), 2, _('El Oro'), _("It's in the center")),
    (_('the city of %s') % _('Cerro Chato'), 2, _('Cerro Chato'), _("It's in the west")),
    (_('the town of %s') % _('La Charqueada'), 2, _('La Charqueada'), _("It's in the southeast")),
    (_('the town of %s') % _('Tupambaé'), 2, _('Tupambaé'), _("It's on the border\nwith %s") % _('Cerro Largo')),
    (_('the town of %s') % _('Valentines'), 2, _('Valentines'), _("It's on the border\nwith %s") % _('Florida'))
]
]

LEVEL3 = [
        15,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('Río Olimar Grande'), _("It's in the south")),
    (_('Río Olimar Chico'), _("It's in the southwest")),
    (_('Río Tacuarí'), _("It's in the northeast")),
    (_('Río Cebollatí'), _("It's in the southeast")),
    (_('Arroyo Corrales'), _("It's in the south")),
    (_('Arroyo Sarandí Grande'), _("It's in the northeast")),
    (_('Arroyo Sarandí Chico'), _("It's in the northeast")),
    (_('Arroyo Ayala'), _("It's in the east")),
    (_('Arroyo del Parao'), _("It's in the north")),
    (_('Arroyo Corrales del Parao'), _("It's in the center")),
    (_('Arroyo Leoncho'), _("It's in the north")),
    (_('Arroyo Olazo'), _("It's in the north")),
    (_('Arroyo Yerbal Grande'), _("It's in the center")),
    (_('Arroyo Yerbal Chico'), _("It's in the center")),
    (_('Arroyo de los Porongos'), _("It's in the center")),
    (_('Arroyo de los Ceibos'), _("It's in the center")),
    (_('Arroyo de las Pavas'), _("It's in the west")),
    (_('Arroyo de las Averías'), _("It's in the east")),
    (_('Arroyo Avestruz Grande'), _("It's in the west"))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %(f)s') % {'f': _('Cuchilla Grande')}, 4, _('Cuchilla Grande'), _('Try again')),
    (_('the %(f)s') % {'f': _('Asperezas del Yerbal')}, 4, _('Asperezas del Yerbal'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla del Carmen')}, 4, _('Cuchilla del Carmen'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla de Palomeque')}, 4, _('Cuchilla de Palomeque'), _('Try again')),
    (_('the %(m)s') % {'m': _('Cerro Valentín')}, 5, _('Cerro Valentín'), _("It's on the border\nwith %s") % _('Florida')),
    (_('the %(m)s') % {'m': _('Cerro Chato')}, 5, _('Cerro Chato'), _("It's in the west")),
    (_('the %(m)s') % {'m': _('Cerro del Olimar')}, 5, _('Cerro del Olimar'), _("It's in the center"))
]
]

LEVEL5 = [
        5,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('Route %s') % 8, _('Passes through departmental capital')),
    (_('Route %s') % 19, _('Comes from %s') % _('Florida')),
    (_('Route %s') % 7, _('Passes through the limit with %s') % _('Florida')),
    (_('Route %s') % 98, _('Passes through %s') % _('Isla Patrulla')),
    (_('Route %s') % 18, _('Passes through %s') % _('Vergara')),
    (_('Route %s') % 17, _('Passes through %s') % _('La Charqueada'))
]
]

LEVELS = [LEVEL2, LEVEL3, LEVEL4, LEVEL5]

