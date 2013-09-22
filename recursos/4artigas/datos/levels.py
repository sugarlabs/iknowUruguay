# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL2 = [
        1,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('the city of %s') % _('Artigas'), 2, _('Artigas'), _("It's the capital of\nthe department")),
    (_('the city of %s') % _('Bella Unión'), 2, _('Bella Unión'), _("It's in the north")),
    (_('the city of %s') % _('Tomás Gomensoro'), 2, _('Tomás Gomensoro'), _("It's in the northwest")),
    (_('the town of %s') % _('Colonia Palma'), 2, _('Colonia Palma'), _("It's in the west")),
    (_('the town of %s') % _('Paso Farías'), 2, _('Paso Farías'), _("It's in the center")),
    (_('the town of %s') % _('Baltasar Brum'), 2, _('Baltasar Brum'), _("It's in the southwest")),
    (_('the town of %s') % _('Bernabé Rivera'), 2, _('Bernabé Rivera'), _("It's in the north")),
    (_('the town of %s') % _('Diego Lamas'), 2, _('Diego Lamas'), _("It's in the center")),
    (_('the town of %s') % _('Paso Campamento'), 2, _('Paso Campamento'), _("It's in the center")),
    (_('the town of %s') % _('Sequeira'), 2, _('Sequeira'), _("It's in the south")),
    (_('the town of %s') % _('Catalán'), 2, _('Catalán'), _("It's in the east"))
]
]

LEVEL3 = [
        15,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('Río Uruguay'), _("It's on the border\nwith %s") % _('Argentina')),
    (_('Río Cuareim'), _("It's on the border\nwith %s") % _('Brasil')),
    (_('Río Arapey'), _("It's on the border\nwith %s") % _('Salto')),
    (_('Arroyo Itacumbú'), _('Flows into the %s') % _('Río Uruguay')),
    (_('Arroyo Ñaquiña'), _('Flows into the %s') % _('Río Uruguay')),
    (_('Arroyo Mandiyú'), _('Flows into the %s') % _('Río Uruguay')),
    (_('Arroyo Guaviyú'), _('Flows into the %s') % _('Río Uruguay')),
    (_('Arroyo Palma Sola Grande'), _("It's in the southwest")),
    (_('Arroyo Sarandí'), _("It's in the southwest")),
    (_('Arroyo Yucutuya'), _('Flows into the %s') % _('Río Cuareim')),
    (_('Arroyo Cuaro Grande'), _('Try again')),
    (_('Arroyo Cuaro Chico'), _("It's in the center")),
    (_('Arroyo Pelado'), _("It's in the center")),
    (_('Arroyo Tres Cruces Grande'), _('Flows into the %s') % _('Río Cuareim')),
    (_('Arroyo Catalán Grande'), _("It's in the east")),
    (_('Arroyo Catalán Chico'), _("It's in the east")),
    (_('Arroyo Catalancito'), _("It's in the east")),
    (_('Arroyo Maneco'), _("It's in the east")),
    (_('Arroyo de la Invernada'), _("It's on the border\nwith %s") % _('Brasil')),
    (_('Arroyo Sepultura'), _("It's in the east")),
    (_('Arroyo Yacuy'), _("It's on the border\nwith %s") % _('Salto')),
    (_('Arroyo Ceballos'), _("It's in the south")),
    (_('Arroyo de las Cañas'), _("It's in the south")),
    (_('Arroyo Patitos'), _("It's in the south")),
    (_('Arroyo Sequeira'), _("It's in the south")),
    (_('Arroyo Espinillo'), _("It's in the south")),
    (_('Arroyo Sarandí Grande'), _("It's in the center"))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %(f)s') % {'f': _('Cuchilla Yacaré Cururú')}, 4, _('Cuchilla Yacaré Cururú'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla de Belén')}, 4, _('Cuchilla de Belén'), _('Try again')),
    (_('the %(m)s') % {'m': _('Cerro Chato')}, 5, _('Cerro Chato'), _("It's in the north")),
    (_('the %(m)s') % {'m': _('Tres Cerros de Catalán')}, 5, _('Tres Cerros de Catalán'), _('Try again')),
    (_('the %(m)s') % {'m': _('Cerro Pintado')}, 5, _('Cerro Pintado'), _('Try again'))
]
]

LEVEL5 = [
        5,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('Route %s') % 3, _('Try again')),
    (_('Route %s') % 4, _('Try again')),
    (_('Route %s') % 30, _('Try again'))
]
]

LEVELS = [LEVEL2, LEVEL3, LEVEL4, LEVEL5]

