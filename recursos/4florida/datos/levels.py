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
    (_('the city of %s') % _('Florida'), 2, _('Florida'), _('Es la capital del\ndepartamento')),
    (_('the town of %s') % _('Cerro Chato'), 2, _('Cerro Chato'), _("It's in the northeast")),
    (_('the town of %s') % _('Valentines'), 2, _('Valentines'), _("It's in the northeast")),
    (_('the town of %s') % _('Capilla del Sauce'), 2, _('Capilla del Sauce'), _("It's in the northeast")),
    (_('the town of %s') % _('Nico Pérez'), 2, _('Nico Pérez'), _("It's in the northeast")),
    (_('the town of %s') % _('Illescas'), 2, _('Illescas'), _("It's in the northeast")),
    (_('the town of %s') % _('Cerro Colorado'), 2, _('Cerro Colorado'), _("It's in the east")),
    (_('the town of %s') % _('San Gabriel'), 2, _('San Gabriel'), _('Está en el centro')),
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
        1,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('the %s') % _('Río Yí'), 3, _('Río Yí'), _("It's in the north")),
    (_('the %s') % _('Río Santa Lucía'), 3, _('Río Santa Lucía'), _("It's in the south")),
    (_('the %s') % _('Río Santa Lucía Ch.'), 3, _('Río Santa Lucía Ch.'), _('Está en el centro')),
    (_('the %s') % _('Arroyo Palermo'), 3, _('A. Palermo'), _('Está en el centro')),
    (_('the %s') % _('Arroyo de la Cruz'), 3, _('A. de la Cruz'), _("It's in the east")),
    (_('the %s') % _('Arroyo Mansavillagra'), 3, _('A. Mansavillagra'), _("It's in the north")),
    (_('the %s') % _('Arroyo del Potrero'), 3, _('A. del Potrero'), _("It's in the east")),
    (_('the %s') % _('Arroyo Illescas'), 3, _('A. Illescas'), _("It's in the northeast")),
    (_('the %s') % _('Arroyo del Pescado'), 3, _('A. del Pescado'), _("It's in the northeast")),
    (_('the %s') % _('Arroyo Molles de P.'), 3, _('A. Molles de P.'), _("It's in the northeast")),
    (_('the %s') % _('Arroyo Monzón'), 3, _('A. Monzón'), _("It's in the northeast")),
    (_('the %s') % _('Arroyo Manguera'), 3, _('A. Manguera'), _("It's in the north")),
    (_('the %s') % _('Arroyo Maciel'), 3, _('A. Maciel'), _("It's in the west")),
    (_('the %s') % _('Arroyo de la Virgen'), 3, _('A. de la Virgen'), _("It's in the west")),
    (_('the %s') % _('Arroyo de Mendoza'), 3, _('A. de Mendoza'), _("It's in the southwest")),
    (_('the %s') % _('Arroyo de Arias'), 3, _('A. de Arias'), _("It's in the south")),
    (_('the %s') % _('Arroyo San Gabriel'), 3, _('A. San Gabriel'), _("It's in the southeast")),
    (_('the %s') % _('Arroyo Chamizo'), 3, _('A. Chamizo'), _("It's in the south")),
    (_('the %s') % _('Arroyo Chamamé'), 3, _('A. Chamamé'), _("It's in the southeast")),
    (_('the %s') % _('Arroyo la Cruz'), 3, _('A. la Cruz'), _("It's in the east")),
    (_('the %s') % _('Arroyo Casupá'), 3, _('A. Casupá'), _("It's in the south")),
    (_('the %s') % _('Arroyo Pintado'), 3, _('A. Pintado'), _("It's in the west")),
    (_('the %s') % _('Arroyo Pantanoso'), 3, _('A. Pantanoso'), _("It's in the north")),
    (_('the %s') % _('Arroyo Sarandí'), 3, _('A. Sarandí'), _("It's in the north")),
    (_('the %s') % _('Arroyo Timote'), 3, _('A. Timote'), _('Está en el centro')),
    (_('the %s') % _('Arroyo Molles\de Timote'), 3, _('A. Molles de Timote'), _("It's in the north")),
    (_('the %s') % _('Arroyo Sauce de Timote'), 3, _('A. Sauce de Timote'), _("It's in the north")),
    (_('the %s') % _('Arroyo Bellaco'), 3, _('A. Bellaco'), _("It's in the northwest")),
    (_('the %s') % _('Arroyo Sarandí Ch.'), 3, _('A. Sarandí Ch.'), _('Está en el centro'))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %s') % _('Cuchilla Mansavillagra'), 4, _('Cuchilla Mansavillagra'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cuchilla Grande'), 4, _('Cuchilla Grande'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cuchilla Grande Inferior'), 4, _('Cuchilla Grande Inferior'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cuchilla del Pintado'), 4, _('Cuchilla del Pintado'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cuchilla Sta. Lucía'), 4, _('Cuchilla Sta. Lucía'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cerro Pescado'), 5, _('Co. Pescado'), _('Queda al noreste')),
    (_('the %s') % _('Cerro Florida'), 5, _('Co. Florida'), _('Queda cerca de la capital')),
    (_('the %s') % _('Cerro Valentín'), 5, _('Co. Valentín'), _('Queda en el límite con\nTreinta y Tres'))
]
]

LEVEL5 = [
        1,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('Route %s') % 5, _('Va de norte a sur')),
    (_('Route %s') % 6, _('Pasa por Capilla del Sauce')),
    (_('Route %s') % 7, _('Pasa por Cerro Chato')),
    (_('Route %s') % 42, _('Sale de Sarandí Grande')),
    (_('Route %s') % 77, _('Va por el oeste')),
    (_('Route %s') % 56, _('Sale de Florida')),
    (_('Route %s') % 41, _('Pasa por Cerro Colorado')),
    (_('Route %s') % 14, _('Pasa por Nico Pérez'))
]
]

LEVELS = [LEVEL1, LEVEL2, LEVEL3, LEVEL4, LEVEL5]

