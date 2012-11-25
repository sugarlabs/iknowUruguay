# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL1 = [
        7,
        _('Departments'),
        ['lineasDepto'],
        [],
[
    (_('Durazno'), _("It's easy")),
    (_('Soriano'), _("It's easy")),
    (_('Flores'), _("It's easy")),
    (_('Colonia'), _("It's easy")),
    (_('San José'), _("It's easy")),
    (_('Florida'), _("It's easy"))
]
]

LEVEL2 = [
        1,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('the city of %s') % _('Trinidad'), 2, _('Trinidad'), _('Es la capital del\ndepartamento')),
    (_('the town of %s') % _('Andresito'), 2, _('Andresito'), _("It's in the north")),
    (_('the town of %s') % _('Juan José Castro'), 2, _('Juan José Castro'), _('Está en el centro')),
    (_('the town of %s') % _('Cerro Colorado'), 2, _('Cerro Colorado'), _('Está en el centro')),
    (_('the town of %s') % _('La Casilla'), 2, _('La Casilla'), _("It's in the south")),
    (_('the town of %s') % _('San Gregorio'), 2, _('San Gregorio'), _("It's in the south")),
    (_('the town of %s') % _('Ismael Cortinas'), 2, _('Ismael Cortinas'), _("It's in the southwest"))
]
]

LEVEL3 = [
        1,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('the %s') % _('Río San José'), 3, _('Río San José'), _("It's in the south")),
    (_('the %s') % _('Río Yí'), 3, _('Río Yí'), _("It's in the northeast")),
    (_('the %s') % _('Río Negro'), 3, _('Río Negro'), _("It's in the north")),
    (_('the %s') % _('Arroyo Grande'), 3, _('A. Grande'), _("It's in the west")),
    (_('the %s') % _('Arroyo Marincho'), 3, _('A. Marincho'), _("It's in the northwest")),
    (_('the %s') % _('Arroyo Coronilla'), 3, _('A. Coronilla'), _("It's in the north")),
    (_('the %s') % _('Arroyo Sarandi'), 3, _('A. Sarandi'), _("It's in the north")),
    (_('the %s') % _('Arroyo Porongos'), 3, _('A. Porongos'), _("It's in the northeast")),
    (_('the %s') % _('Arroyo del Sarandí'), 3, _('A. del Sarandí'), _('Está en el centro')),
    (_('the %s') % _('Arroyo del Tala'), 3, _('A. del Tala'), _("It's in the east")),
    (_('the %s') % _('Arroyo San Gregorio'), 3, _('A. San Gregorio'), _("It's in the south")),
    (_('the %s') % _('Arroyo Pintos'), 3, _('A. Pintos'), _("It's in the south")),
    (_('the %s') % _('Arroyo Bolas Gr.'), 3, _('A. Bolas Gr.'), _("It's in the south")),
    (_('the %s') % _('Arroyo Juncal'), 3, _('A. Juncal'), _("It's in the south")),
    (_('the %s') % _('Arroyo del Sauce'), 3, _('A. del Sauce'), _("It's in the southwest")),
    (_('the %s') % _('Arroyo Ojosmín'), 3, _('A. Ojosmín'), _("It's in the southwest")),
    (_('the %s') % _('Arroyo Guardia Vieja'), 3, _('A. Guardia Vieja'), _("It's in the west")),
    (_('the %s') % _('Arroyo Manantiales'), 3, _('A. Manantiales'), _("It's in the west")),
    (_('the %s') % _('Arroyo Arenal Ch.'), 3, _('A. Arenal Ch.'), _("It's in the west")),
    (_('the %s') % _('Arroyo Sauce'), 3, _('A. Sauce'), _("It's in the northwest")),
    (_('the %s') % _('Arroyo Tala'), 3, _('A. Tala'), _("It's in the north")),
    (_('the %s') % _('Arroyo Malo'), 3, _('A. Malo'), _("It's in the north")),
    (_('the %s') % _('Arroyo de la Cordobesa'), 3, _('A. de la Cordobesa'), _("It's in the east")),
    (_('the %s') % _('Arroyo Duraznito'), 3, _('A. Duraznito'), _("It's in the east")),
    (_('the %s') % _('Arroyo Chamangá'), 3, _('A. Chamangá'), _("It's in the east")),
    (_('the %s') % _('Arroyo de los Ahogados'), 3, _('A. de los Ahogados'), _("It's in the southeast")),
    (_('the %s') % _('Arroyo Piedra Sola'), 3, _('A. Piedra Sola'), _("It's in the southeast")),
    (_('the %s') % _('Arroyo Maciel'), 3, _('A. Maciel'), _("It's in the east")),
    (_('the %s') % _('Arroyo Manguera'), 3, _('A. Manguera'), _("It's in the northeast"))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %s') % _('Cuchilla Marincho'), 4, _('Cuchilla Marincho'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cuchilla Villasboas'), 4, _('Cuchilla Villasboas'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cuchilla Grande Inferior'), 4, _('Cuchilla Grande Inferior'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cerros de Ojosmín'), 5, _('Cos. de Ojosmín'), _('Quedan al oeste'))
]
]

LEVEL5 = [
        1,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('the %s') % _('Ruta 3'), 6, _('Ruta 3'), _('Va de norte a sur')),
    (_('the %s') % _('Ruta 14'), 6, _('Ruta 14'), _('Va hacia el este')),
    (_('the %s') % _('Ruta 57'), 6, _('Ruta 57'), _('Va hacia el suroeste')),
    (_('the %s') % _('Ruta 23'), 6, _('Ruta 23'), _('Pasa por Ismael Cortinas'))
]
]

LEVELS = [LEVEL1, LEVEL2, LEVEL3, LEVEL4, LEVEL5]

