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
    (_('the city of %s') % _('San José de Mayo'), 2, _('San José de Mayo'), _('Es la capital del\ndepartamento')),
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
        1,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('the %s') % _('Río de la Plata'), 3, _('Río de la Plata'), _("It's in the south")),
    (_('the %s') % _('Río Santa Lucía'), 3, _('Río Santa Lucía'), _("It's in the east")),
    (_('the %s') % _('Río San José'), 3, _('Río San José'), _('Está en el centro')),
    (_('the %s') % _('Arroyo de la Virgen'), 3, _('A. de la Virgen'), _("It's in the east")),
    (_('the %s') % _('Arroyo Mahoma'), 3, _('A. Mahoma'), _("It's in the northwest")),
    (_('the %s') % _('Arroyo Guaycurú'), 3, _('A. Guaycurú'), _("It's in the northwest")),
    (_('the %s') % _('Arroyo Chamizo'), 3, _('A. Chamizo'), _("It's in the north")),
    (_('the %s') % _('Arroyo Cerro'), 3, _('A. Cerro'), _("It's in the north")),
    (_('the %s') % _('Arroyo Carreta Quemada'), 3, _('A. Carreta Quemada'), _("It's in the northeast")),
    (_('the %s') % _('Arroyo Tala Gr.'), 3, _('A. Tala Gr.'), _("It's in the northwest")),
    (_('the %s') % _('Arroyo Cufré'), 3, _('A. Cufré'), _("It's in the southwest")),
    (_('the %s') % _('Arroyo Escudero'), 3, _('A. Escudero'), _("It's in the west")),
    (_('the %s') % _('Arroyo Pavón'), 3, _('A. Pavón'), _("It's in the west")),
    (_('the %s') % _('Arroyo Toscaso'), 3, _('A. Toscaso'), _("It's in the southwest")),
    (_('the %s') % _('Arroyo Pereira'), 3, _('A. Pereira'), _("It's in the south")),
    (_('the %s') % _('Arroyo San Gregorio'), 3, _('A. San Gregorio'), _("It's in the south")),
    (_('the %s') % _('Arroyo S. Gregorio'), 3, _('A. S. Gregorio'), _("It's in the north")),
    (_('the %s') % _('Arroyo Tigre'), 3, _('A. Tigre'), _("It's in the southeast")),
    (_('the %s') % _('Arroyo Cagancha'), 3, _('A. Cagancha'), _("It's in the east")),
    (_('the %s') % _('Arroyo del Tala'), 3, _('A. del Tala'), _("It's in the east"))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %s') % _('Cuchilla Guaycurú'), 4, _('Cuchilla Guaycurú'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Sierra Mahoma'), 4, _('Sierra Mahoma'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cuchilla del Tala'), 4, _('Cuchilla del Tala'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cuchilla Mangrullo'), 4, _('Cuchilla Mangrullo'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cerro Clara'), 5, _('Co. Clara'), _("It's in the north")),
    (_('the %s') % _('Cerro San José'), 5, _('Co. San José'), _('Está en el centro'))
]
]

LEVEL5 = [
        1,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('the %s') % _('Ruta 1'), 6, _('Ruta 1'), _('Va hasta Montevideo')),
    (_('the %s') % _('Ruta 3'), 6, _('Ruta 3'), _('Va hacia el norte')),
    (_('the %s') % _('Ruta 11'), 6, _('Ruta 11'), _('Pasa por Santa Lucía')),
    (_('the %s') % _('Ruta 23'), 6, _('Ruta 23'), _('Pasa por Ismael Cortinas')),
    (_('the %s') % _('Ruta 45'), 6, _('Ruta 45'), _('Pasa por Villa Rodríguez'))
]
]

LEVELS = [LEVEL1, LEVEL2, LEVEL3, LEVEL4, LEVEL5]

