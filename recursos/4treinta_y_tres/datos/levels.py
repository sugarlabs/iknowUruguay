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
    (_('the town of %s') % _('Isla Patrulla'), 2, _('Isla Patrulla'), _('Está en el centro')),
    (_('the town of %s') % _('El Oro'), 2, _('El Oro'), _('Está en el centro')),
    (_('the city of %s') % _('Cerro Chato'), 2, _('Cerro Chato'), _("It's in the west")),
    (_('the town of %s') % _('La Charqueada'), 2, _('La Charqueada'), _("It's in the southeast")),
    (_('the town of %s') % _('Tupambaé'), 2, _('Tupambaé'), _('Está en el límite\ncon Cerro Largo')),
    (_('the town of %s') % _('Valentines'), 2, _('Valentines'), _('Está en el límite\ncon Florida'))
]
]

LEVEL3 = [
        15,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('Olimar Gr.'), _("It's in the south")),
    (_('Olimar Ch. River'), _("It's in the southwest")),
    (_('Tacuarí'), _("It's in the northeast")),
    (_('Cebollatí'), _("It's in the southeast")),
    (_('Corrales'), _("It's in the south")),
    (_('Sarandí Gr.'), _("It's in the northeast")),
    (_('Sarandí Ch.'), _("It's in the northeast")),
    (_('Ayala'), _("It's in the east")),
    (_('del Parao'), _("It's in the north")),
    (_('Corrales del Parao'), _('Está en el centro')),
    (_('Leoncho'), _("It's in the north")),
    (_('Olazo'), _("It's in the north")),
    (_('Yerbal Gr.'), _('Está en el centro')),
    (_('Yerbal Ch.'), _('Está en el centro')),
    (_('de los Porongos'), _('Está en el centro')),
    (_('de los Ceibos'), _('Está en el centro')),
    (_('de las Pavas'), _("It's in the west")),
    (_('de las Averías'), _("It's in the east")),
    (_('Avestruz Gr.'), _("It's in the west"))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %s') % _('Cuchilla Grande'), 4, _('Cuchilla Grande'), _('Try again')),
    (_('the %s') % _('Asperezas del Yerbal'), 4, _('Asperezas del Yerbal'), _('Try again')),
    (_('the %s') % _('Cuchilla del Carmen'), 4, _('Cuchilla del Carmen'), _('Try again')),
    (_('the %s') % _('Cuchilla de Palomeque'), 4, _('Cuchilla de Palomeque'), _('Try again')),
    (_('the %s') % _('Cerro Valentín'), 5, _('Co. Valentín'), _('Está en límite\ncon Florida')),
    (_('the %s') % _('Cerro Chato'), 5, _('Co. Chato'), _("It's in the west")),
    (_('the %s') % _('Cerro del Olimar'), 5, _('Co. del Olimar'), _("It's in the center"))
]
]

LEVEL5 = [
        5,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('Route %s') % 8, _('Pasa por la capital\ndepartamental')),
    (_('Route %s') % 19, _('Viene de Florida')),
    (_('Route %s') % 7, _('Pasa por el límite\ncon Florida')),
    (_('Route %s') % 98, _('Pasa por Isla Patrulla')),
    (_('Route %s') % 18, _('Pasa por Vergara')),
    (_('Route %s') % 17, _('Pasa por La Charqueada'))
]
]

LEVELS = [LEVEL2, LEVEL3, LEVEL4, LEVEL5]

