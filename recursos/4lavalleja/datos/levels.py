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
    (_('the town of %s') % _('José Batlle y Ordóñez'), 2, _('José Batlle y Ordóñez'), _("It's in the northwest")),
    (_('the town of %s') % _('José Pedro Varela'), 2, _('José Pedro Varela'), _("It's in the northeast")),
    (_('the town of %s') % _('Pirarajá'), 2, _('Pirarajá'), _("It's in the north")),
    (_('the town of %s') % _('Polanco'), 2, _('Polanco'), _("It's in the center")),
    (_('the town of %s') % _('Gaetán'), 2, _('Gaetán'), _("It's in the west")),
    (_('the town of %s') % _('Mariscala'), 2, _('Mariscala'), _("It's in the east")),
    (_('the town of %s') % _('Villa del Rosario'), 2, _('Villa del Rosario'), _("It's in the south")),
    (_('the town of %s') % _('Solís de Mataojo'), 2, _('Solís de Mataojo'), _("It's in the south"))
]
]

LEVEL3 = [
        15,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('Río Santa Lucía'), _("It's in the south")),
    (_('Río Cebollatí'), _("It's in the west")),
    (_('Río Olimar Chico'), _("It's in the northwest")),
    (_('Arroyo del Sauce'), _("It's in the northwest")),
    (_('Arroyo Corrales'), _("It's in the northeast")),
    (_('Arroyo Solís Grande'), _("It's in the south")),
    (_('Arroyo Mataojo'), _("It's in the south")),
    (_('Arroyo Casupá'), _("It's in the southwest")),
    (_('Arroyo Chamamé'), _("It's in the west")),
    (_('Arroyo Gaitea'), _("It's in the southwest")),
    (_('Arroyo del Soldado'), _("It's in the southwest")),
    (_('Arroyo Campamento'), _("It's in the south")),
    (_('Arroyo San Francisco'), _("It's in the south")),
    (_('Arroyo de la Plata'), _("It's in the south")),
    (_('Arroyo Marmarajá'), _("It's in the southeast")),
    (_('Arroyo Aiguá'), _("It's in the east")),
    (_('Arroyo de la Lorencita'), _("It's in the center")),
    (_('Arroyo de los Viera'), _("It's in the west")),
    (_('Arroyo Tapes'), _("It's in the center")),
    (_('Arroyo Barriga Negra'), _("It's in the center")),
    (_('Arroyo Polanco'), _("It's in the center")),
    (_('Arroyo Malo Grande'), _("It's in the north")),
    (_('Arroyo Malo Chico'), _("It's in the northwest")),
    (_('Arroyo de los Chanchos'), _("It's in the west")),
    (_('Arroyo de los Molles'), _("It's in the west")),
    (_('Arroyo de los Tapes'), _("It's in the northwest")),
    (_('Arroyo Piranga'), _("It's in the center")),
    (_('Arroyo Gutiérrez'), _("It's in the northeast"))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %(f)s') % {'f': _('Cuchilla Grande')}, 4, _('Cuchilla Grande'), _('Try again')),
    (_('the %(f)s') % {'f': _('Asperezas de Retamosa')}, 4, _('Asperezas de Retamosa'), _('Try again')),
    (_('the %(f)s') % {'f': _('Asperezas de Polanco')}, 4, _('Asperezas de Polanco'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla Cerro Partido')}, 4, _('Cuchilla Cerro Partido'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla de Medina')}, 4, _('Cuchilla de Medina'), _('Try again')),
    (_('the %(f)s') % {'f': _('Sierra de Carapé')}, 4, _('Sierra de Carapé'), _('Try again')),
    (_('the %(m)s') % {'m': _('Cerro Espuelitas')}, 5, _('Cerro Espuelitas'), _("It's in the west")),
    (_('the %(m)s') % {'m': _('Cerro Arequita')}, 5, _('Cerro Arequita'), _("It is near %s") % _('Minas')),
    (_('the %(m)s') % {'m': _('Cerro Verdún')}, 5, _('Cerro Verdún'), _("It is near %s") % _('Minas')),
    (_('the %(m)s') % {'m': _('Cerro Retamosa')}, 5, _('Cerro Retamosa'), _("It's in the north"))
]
]

LEVEL5 = [
        5,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('Route %s') % 8, _('Try again')),
    (_('Route %s') % 60, _('Try again')),
    (_('Route %s') % 12, _('Passes through %s') % _('Villa del Rosario')),
    (_('Route %s') % 58, _('Passes through %s') % _('Polanco')),
    (_('Route %s') % 40, _("Ends in %s") % _('Pirarajá')),
    (_('Route %s') % 13, _('Try again')),
    (_('Route %s') % 14, _('Passes through %s') % _('José Pedro Varela'))
]
]

LEVELS = [LEVEL1, LEVEL2, LEVEL3, LEVEL4, LEVEL5]

