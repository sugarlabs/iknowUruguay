# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL1 = [
        7,
        _('Departments'),
        ['lineasDepto'],
        [],
[
    (_('Flores'), _("It's easy")),
    (_('Colonia'), _("It's easy")),
    (_('Florida'), _("It's easy")),
    (_('Canelones'), _("It's easy")),
    (_('Montevideo'), _("It's easy")),
    (_('Soriano'), _("It's easy")),
    (_('San José'), _("It's easy"))	
]
]

LEVEL2 = [
        1,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('the city of %s') % _('San José de Mayo'), 2, _('San José de Mayo'), _("It's the capital of\nthe department")),
    (_('the town of %s') % _('Mal Abrigo'), 2, _('Mal Abrigo'), _("It's in the northwest")),
    (_('the town of %s') % _('Carreta Quemada'), 2, _('Carreta Quemada'), _("It's in the northeast")),
    (_('the town of %s') % _('Estación González'), 2, _('Estación González'), _("It's in the west")),
    (_('the town of %s') % _('Juan Soler'), 2, _('Juan Soler'), _('Está en el centro')),
    (_('the town of %s') % _('Raigon'), 2, _('Raigon'), _('Está en el centro')),
    (_('the city of %s') % _('Ecilda Paullier'), 2, _('Ecilda Paullier'), _("It's in the southwest")),
    (_('the town of %s') % _('Villa Rodríguez'), 2, _('Villa Rodríguez'), _('Está en el centro')),
    (_('the town of %s') % _('Ituzaingó'), 2, _('Ituzaingó'), _("It's in the east")),
    (_('the town of %s') % _('Capurro'), 2, _('Capurro'), _("It's in the east")),
    (_('the town of %s') % _('Puntas de Valdez'), 2, _('Puntas de Valdez'), _("It's in the southeast")),
    (_('the town of %s') % _('Rafael Perazza'), 2, _('Rafael Perazza'), _("It's in the south")),
    (_('the town of %s') % _('Rincón del Pino'), 2, _('Rincón del Pino'), _("It's in the south")),
    (_('the health resort of %s') % _('Kiyú'), 2, _('Kiyú'), _('Está sobre el\nRío de la Plata')),
    (_('the health resort of %s') % _('Ordeig'), 2, _('Ordeig'), _('Está sobre el\nRío de la Plata')),
    (_('the city of %s') % _('Libertad'), 2, _('Libertad'), _("It's in the south")),
    (_('the town of %s') % _('Delta del Tigre'), 2, _('Delta del Tigre'), _('Está en la desembocadura\ndel Río Santa Lucía')),
    (_('the %s') % _('Ciudad del Plata'), 2, _('Ciudad del Plata'), _("It's in the south")),
    (_('the town of %s') % _('Playa Pascual'), 2, _('Playa Pascual'), _('Está sobre el\nRío de la Plata'))	
]
]

LEVEL3 = [
        15,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('Río de la Plata'), _("It's in the south")),
    (_('Río Santa Lucía'), _("It's in the east")),
    (_('Río San José'), _('Está en el centro')),
    (_('Arroyo de la Virgen'), _("It's in the east")),
    (_('Arroyo Mahoma'), _("It's in the northwest")),
    (_('Arroyo Guaycurú'), _("It's in the northwest")),
    (_('Arroyo Chamizo'), _("It's in the north")),
    (_('Arroyo Cerro'), _("It's in the north")),
    (_('Arroyo Carreta Quemada'), _("It's in the northeast")),
    (_('Arroyo Tala Grande'), _("It's in the northwest")),
    (_('Arroyo Cufré'), _("It's in the southwest")),
    (_('Arroyo Escudero'), _("It's in the west")),
    (_('Arroyo Pavón'), _("It's in the west")),
    (_('Arroyo Toscaso'), _("It's in the southwest")),
    (_('Arroyo Pereira'), _("It's in the south")),
    (_('Arroyo San Gregorio'), _("It's in the south")),
    (_('Arroyo Tigre'), _("It's in the southeast")),
    (_('Arroyo Cagancha'), _("It's in the east")),
    (_('Arroyo del Tala'), _("It's in the east"))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %(f)s') % {'f': _('Cuchilla Guaycurú')}, 4, _('Cuchilla Guaycurú'), _('Try again')),
    (_('the %(f)s') % {'f': _('Sierra Mahoma')}, 4, _('Sierra Mahoma'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla del Tala')}, 4, _('Cuchilla del Tala'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla Mangrullo')}, 4, _('Cuchilla Mangrullo'), _('Try again')),
    (_('the %(m)s') % {'m': _('Cerro Clara')}, 5, _('Cerro Clara'), _("It's in the north")),
    (_('the %(m)s') % {'m': _('Cerro San José')}, 5, _('Cerro San José'), _("It's in the center"))
]
]

LEVEL5 = [
        5,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('Route %s') % 1, _('Va hasta Montevideo')),
    (_('Route %s') % 3, _('Va hacia el norte')),
    (_('Route %s') % 11, _('Pasa por Santa Lucía')),
    (_('Route %s') % 23, _('Pasa por Ismael Cortinas')),
    (_('Route %s') % 45, _('Pasa por Villa Rodríguez'))
]
]

LEVELS = [LEVEL1, LEVEL2, LEVEL3, LEVEL4, LEVEL5]

