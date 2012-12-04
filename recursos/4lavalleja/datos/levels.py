# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL1 = [
        7,
        _('Departments'),
        ['lineasDepto'],
        [],
[
    (_('Treinta y Tres'), _("It's easy")),
    (_('Florida'), _("It's easy")),
    (_('Canelones'), _("It's easy")),
    (_('Maldonado'), _("It's easy")),
    (_('Rocha'), _("It's easy")),
    (_('Lavalleja'), _("It's easy")),
]
]

LEVEL2 = [
        1,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('the city of %s') % _('Minas'), 2, _('Minas'), _("It's the capital of\nthe department")),
    (_('the town of %s') % _('Batlle y Ordoñez'), 2, _('Batlle y Ordoñez'), _("It's in the northwest")),
    (_('the town of %s') % _('J. P. Varela'), 2, _('J. P. Varela'), _("It's in the northeast")),
    (_('the town of %s') % _('Pirarajá'), 2, _('Pirarajá'), _("It's in the north")),
    (_('the town of %s') % _('Polanco'), 2, _('Polanco'), _('Está en el centro')),
    (_('the town of %s') % _('Gaetán'), 2, _('Gaetán'), _("It's in the west")),
    (_('the town of %s') % _('Mariscala'), 2, _('Mariscala'), _("It's in the east")),
    (_('the town of %s') % _('Villa del Rosario'), 2, _('Villa del Rosario'), _("It's in the south")),
    (_('the town of %s') % _('Solís de Mataojo'), 2, _('Solís de Mataojo'), _("It's in the south"))
]
]

LEVEL3 = [
        1,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('the %s') % _('Río Santa Lucía'), 3, _('Río Santa Lucía'), _("It's in the south")),
    (_('the %s') % _('Río Cebollatí'), 3, _('Río Cebollatí'), _("It's in the west")),
    (_('the %s') % _('Río Olimar Ch.'), 3, _('Río Olimar Ch.'), _("It's in the northwest")),
    (_('the %s') % _('Arroyo del Sauce'), 3, _('A. del Sauce'), _("It's in the northwest")),
    (_('the %s') % _('Arroyo Corrales'), 3, _('A. Corrales'), _("It's in the northeast")),
    (_('the %s') % _('Arroyo Solís Gr.'), 3, _('A. Solís Gr.'), _("It's in the south")),
    (_('the %s') % _('Arroyo Mataojo'), 3, _('A. Mataojo'), _("It's in the south")),
    (_('the %s') % _('Arroyo Casupá'), 3, _('A. Casupá'), _("It's in the southwest")),
    (_('the %s') % _('Arroyo Chamamé'), 3, _('A. Chamamé'), _("It's in the west")),
    (_('the %s') % _('Arroyo Gaitea'), 3, _('A. Gaitea'), _("It's in the southwest")),
    (_('the %s') % _('Arroyo del Soldado'), 3, _('A. del Soldado'), _("It's in the southwest")),
    (_('the %s') % _('Arroyo Campamento'), 3, _('A. Campamento'), _("It's in the south")),
    (_('the %s') % _('Arroyo San Francisco'), 3, _('A. San Francisco'), _("It's in the south")),
    (_('the %s') % _('Arroyo de la Plata'), 3, _('A. de la Plata'), _("It's in the south")),
    (_('the %s') % _('Arroyo Marmarajá'), 3, _('A. Marmarajá'), _("It's in the southeast")),
    (_('the %s') % _('Arroyo Aiguá'), 3, _('A. Aiguá'), _("It's in the east")),
    (_('the %s') % _('Arroyo de la Lorencita'), 3, _('A. de la Lorencita'), _('Está en el centro')),
    (_('the %s') % _('Arroyo de los Viera'), 3, _('A. de los Viera'), _("It's in the west")),
    (_('the %s') % _('Arroyo Tapes'), 3, _('A. Tapes'), _('Está en el centro')),
    (_('the %s') % _('Arroyo Barriga Negra'), 3, _('A. Barriga Negra'), _('Está en el centro')),
    (_('the %s') % _('Arroyo Polanco'), 3, _('A. Polanco'), _('Está en el centro')),
    (_('the %s') % _('Arroyo Malo Gr.'), 3, _('A. Malo Gr.'), _('Está en el centronorte')),
    (_('the %s') % _('Arroyo Malo Ch.'), 3, _('A. Malo Ch.'), _("It's in the northwest")),
    (_('the %s') % _('Arroyo de los Chanchos'), 3, _('A. de los Chanchos'), _("It's in the west")),
    (_('the %s') % _('Arroyo de los Molles'), 3, _('A. de los Molles'), _("It's in the west")),
    (_('the %s') % _('Arroyo de los Tapes'), 3, _('A. de los Tapes'), _("It's in the northwest")),
    (_('the %s') % _('Arroyo Piranga'), 3, _('A. Piranga'), _('Está en el centro')),
    (_('the %s') % _('Arroyo Gutiérrez'), 3, _('A. Gutiérrez'), _("It's in the northeast"))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %s') % _('Cuchilla Grande'), 4, _('Cuchilla Grande'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Asperezas de Retamosa'), 4, _('Asperezas de Retamosa'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Asperezas de Polanco'), 4, _('Asperezas de Polanco'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cuchilla Cerro Partido'), 4, _('Cuchilla Cerro Partido'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cuchilla de Medina'), 4, _('Cuchilla de Medina'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Sierra de Carapé'), 4, _('Sierra de Carapé'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cerro Espuelitas'), 5, _('Co. Espuelitas'), _('Queda al oeste')),
    (_('the %s') % _('Cerro Arequita'), 5, _('Co. Arequita'), _('Queda cerca de Minas')),
    (_('the %s') % _('Cerro Verdún'), 5, _('Co. Verdún'), _('Queda cerca de Minas')),
    (_('the %s') % _('Cerro Retamosa'), 5, _('Co. Retamosa'), _('Queda al norte'))
]
]

LEVEL5 = [
        5,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('Route %s') % 8, _('Cruza el departamento\nde sur a norte')),
    (_('Route %s') % 60, _('Va de Minas al sur')),
    (_('Route %s') % 12, _('Pasa por Villa del Rosario')),
    (_('Route %s') % 58, _('Pasa por Polanco')),
    (_('Route %s') % 40, _('Termina en Pirarajá')),
    (_('Route %s') % 13, _('Va hacia el este')),
    (_('Route %s') % 14, _('Pasa por J.P. Varela'))
]
]

LEVELS = [LEVEL1, LEVEL2, LEVEL3, LEVEL4, LEVEL5]

