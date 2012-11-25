# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL2 = [
        1,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('the city of %s') % _('Treinta y Tres'), 1, _('Treinta y Tres'), _('Es la capital del\ndepartamento')),
    (_('the city of %s') % _('Santa Clara de Olimar'), 2, _('Santa Clara de Olimar'), _("It's in the northwest")),
    (_('the town of %s') % _('Rincón'), 2, _('Rincón'), _("It's in the northeast")),
    (_('the city of %s') % _('Vergara'), 2, _('Vergara'), _("It's in the northeast")),
    (_('the town of %s') % _('Isla Patrulla'), 2, _('Isla Patrulla'), _('Está en el centro')),
    (_('the town of %s') % _('El Oro'), 2, _('El Oro'), _('Está en el centro')),
    (_('the city of %s') % _('Cerro Chato'), 2, _('Cerro Chato'), _("It's in the west")),
    (_('the town of %s') % _('La Charqueada'), 2, _('La Charqueada'), _("It's in the southeast")),
    (_('the town of %s') % _('Tupambaé'), 2, _('Tupambaé'), _('Está en el límite\ncon Cerro Largo')),
    (_('the town of %s') % _('Valentines'), 2, _('Valentines'), _('Está en el límite\ncon Florida'))
]
]

LEVEL3 = [
        1,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('the %s') % _('Río Olimar Gr.'), 3, _('Río Olimar Gr.'), _("It's in the south")),
    (_('the %s') % _('Río Olimar Ch.'), 3, _('Río Olimar Ch.'), _("It's in the southwest")),
    (_('the %s') % _('Río Tacuarí'), 3, _('Río Tacuarí'), _("It's in the northeast")),
    (_('the %s') % _('Río Cebollatí'), 3, _('Río Cebollatí'), _("It's in the southeast")),
    (_('the %s') % _('Arroyo Corrales'), 3, _('A. Corrales'), _("It's in the south")),
    (_('the %s') % _('Arroyo Sarandí Grande'), 3, _('A. Sarandí Gr.'), _("It's in the northeast")),
    (_('the %s') % _('Arroyo Sarandí Chico'), 3, _('A. Sarandí Ch.'), _("It's in the northeast")),
    (_('the %s') % _('Arroyo Ayala'), 3, _('A. Ayala'), _("It's in the east")),
    (_('the %s') % _('Arroyo del Parao'), 3, _('A. del Parao'), _("It's in the north")),
    (_('the %s') % _('Arroyo Corrales del Parao'), 3, _('A. Corrales del Parao'), _('Está en el centro')),
    (_('the %s') % _('Arroyo Leoncho'), 3, _('A. Leoncho'), _("It's in the north")),
    (_('the %s') % _('Arroyo Olazo'), 3, _('A. Olazo'), _("It's in the north")),
    (_('the %s') % _('Arroyo Yerbal Grande'), 3, _('A. Yerbal Gr.'), _('Está en el centro')),
    (_('the %s') % _('Arroyo Yerbal Chico'), 3, _('A. Yerbal Ch.'), _('Está en el centro')),
    (_('the %s') % _('Arroyo de los Porongos'), 3, _('A. de los Porongos'), _('Está en el centro')),
    (_('the %s') % _('Arroyo de los Ceibos'), 3, _('A. de los Ceibos'), _('Está en el centro')),
    (_('the %s') % _('Arroyo de las Pavas'), 3, _('A. de las Pavas'), _("It's in the west")),
    (_('the %s') % _('Arroyo de las Averías'), 3, _('A. de las Averías'), _("It's in the east")),
    (_('the %s') % _('Arroyo Avestruz Gr.'), 3, _('A. Avestruz Gr.'), _("It's in the west")),
    (_('the %s') % _('Laguna Merín'), 3, _('Lag. Merín'), _('Está al Está al este'))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %s') % _('Cuchilla Grande'), 4, _('Cuchilla Grande'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Asperezas del Yerbal'), 4, _('Asperezas del Yerbal'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cuchilla del Carmen'), 4, _('Cuchilla del Carmen'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cuchilla de Palomeque'), 4, _('Cuchilla de Palomeque'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cerro Valentín'), 5, _('Co. Valentín'), _('Está en límite\ncon Florida')),
    (_('the %s') % _('Cerro Chato'), 5, _('Co. Chato'), _("It's in the west")),
    (_('the %s') % _('Cerro del Olimar'), 5, _('Co. del Olimar'), _('Está en el centro'))
]
]

LEVEL5 = [
        1,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('the %s') % _('Ruta 8'), 6, _('Ruta 8'), _('Pasa por la capital\ndepartamental')),
    (_('the %s') % _('Ruta 19'), 6, _('Ruta 19'), _('Viene de Florida')),
    (_('the %s') % _('Ruta 7'), 6, _('Ruta 7'), _('Pasa por el límite\ncon Florida')),
    (_('the %s') % _('Ruta 98'), 6, _('Ruta 98'), _('Pasa por Isla Patrulla')),
    (_('the %s') % _('Ruta 18'), 6, _('Ruta 18'), _('Pasa por Vergara')),
    (_('the %s') % _('Ruta 17'), 6, _('Ruta 17'), _('Pasa por La Charqueada'))
]
]

LEVELS = [LEVEL2, LEVEL3, LEVEL4, LEVEL5]

