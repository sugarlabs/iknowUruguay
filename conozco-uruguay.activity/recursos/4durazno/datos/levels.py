# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL1 = [
        7,
        _('Departments'),
        ['lineasDepto'],
        [],
[
    (_('Tacuarembó'), _("It's easy")),
    (_('Río Negro'), _("It's easy")),
    (_('Durazno'), _("It's easy")),
    (_('Flores'), _("It's easy")),
    (_('Florida'), _("It's easy")),
    (_('Cerro Largo'), _("It's easy")),
    (_('Lavalleja'), _("It's easy")),
    (_('Treinta y Tres'), _("It's easy"))
]
]

LEVEL2 = [
        1,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('the city of %s') % _('Durazno'), 2, _('Durazno'), _('Es la capital\ndel departamento')),
    (_('the city of %s') % _('Sarandi del Yi'), 2, _('Sarandi del Yi'), _("It's in the south")),
    (_('the town of %s') % _('Blanquillo'), 2, _('Blanquillo'), _("It's in the west")),
    (_('the town of %s') % _('La Paloma'), 2, _('La Paloma'), _("It's in the northeast")),
    (_('the town of %s') % _('Carlos Reyles'), 2, _('Carlos Reyles'), _("It's in the west")),
    (_('the town of %s') % _('Centenario'), 2, _('Centenario'), _("It's in the north")),
    (_('the town of %s') % _('Baygorria'), 2, _('Baygorria'), _("It's in the northwest")),
    (_('the town of %s') % _('Aguas Buenas'), 2, _('Aguas Buenas'), _("It's in the north")),
    (_('the town of %s') % _('Alvarez'), 2, _('Pueblo de Alvarez'), _("It's in the northeast")),
    (_('the town of %s') % _('Feliciano'), 2, _('Feliciano'), _("It's in the west")),
    (_('the town of %s') % _('Ombúes de Oribe'), 2, _('Ombúes de Oribe'), _('Está al centro')),
    (_('the town of %s') % _('Rossell y Rius'), 2, _('Rossell y Rius'), _("It's in the southeast")),
    (_('the town of %s') % _('San Jorge'), 2, _('San Jorge'), _("It's in the north")),
    (_('the town of %s') % _('Carmen'), 2, _('Carmen'), _("It's in the south")),
    (_('the city of %s') % _('Cerro Chato'), 2, _('Cerro Chato'), _("It's in the southeast")),
    (_('the town of %s') % _('Santa Bernardina'), 2, _('Santa Bernardina'), _("It's in the southwest")),
    (_('the town of %s') % _('Puntas de Malbajar'), 2, _('Puntas de Malbajar'), _("It's in the southeast"))
]
]

LEVEL3 = [
        1,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('the %s') % _('Río Negro'), 3, _('Río Negro'), _("It's in the north")),
    (_('the %s') % _('Río Yí'), 3, _('Río Yí'), _("It's in the south")),
    (_('the %s') % _('Arroyo de Caballero'), 3, _('A. de Caballero'), _("It's in the west")),
    (_('the %s') % _('Arroyo Villasboas'), 3, _('A. Villasboas'), _("It's in the southwest")),
    (_('the %s') % _('Arroyo Maciel'), 3, _('A. Maciel'), _("It's in the south")),
    (_('the %s') % _('Arroyo de Tejera'), 3, _('A. de Tejera'), _("It's in the south")),
    (_('the %s') % _('Arroyo Tomás Cuadra'), 3, _('A. Tomás Cuadra'), _("It's in the south")),
    (_('the %s') % _('Arroyo Maestre de Campo'), 3, _('A. Maestre de Campo'), _("It's in the south")),
    (_('the %s') % _('Arroyo Antonio Herrera'), 3, _('A. Antonio Herrera'), _("It's in the south")),
    (_('the %s') % _('Arroyo Malbajar'), 3, _('A. Malbajar'), _("It's in the southeast")),
    (_('the %s') % _('Arroyo del Cordobés'), 3, _('A. del Cordobés'), _("It's in the east")),
    (_('the %s') % _('Arroyo Palmas'), 3, _('A. Palmas'), _("It's in the east")),
    (_('the %s') % _('Arroyo Blanquillo'), 3, _('A. Blanquillo'), _("It's in the northeast")),
    (_('the %s') % _('Arroyo de las Cañas'), 3, _('A. de las Cañas'), _("It's in the northeast"))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %s') % _('Cuchilla Ramírez'), 4, _('Cuchilla Ramírez'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cuchilla Grande\ndel Durazno'), 4, _('Cuchilla Grande del Durazno'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cuchilla Villasboas'), 4, _('Cuchilla Villasboas'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cerro Dos Hermanos'), 5, _('Co. Dos Hermanos'), _("It's in the east"))
]
]

LEVEL5 = [
        1,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('the %s') % _('Ruta 5'), 6, _('Ruta 5'), _('Pasa por Durazno')),
    (_('the %s') % _('Ruta 4'), 6, _('Ruta 4'), _('Pasa por Baygorria')),
    (_('the %s') % _('Ruta 14'), 6, _('Ruta 14'), _('Pasa por Villa del Carmen')),
    (_('the %s') % _('Ruta 6'), 6, _('Ruta 6'), _('Pasa por Sarandí del Yi')),
    (_('the %s') % _('Ruta 43'), 6, _('Ruta 43'), _('Pasa por Blanquillo')),
    (_('the %s') % _('Ruta 19'), 6, _('Ruta 19'), _('Pasa cerca de Rossell y Rius')),
    (_('the %s') % _('Ruta 100'), 6, _('Ruta 100'), _('Va hasta el embalse\ndel Río Negro'))
]
]

LEVELS = [LEVEL1, LEVEL2, LEVEL3, LEVEL4, LEVEL5]

