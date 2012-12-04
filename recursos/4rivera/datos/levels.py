# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL2 = [
        1,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('the city of %s') % _('Rivera'), 1, _('Rivera'), _('Es la capital del\ndepartamento')),
    (_('the town of %s') % _('Curticeiras'), 2, _('Curticeiras'), _("It's in the north")),
    (_('the city of %s') % _('Tranqueras'), 2, _('Tranqueras'), _("It's in the northwest")),
    (_('the town of %s') % _('La Calera'), 2, _('La Calera'), _('Está en el centro')),
    (_('the town of %s') % _('Lapuente'), 2, _('Lapuente'), _('Está en el centro')),
    (_('the town of %s') % _('Cerrillada'), 2, _('Cerrillada'), _("It's in the north")),
    (_('the town of %s') % _('Cerro Pelado'), 2, _('Cerro Pelado'), _('Está en el centro')),
    (_('the town of %s') % _('Minas de Corrales'), 2, _('Minas de Corrales'), _('Está en el centro')),
    (_('the town of %s') % _('Hospital'), 2, _('Hospital'), _("It's in the southeast")),
    (_('the town of %s') % _('Las Flores'), 2, _('Las Flores'), _("It's in the southeast")),
    (_('the town of %s') % _('Vichadero'), 2, _('Vichadero'), _("It's in the southeast"))
]
]

LEVEL3 = [
        1,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('the %s') % _('Río Tacuarembó'), 3, _('Río Tacuarembó'), _("It's in the northwest")),
    (_('the %s') % _('Río Negro'), 3, _('Río Negro'), _("It's in the southeast")),
    (_('the %s') % _('Arroyo Laureles'), 3, _('A. Laureles'), _("It's in the northwest")),
    (_('the %s') % _('Arroyo Tigre'), 3, _('A. Tigre'), _("It's in the northwest")),
    (_('the %s') % _('Arroyo Médanos'), 3, _('A. Médanos'), _("It's in the west")),
    (_('the %s') % _('Arroyo Mangueras'), 3, _('A. Mangueras'), _("It's in the northeast")),
    (_('the %s') % _('Arroyo del Ataque'), 3, _('A. del Ataque'), _("It's in the northeast")),
    (_('the %s') % _('Arroyo Batoví Dorado'), 3, _('A. Batoví Dorado'), _("It's in the northeast")),
    (_('the %s') % _('Arroyo Cuñapirú'), 3, _('A. Cuñapirú'), _("It's in the north")),
    (_('the %s') % _('Arroyo Corrales'), 3, _('A. Corrales'), _('Está en el centro')),
    (_('the %s') % _('Arroyo J. Amarillas'), 3, _('A. J. Amarillas'), _('Está en el centro')),
    (_('the %s') % _('Arroyo Coronilla'), 3, _('A. Coronilla'), _('Está en el centro')),
    (_('the %s') % _('Arroyo Carpintería'), 3, _('A. Carpintería'), _("It's in the south")),
    (_('the %s') % _('Arroyo Yaguarí'), 3, _('A. Yaguarí'), _('Está en el centro')),
    (_('the %s') % _('Arroyo Amarillo'), 3, _('A. Amarillo'), _('Está en el centro')),
    (_('the %s') % _('Arroyo Cerro'), 3, _('A. Cerro'), _('Está en el centro')),
    (_('the %s') % _('Arroyo del Hospital'), 3, _('A. del Hospital'), _("It's in the east")),
    (_('the %s') % _('Arroyo San Luis'), 3, _('A. San Luis'), _("It's in the east")),
    (_('the %s') % _('Arroyo Ceibal'), 3, _('A. Ceibal'), _("It's in the southeast")),
    (_('the %s') % _('Arroyo Zanja Honda'), 3, _('A. Zanja Honda'), _("It's in the southeast")),
    (_('the %s') % _('Arroyo Blanco'), 3, _('A. Blanco'), _("It's in the east")),
    (_('the %s') % _('Arroyo Molles'), 3, _('A. Molles'), _("It's in the east")),
    (_('the %s') % _('Arroyo Caraguatá'), 3, _('A. Caraguatá'), _("It's in the southeast")),
    (_('the %s') % _('Arroyo Cerro Chato'), 3, _('A. Cerro Chato'), _("It's in the south"))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %s') % _('Cuchilla de Cuñapirú'), 4, _('Cuchilla de Cuñapirú'), _('Está en el centro')),
    (_('the %s') % _('Cuchilla del Yaguarí'), 4, _('Cuchilla del Yaguarí'), _('Queda al sur')),
    (_('the %s') % _('Cuchilla Negra'), 4, _('Cuchilla Negra'), _('Queda en el límite\ncon Artigas')),
    (_('the %s') % _('Cuchilla de Haedo'), 4, _('Cuchilla de Haedo'), _('Queda al oeste')),
    (_('the %s') % _('Cuchilla de Santa Ana'), 4, _('Cuchilla de Santa Ana'), _('Queda en el límite\ncon Brasil')),
    (_('the %s') % _('Cerro del Hospital'), 5, _('Co. del Hospital'), _('Queda al este')),
    (_('the %s') % _('Cerro Bonito'), 5, _('Co. Bonito'), _('Queda al este')),
    (_('the %s') % _('Cerro de la Cruz'), 5, _('Co. de la Cruz'), _('Queda al sur')),
    (_('the %s') % _('Cerro del Medio'), 5, _('Co. del Medio'), _('Queda en el límite\ncon Tacuarembó')),
    (_('the %s') % _('Cerro de los Peludos'), 5, _('Co. de los Peludos'), _('Queda al noroeste'))
]
]

LEVEL5 = [
        5,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('Route %s') % 5, _('Pasa por la capital')),
    (_('Route %s') % 30, _('Pasa por Tranqueras')),
    (_('Route %s') % 29, _('Termina en\nMinas de Corrales')),
    (_('Route %s') % 27, _('Pasa por Cerro Pelado')),
    (_('Route %s') % 6, _('Llega hasta Brasil')),
    (_('Route %s') % 28, _('Pasa por el límite\ncon Tacuarembó')),
    (_('Route %s') % 44, _('Va hacia Cerro Largo'))
]
]

LEVELS = [LEVEL2, LEVEL3, LEVEL4, LEVEL5]

