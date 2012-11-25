# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL2 = [
        1,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('the city of %s') % _('Melo'), 2, _('Melo'), _('Es la capital del\ndepartamento')),
    (_('the town of %s') % _('Isidoro Noblía'), 2, _('Isidoro Noblía'), _("It's in the north")),
    (_('the town of %s') % _('Centurión'), 2, _('Centurión'), _("It's in the northwest")),
    (_('the town of %s') % _('Bañados de Medina'), 2, _('Bañados de Medina'), _('Está en el centro')),
    (_('the town of %s') % _('Tres Islas'), 2, _('Tres Islas'), _('Está en el centro')),
    (_('the town of %s') % _('Arévalo'), 2, _('Arévalo'), _("It's in the southwest")),
    (_('the town of %s') % _('C. de las Cuentas'), 2, _('C. de las Cuentas'), _("It's in the south")),
    (_('the town of %s') % _('Fraile Muerto'), 2, _('Fraile Muerto'), _('Está en el centro')),
    (_('the town of %s') % _('Arbolito'), 2, _('Arbolito'), _("It's in the south")),
    (_('the town of %s') % _('Plácido Rosas'), 2, _('Plácido Rosas'), _("It's in the southeast")),
    (_('the town of %s') % _('Río Branco'), 2, _('Río Branco'), _("It's in the southeast")),
    (_('the town of %s') % _('Tambos de Melo'), 2, _('Tambos de Melo'), _('Está en el centro'))
]
]

LEVEL3 = [
        1,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('the %s') % _('Río Yaguarón'), 3, _('Río Yaguarón'), _('Queda en el límite\ncon Brasil')),
    (_('the %s') % _('Río Negro'), 3, _('Río Negro'), _('Queda en el límite\ncon Tacuarembó')),
    (_('the %s') % _('Río Tacuarí'), 3, _('Río Tacuarí'), _('Queda en el límite\ncon Treinta y Tres')),
    (_('the %s') % _('Arroyo del Parao'), 3, _('A. del Parao'), _('Queda al sur')),
    (_('the %s') % _('Arroyo Santos'), 3, _('A. Santos'), _('Queda al sureste')),
    (_('the %s') % _('Arroyo Malo'), 3, _('A. Malo'), _('Queda al sureste')),
    (_('the %s') % _('Arroyo Chuy'), 3, _('A. Chuy'), _('Queda en el centro')),
    (_('the %s') % _('Arroyo del Sauce'), 3, _('A. del Sauce'), _('Queda en el centro')),
    (_('the %s') % _('Arroyo del Cordobés'), 3, _('A. del Cordobés'), _('Queda al suroeste')),
    (_('the %s') % _('Arroyo Lechiguana'), 3, _('A. Lechiguana'), _('Queda al suroeste')),
    (_('the %s') % _('Arroyo Pablo Páez'), 3, _('A. Pablo Páez'), _('Queda al suroeste')),
    (_('the %s') % _('Arroyo Tarariras'), 3, _('A. Tarariras'), _('Queda al suroeste')),
    (_('the %s') % _('Arroyo Tupambaé'), 3, _('A. Tupambaé'), _('Queda al oeste')),
    (_('the %s') % _('Arroyo Quebracho'), 3, _('A. Quebracho'), _('Queda al sur')),
    (_('the %s') % _('Arroyo Fraile Muerto'), 3, _('A. Fraile Muerto'), _('Queda al este')),
    (_('the %s') % _('Arroyo del Sarandí'), 3, _('A. del Sarandí'), _('Queda al noroeste')),
    (_('the %s') % _('Arroyo Zapallar'), 3, _('A. Zapallar'), _('Queda al noroeste')),
    (_('the %s') % _('Arroyo Aceguá'), 3, _('A. Aceguá'), _('Queda al norte')),
    (_('the %s') % _('Arroyo Pantanoso'), 3, _('A. Pantanoso'), _('Queda al norte')),
    (_('the %s') % _('Laguna Merin'), 3, _('Laguna Merin'), _('Queda al sur'))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %s') % _('Sierra de Aceguá'), 4, _('Sierra de Aceguá'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cuchilla Grande'), 4, _('Cuchilla Grande'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Sierra de los Ríos'), 4, _('Sierra de los Ríos'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cuchilla de Mangrullo'), 4, _('Cuchilla de Mangrullo'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cuchilla del Cordobés'), 4, _('Cuchilla del Cordobés'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cerro Grande de Aceguá'), 5, _('Co. Gde. de Aceguá'), _("It's in the north")),
    (_('the %s') % _('Cerro Colorado'), 5, _('Co. Colorado'), _("It's in the east")),
    (_('the %s') % _('Cerro Redondo'), 5, _('Co. Redondo'), _("It's in the northeast")),
    (_('the %s') % _('Cerro Pablo Pérez'), 5, _('Co. Pablo Pérez'), _("It's in the southwest")),
    (_('the %s') % _('Cerro Largo'), 5, _('Co. Largo'), _("It's in the south")),
    (_('the %s') % _('Cerro Verde'), 5, _('Co. Verde'), _('Está cerca de Melo'))
]
]

LEVEL5 = [
        1,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('the %s') % _('Ruta 7'), 6, _('Ruta 7'), _('Pasa por Fraile Muerto')),
    (_('the %s') % _('Ruta 8'), 6, _('Ruta 8'), _('Pasa por Melo')),
    (_('the %s') % _('Ruta 26'), 6, _('Ruta 26'), _('Va hasta Río Branco')),
    (_('the %s') % _('Ruta 44'), 6, _('Ruta 44'), _('Cruza el Río Negro')),
    (_('the %s') % _('Ruta 18'), 6, _('Ruta 18'), _('Viene de Treinta y Tres'))
]
]

LEVELS = [LEVEL2, LEVEL3, LEVEL4, LEVEL5]

