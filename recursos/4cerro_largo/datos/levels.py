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
    (_('the town of %s') % _('Bañados de Medina'), 2, _('Bañados de Medina'), _("It's in the center")),
    (_('the town of %s') % _('Tres Islas'), 2, _('Tres Islas'), _("It's in the center")),
    (_('the town of %s') % _('Arévalo'), 2, _('Arévalo'), _("It's in the southwest")),
    (_('the town of %s') % _('C. de las Cuentas'), 2, _('C. de las Cuentas'), _("It's in the south")),
    (_('the town of %s') % _('Fraile Muerto'), 2, _('Fraile Muerto'), _("It's in the center")),
    (_('the town of %s') % _('Arbolito'), 2, _('Arbolito'), _("It's in the south")),
    (_('the town of %s') % _('Plácido Rosas'), 2, _('Plácido Rosas'), _("It's in the southeast")),
    (_('the town of %s') % _('Río Branco'), 2, _('Río Branco'), _("It's in the southeast")),
    (_('the town of %s') % _('Tambos de Melo'), 2, _('Tambos de Melo'), _("It's in the center"))
]
]

LEVEL3 = [
        15,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('Río Yaguarón'), _("It's on the border\nwith %s") % _('Brasil')),
    (_('Río Negro'), _("It's on the border\nwith %s") % _('Tacuarembó')),
    (_('Río Tacuarí'), _("It's on the border\nwith %s") % _('Treinta y Tres')),
    (_('Arroyo del Parao'), _("It's in the south")),
    (_('Arroyo Santos'), _("It's in the southeast")),
    (_('Arroyo Malo'), _("It's in the southeast")),
    (_('Arroyo Chuy'), _("It's in the center")),
    (_('Arroyo del Sauce'), _("It's in the center")),
    (_('Arroyo del Cordobés'), _("It's in the southwest")),
    (_('Arroyo Lechiguana'), _("It's in the southwest")),
    (_('Arroyo Pablo Páez'), _("It's in the southwest")),
    (_('Arroyo Tarariras'), _("It's in the southwest")),
    (_('Arroyo Tupambaé'), _("It's in the west")),
    (_('Arroyo Quebracho'), _("It's in the south")),
    (_('Arroyo Fraile Muerto'), _("It's in the east")),
    (_('Arroyo del Sarandí'), _("It's in the northwest")),
    (_('Arroyo Zapallar'), _("It's in the northwest")),
    (_('Arroyo Aceguá'), _("It's in the north")),
    (_('Arroyo Pantanoso'), _("It's in the north"))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %(f)s') % {'f': _('Sierra de Aceguá')}, 4, _('Sierra de Aceguá'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla Grande')}, 4, _('Cuchilla Grande'), _('Try again')),
    (_('the %(f)s') % {'f': _('Sierra de los Ríos')}, 4, _('Sierra de los Ríos'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla de Mangrullo')}, 4, _('Cuchilla de Mangrullo'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla del Cordobés')}, 4, _('Cuchilla del Cordobés'), _('Try again')),
    (_('the %(m)s') % {'m': _('Cerro Grande de Aceguá')}, 5, _('Cerro Grande de Aceguá'), _("It's in the north")),
    (_('the %(m)s') % {'m': _('Cerro Colorado')}, 5, _('Cerro Colorado'), _("It's in the east")),
    (_('the %(m)s') % {'m': _('Cerro Redondo')}, 5, _('Cerro Redondo'), _("It's in the northeast")),
    (_('the %(m)s') % {'m': _('Cerro Pablo Pérez')}, 5, _('Cerro Pablo Pérez'), _("It's in the southwest")),
    (_('the %(m)s') % {'m': _('Cerro Largo')}, 5, _('Cerro Largo'), _("It's in the south")),
    (_('the %(m)s') % {'m': _('Cerro Verde')}, 5, _('Cerro Verde'), _("It is near %s") % _('Melo'))
]
]

LEVEL5 = [
        5,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('Route %s') % 7, _('Passes through %s') % _('Fraile Muerto')),
    (_('Route %s') % 8, _('Passes through %s') % _('Melo')),
    (_('Route %s') % 26, _('Ends in %s') % _('Río Branco')),
    (_('Route %s') % 44, _('Passes through %s') % _('Río Negro')),
    (_('Route %s') % 18, _('Comes from %s') % _('Treinta y Tres'))
]
]

LEVELS = [LEVEL2, LEVEL3, LEVEL4, LEVEL5]

