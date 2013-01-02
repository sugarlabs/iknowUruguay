# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL1 = [
        1,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('the city of %s') % _('Maldonado'), 2, _('Maldonado'), _("It's the capital of\nthe department")),
    (_('the town of %s') % _('Los Talas'), 2, _('Los Talas'), _("It's in the north")),
    (_('the town of %s') % _('Aiguá'), 2, _('Aiguá'), _("It's in the north")),
    (_('the resort of %s') % _('José Ignacio'), 2, _('José Ignacio'), _("It's in the south")),
    (_('the city of %s') % _('San Carlos'), 2, _('San Carlos'), _("It's in the south")),
    (_('the city of %s') % _('Punta del Este'), 2, _('Punta del Este'), _("It's in the south")),
    (_('the city of %s') % _('Pan de Azúcar'), 2, _('Pan de Azúcar'), _("It's in the south")),
    (_('the city of %s') % _('Piriápolis'), 2, _('Piriápolis'), _("It's in the south")),
    (_('the resort of %s') % _('Punta Ballena'), 2, _('Punta Ballena'), _("It's in the south")),
    (_('the town of %s') % _('Garzón'), 2, _('Garzón'), _("It's in the east")),
    (_('the resort of %s') % _('Las Flores'), 2, _('Las Flores'), _("It's in the southwest")),
    (_('the resort of %s') % _('La Barra'), 2, _('La Barra'), _("It's in the south"))
]
]

LEVEL2 = [
        15,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('Río de la Plata'), _("It's in the south")),
    (_('Atlantic Ocean'), _("It's in the south")),
    (_('Arroyo Garzón'), _("It's in the southeast")),
    (_('Arroyo de Rocha'), _("It's in the east")),
    (_('Arroyo Valdivia'), _("It's in the east")),
    (_('Arroyo del Alferez'), _("It's in the east")),
    (_('Arroyo del Aiguá'), _("It's in the north")),
    (_('Arroyo Sarandí'), _("It's in the north")),
    (_('Arroyo del León'), _("It's in the north")),
    (_('Arroyo Solís Grande'), _("It's in the southwest")),
    (_('Arroyo Coronilla'), _("It's in the center")),
    (_('Arroyo Sauce'), _("It's in the southwest")),
    (_('Arroyo Pan de Azúcar'), _("It's in the south")),
    (_('Arroyo del Sauce'), _("It's in the south")),
    (_('Arroyo Mataojo'), _("It's in the south")),
    (_('Arroyo de las Cañas'), _("It's in the center")),
    (_('Arroyo de los Caracoles'), _("It's in the center")),
    (_('Arroyo de los Carpés'), _("It's in the center")),
    (_('Arroyo San Carlos'), _("It's in the south")),
    (_('Arroyo Maldonado'), _("It's in the south")),
    (_('Arroyo José Ignacio'), _("It's in the southeast"))
]
]

LEVEL3 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %(f)s') % {'f': _('Sierra de las Cañas')}, 4, _('Sierra de las Cañas'), _('Try again')),
    (_('the %(f)s') % {'f': _('Sierra de los Caracoles')}, 4, _('Sierra de los Caracoles'), _('Try again')),
    (_('the %(f)s') % {'f': _('Sierra de las Ánimas')}, 4, _('Sierra de las Ánimas'), _('Try again')),
    (_('the %(f)s') % {'f': _('Sierra de la Ballena')}, 4, _('Sierra de la Ballena'), _('Try again')),
    (_('the %(f)s') % {'f': _('Sierra de Carapé')}, 4, _('Sierra de Carapé'), _('Try again')),
    (_('the %(m)s') % {'m': _('Cerro del Toro')}, 5, _('Cerro del Toro'), _("It is near %s") % _('Piriápolis')),
    (_('the %(m)s') % {'m': _('Cerro San Antonio')}, 5, _('Cerro San Antonio'), _("It is near %s") % _('Piriápolis')),
    (_('the %(m)s') % {'m': _('Cerro Pan de Azúcar')}, 5, _('Cerro Pan de Azúcar'), _("It's in the south")),
    (_('the %(m)s') % {'m': _('Cerro Catedral')}, 5, _('Cerro Catedral'), _("It's the highest in Uruguay"))
]
]

LEVEL4 = [
        5,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('Route %s') % 9, _('Try again')),
    (_('Route %s') % 'IB', _('Try again')),
    (_('Route %s') % 60, _('Try again')),
    (_('Route %s') % 37, _('Try again')),
    (_('Route %s') % 12, _('Try again')),
    (_('Route %s') % 93, _('Passes through %s') % _('major resort')),
    (_('Route %s') % 39, _('Passes through %s') % _('San Carlos')),
    (_('Route %s') % 13, _('Passes through %s') % _('Aiguá')),
    (_('Route %s') % 109, _('Passes through %s') % _('Aiguá'))
]
]

LEVELS = [LEVEL1, LEVEL2, LEVEL3, LEVEL4]

