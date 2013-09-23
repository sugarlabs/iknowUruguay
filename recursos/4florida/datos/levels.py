# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL1 = [
        7,
        _('Departments'),
        ['lineasDepto'],
        [],
[
    (_('Durazno'), _("It's easy")),
    (_('Florida'), _("It's easy")),
    (_('Canelones'), _("It's easy")),
    (_('Lavalleja'), _("It's easy")),
    (_('San José'), _("It's easy")),
    (_('Flores'), _("It's easy")),
    (_('Treinta y Tres'), _("It's easy"))
]
]

LEVEL2 = [
        1,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('the city of %s') % _('Florida'), 2, _('Florida'), _("It's the capital of\nthe department")),
    (_('the town of %s') % _('Cerro Chato'), 2, _('Cerro Chato'), _("It's in the northeast")),
    (_('the town of %s') % _('Valentines'), 2, _('Valentines'), _("It's in the northeast")),
    (_('the town of %s') % _('Capilla del Sauce'), 2, _('Capilla del Sauce'), _("It's in the northeast")),
    (_('the town of %s') % _('Nico Pérez'), 2, _('Nico Pérez'), _("It's in the northeast")),
    (_('the town of %s') % _('Illescas'), 2, _('Illescas'), _("It's in the northeast")),
    (_('the town of %s') % _('Cerro Colorado'), 2, _('Cerro Colorado'), _("It's in the east")),
    (_('the town of %s') % _('San Gabriel'), 2, _('San Gabriel'), _("It's in the center")),
    (_('the town of %s') % _('Reboledo'), 2, _('Reboledo'), _("It's in the southeast")),
    (_('the town of %s') % _('Casupá'), 2, _('Casupá'), _("It's in the southeast")),
    (_('the city of %s') % _('Fray Marcos'), 2, _('Fray Marcos'), _("It's in the southeast")),
    (_('the town of %s') % _('Chamizo'), 2, _('Chamizo'), _("It's in the south")),
    (_('the town of %s') % _('Goñi'), 2, _('Goñi'), _("It's in the northwest")),
    (_('the town of %s') % _('Puntas de Maciel'), 2, _('Puntas de Maciel'), _("It's in the northwest")),
    (_('the city of %s') % _('Sarandí Grande'), 2, _('Sarandí Grande'), _("It's in the northwest")),
    (_('the town of %s') % _('Pintado'), 2, _('Pintado'), _("It's in the west")),
    (_('the town of %s') % _('La Cruz'), 2, _('La Cruz'), _("It's in the west")),
    (_('the town of %s') % _('La Macana'), 2, _('La Macana'), _("It's in the west")),
    (_('the town of %s') % _('Berrondo'), 2, _('Berrondo'), _("It's in the southwest")),
    (_('the city of %s') % _('25 de Mayo'), 2, _('25 de Mayo'), _("It's in the southwest")),
    (_('the town of %s') % _('Mendoza Chico'), 2, _('Mendoza Chico'), _("It's in the southwest")),
    (_('the town of %s') % _('Mendoza Grande'), 2, _('Mendoza Grande'), _("It's in the south")),
    (_('the town of %s') % _('Cardal'), 2, _('Cardal'), _("It's in the southwest")),
    (_('the town of %s') % _('Independencia'), 2, _('Independencia'), _("It's in the southwest"))
]
]

LEVEL3 = [
        15,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('Río Yí'), _("It's in the north")),
    (_('Río Santa Lucía'), _("It's in the south")),
    (_('Río Santa Lucía Chico'), _("It's in the center")),
    (_('Arroyo Palermo'), _("It's in the center")),
    (_('Arroyo de la Cruz'), _("It's in the east")),
    (_('Arroyo Mansavillagra'), _("It's in the north")),
    (_('Arroyo del Potrero'), _("It's in the east")),
    (_('Arroyo Illescas'), _("It's in the northeast")),
    (_('Arroyo del Pescado'), _("It's in the northeast")),
    (_('Arroyo Molles de P.'), _("It's in the northeast")),
    (_('Arroyo Monzón'), _("It's in the northeast")),
    (_('Arroyo Manguera'), _("It's in the north")),
    (_('Arroyo Maciel'), _("It's in the west")),
    (_('Arroyo de la Virgen'), _("It's in the west")),
    (_('Arroyo de Mendoza'), _("It's in the southwest")),
    (_('Arroyo de Arias'), _("It's in the south")),
    (_('Arroyo San Gabriel'), _("It's in the southeast")),
    (_('Arroyo Chamizo'), _("It's in the south")),
    (_('Arroyo Chamamé'), _("It's in the southeast")),
    (_('Arroyo la Cruz'), _("It's in the east")),
    (_('Arroyo Casupá'), _("It's in the south")),
    (_('Arroyo Pintado'), _("It's in the west")),
    (_('Arroyo Pantanoso'), _("It's in the north")),
    (_('Arroyo Sarandí'), _("It's in the north")),
    (_('Arroyo Timote'), _("It's in the center")),
    (_('Arroyo Molles de Timote'), _("It's in the north")),
    (_('Arroyo Sauce de Timote'), _("It's in the north")),
    (_('Arroyo Bellaco'), _("It's in the northwest")),
    (_('Arroyo Sarandí Chico'), _("It's in the center"))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %(f)s') % {'f': _('Cuchilla Mansavillagra')}, 4, _('Cuchilla Mansavillagra'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla Grande')}, 4, _('Cuchilla Grande'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla Grande Inferior')}, 4, _('Cuchilla Grande Inferior'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla del Pintado')}, 4, _('Cuchilla del Pintado'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla Santa Lucía')}, 4, _('Cuchilla Santa Lucía'), _('Try again')),
    (_('the %(m)s') % {'m': _('Cerro Pescado')}, 5, _('Cerro Pescado'), _("It's in the northeast")),
    (_('the %(m)s') % {'m': _('Cerro Florida')}, 5, _('Cerro Florida'), _("It is near %s") % _('the capital')),
    (_('the %(m)s') % {'m': _('Cerro Valentín')}, 5, _('Cerro Valentín'), _("It's on the border\nwith %s") % _('Treinta y Tres'))
]
]

LEVEL5 = [
        5,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('Route %s') % 5, _('Try again')),
    (_('Route %s') % 6, _('Passes through %s') % _('Capilla del Sauce')),
    (_('Route %s') % 7, _('Passes through %s') % _('Cerro Chato')),
    (_('Route %s') % 42, _('Try again')),
    (_('Route %s') % 77, _('Try again')),
    (_('Route %s') % 56, _('Try again')),
    (_('Route %s') % 41, _('Passes through %s') % _('Cerro Colorado')),
    (_('Route %s') % 14, _('Passes through %s') % _('Nico Pérez'))
]
]

LEVELS = [LEVEL1, LEVEL2, LEVEL3, LEVEL4, LEVEL5]

