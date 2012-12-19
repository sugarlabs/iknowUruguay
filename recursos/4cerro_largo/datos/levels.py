# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL2 = [
        1,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('the city of %s') % _('Melo'), 2, _('Melo'), _("It's the capital of\nthe department")),
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
        15,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('Río Yaguarón'), _('Queda en el límite\ncon Brasil')),
    (_('Río Negro'), _('Queda en el límite\ncon Tacuarembó')),
    (_('Río Tacuarí'), _('Queda en el límite\ncon Treinta y Tres')),
    (_('Arroyo del Parao'), _('Queda al sur')),
    (_('Arroyo Santos'), _('Queda al sureste')),
    (_('Arroyo Malo'), _('Queda al sureste')),
    (_('Arroyo Chuy'), _('Queda en el centro')),
    (_('Arroyo del Sauce'), _('Queda en el centro')),
    (_('Arroyo del Cordobés'), _('Queda al suroeste')),
    (_('Arroyo Lechiguana'), _('Queda al suroeste')),
    (_('Arroyo Pablo Páez'), _('Queda al suroeste')),
    (_('Arroyo Tarariras'), _('Queda al suroeste')),
    (_('Arroyo Tupambaé'), _('Queda al oeste')),
    (_('Arroyo Quebracho'), _('Queda al sur')),
    (_('Arroyo Fraile Muerto'), _('Queda al este')),
    (_('Arroyo del Sarandí'), _('Queda al noroeste')),
    (_('Arroyo Zapallar'), _('Queda al noroeste')),
    (_('Arroyo Aceguá'), _('Queda al norte')),
    (_('Arroyo Pantanoso'), _('Queda al norte'))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %(f)s') % {'f': _('Sierra de Aceguá'), 4, _('Sierra de Aceguá'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla Grande'), 4, _('Cuchilla Grande'), _('Try again')),
    (_('the %(f)s') % {'f': _('Sierra de los Ríos'), 4, _('Sierra de los Ríos'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla de Mangrullo'), 4, _('Cuchilla de Mangrullo'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla del Cordobés'), 4, _('Cuchilla del Cordobés'), _('Try again')),
    (_('the %(m)s') % {'m': _('Cerro Grande de Aceguá'), 5, _('Cerro Gde. de Aceguá'), _("It's in the north")),
    (_('the %(m)s') % {'m': _('Cerro Colorado'), 5, _('Cerro Colorado'), _("It's in the east")),
    (_('the %(m)s') % {'m': _('Cerro Redondo'), 5, _('Cerro Redondo'), _("It's in the northeast")),
    (_('the %(m)s') % {'m': _('Cerro Pablo Pérez'), 5, _('Cerro Pablo Pérez'), _("It's in the southwest")),
    (_('the %(m)s') % {'m': _('Cerro Largo'), 5, _('Cerro Largo'), _("It's in the south")),
    (_('the %(m)s') % {'m': _('Cerro Verde'), 5, _('Cerro Verde'), _('Está cerca de Melo'))
]
]

LEVEL5 = [
        5,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('Route %s') % 7, _('Pasa por Fraile Muerto')),
    (_('Route %s') % 8, _('Pasa por Melo')),
    (_('Route %s') % 26, _('Va hasta Río Branco')),
    (_('Route %s') % 44, _('Cruza el Río Negro')),
    (_('Route %s') % 18, _('Viene de Treinta y Tres'))
]
]

LEVELS = [LEVEL2, LEVEL3, LEVEL4, LEVEL5]

