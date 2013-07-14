# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL2 = [
        1,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('the city of %s') % _('Rocha'), 2, _('Rocha'), _("It's the capital of\nthe department")),
    (_('the city of %s') % _('Cebollatí'), 2, _('Cebollatí'), _("It's in the north")),
    (_('the town of %s') % _('San Luis al Medio'), 2, _('San Luis al Medio'), _("It's in the northeast")),
    (_('the town of %s') % _('Lascano'), 2, _('Lascano'), _("It's in the northwest")),
    (_('the town of %s') % _('18 de Julio'), 2, _('18 de Julio'), _("It's in the east")),
    (_('the city of %s') % _('La Coronilla'), 2, _('La Coronilla'), _("It's in the east")),
    (_('the town of %s') % _('Velázquez'), 2, _('Velázquez'), _("It's in the center")),
    (_('the city of %s') % _('Castillos'), 2, _('Castillos'), _("It's in the southeast")),
    (_('the city of %s') % _('La Paloma'), 2, _('La Paloma'), _("It's an important resort")),
    (_('the resort of %s') % _('La Pedrera'), 2, _('La Pedrera'), _("It is near %s") % _('La Paloma')),
    (_('the resort of %s') % _('Cabo Polonio'), 2, _('Cabo Polonio'), _("It's in the southeast")),
    (_('the resort of %s') % _('Barra de Valizas'), 2, _('Barra de Valizas'), _("It is near %s") % _('Cabo Polonio')),
    (_('the resort of %s') % _('Aguas Dulces'), 2, _('Aguas Dulces'), _("It is near %s") % _('Castillos')),
    (_('the resort of %s') % _('Punta del Diablo'), 2, _('Punta del Diablo'), _("It is near %s") % _('Laguna Negra')),
    (_('the %s') % _('Parque Santa Teresa'), 2, _('Parque Santa Teresa'), _("It is near %s") % _('La Coronilla')),
    (_('the resort of %s') % _('Barra del Chuy'), 2, _('Barra del Chuy'), _("It's on the border\nwith %s") % _('Brazil')),
    (_('the city of %s') % _('Chuy'), 2, _('Chuy'), _("It's on the border\nwith %s") % _('Brazil')),
    (_('the town of %s') % _('19 de Abril'), 2, _('19 de Abril'), _('Try again'))
]
]

LEVEL3 = [
        15,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('Atlantic Ocean'), _("It's in the southeast")),
    (_('Río Cebollatí'), _("It's in the north")),
    (_('Río San Luis'), _("It's in the northeast")),
    (_('Arroyo de las Pelotas'), _("It's in the north")),
    (_('Arroyo de la India Muerta'), _("It's in the center")),
    (_('Arroyo S. de la Paloma'), _("It's in the west")),
    (_('Arroyo Sarandí de la I. M.'), _("It's in the center")),
    (_('Arroyo Sauce'), _("It's in the center")),
    (_('Arroyo Sauce Caído'), _("It's in the center")),
    (_('Arroyo San Miguel'), _("It's in the east")),
    (_('Arroyo S. del Peñon'), _("It's in the center")),
    (_('Arroyo del Sarandí'), _("It's in the east")),
    (_('Arroyo del Chuy'), _("It's in the east")),
    (_('Arroyo del Peñon'), _("It's in the southeast")),
    (_('Arroyo del Sauce'), _("It's in the southeast")),
    (_('Arroyo Castillos'), _("It's in the southeast")),
    (_('Arroyo Don Carlos'), _("It's in the south")),
    (_('Arroyo del Chafalote'), _("It's in the southeast")),
    (_('Arroyo Garzón'), _("It's in the southwest")),
    (_('Arroyo Carpinchos'), _("It's in the south")),
    (_('Arroyo del Oeste'), _("It's in the southwest")),
    (_('Arroyo de los Rocha'), _("It's in the south")),
    (_('Arroyo del Alférez'), _("It's in the west")),
    (_('Arroyo Aiguá'), _("It's in the west"))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %(f)s') % {'f': _('Cuchilla de las Averías')}, 4, _('Cuchilla de las Averías'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla de la Carbonera')}, 4, _('Cuchilla de la Carbonera'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla de la India Muerta')}, 4, _('Cuchilla de la India Muerta'), _('Try again')),
    (_('the %(m)s') % {'m': _('Cerro de Aguirre')}, 5, _('Cerro de Aguirre'), _("It's in the south"))
]
]

LEVEL5 = [
        5,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('Route %s') % 9, _("Ends in %s") % _('Chuy')),
    (_('Route %s') % 10, _('Passes through %s') % _('La Paloma')),
    (_('Route %s') % 109, _("Ends in %s") % _('Rocha')),
    (_('Route %s') % 15, _('Passes through %s') % _('Lascano')),
    (_('Route %s') % 13, _("It's in the center\nof the department")),
    (_('Route %s') % 16, _('Passes through %s') % _('Castillos')),
    (_('Route %s') % 14, _('Try again')),
    (_('Route %s') % 19,_('Passes through %s') % _('San Luis al Medio'))
]
]

LEVELS = [LEVEL2, LEVEL3, LEVEL4, LEVEL5]

