# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL2 = [
        1,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('the city of %s') % _('Mercedes'), 1, _('Mercedes'), _("It's the capital of\nthe department")),
    (_('the town of %s') % _('Sacachispas'), 2, _('Sacachispas'), _("It's in the north")),
    (_('the town of %s') % _('El Tala'), 2, _('El Tala'), _("It's in the northeast")),
    (_('the city of %s') % _('Palmitas'), 2, _('Palmitas'), _("It's in the center")),
    (_('the town of %s') % _('Colonia Concordia'), 2, _('Colonia Concordia'), _("It's in the west")),
    (_('the town of %s') % _('Egaña'), 2, _('Egaña'), _("It's in the center")),
    (_('the town of %s') % _('Risso'), 2, _('Risso'), _("It's in the center")),
    (_('the town of %s') % _('Rodó'), 2, _('Rodó'), _("It's in the center")),
    (_('the town of %s') % _('Perseverano'), 2, _('Perseverano'), _("It's in the south")),
    (_('the town of %s') % _('Castillo'), 2, _('Castillo'), _("It's in the south")),
    (_('the town of %s') % _('Cuchilla del Perdido'), 2, _('Cuchilla del Perdido'), _("It's in the southeast")),
    (_('the city of %s') % _('Santa Catalina'), 2, _('Santa Catalina'), _("It's in the southeast")),
    (_('the city of %s') % _('Cardona'), 2, _('Cardona'), _("It's in the southeast")),
    (_('the town of %s') % _('Villa Soriano'), 2, _('Villa Soriano'), _("It's in the northwest")),
    (_('the city of %s') % _('Dolores'), 2, _('Dolores'), _("It's in the west"))
]
]

LEVEL3 = [
        15,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('Río Uruguay'), _("It's in the west")),
    (_('Río de la Plata'), _("It's in the southwest")),
    (_('Río Negro'), _("It's in the north")),
    (_('Río San Salvador'), _("It's in the south")),
    (_('Arroyo de Espinillo'), _("It's in the southwest")),
    (_('Arroyo del Sauce'), _("It's in the southwest")),
    (_('Arroyo Bizcocho'), _("It's in the west")),
    (_('Arroyo Magallanes'), _("It's in the west")),
    (_('Arroyo del Águila'), _("It's in the southwest")),
    (_('Arroyo del Corralito'), _("It's in the southwest")),
    (_('Arroyo Maciel'), _("It's in the south")),
    (_('Arroyo San Martín'), _("It's in the south")),
    (_('Arroyo del Medio'), _("It's in the south")),
    (_('Arroyo de las Maulas'), _("It's in the west")),
    (_('Arroyo Bequeló'), _("It's in the center")),
    (_('Arroyo Coquimbo'), _("It's in the center")),
    (_('Arroyo Sarandí'), _("It's in the center")),
    (_('Arroyo Caballudo'), _("It's in the center")),
    (_('Arroyo Maia'), _("It's in the north")),
    (_('Arroyo Cololó'), _("It's in the north")),
    (_('Arroyo Perico'), _("It's in the north")),
    (_('Arroyo de Vera'), _("It's in the north")),
    (_('Arroyo Grande'), _("It's in the northeast")),
    (_('Arroyo del Perdido'), _("It's in the southeast")),
    (_('Arroyo del Durazno'), _("It's in the southeast")),
    (_('Arroyo Monzón'), _("It's in the southeast"))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %(f)s') % {'f': _('Cuchilla de Bequeló')}, 4, _('Cuchilla de Bequeló'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla del Perdido')}, 4, _('Cuchilla del Perdido'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla del Bizcocho')}, 4, _('Cuchilla del Bizcocho'), _('Try again')),
    (_('the %(f)s') % {'f': _('Cuchilla San Salvador')}, 4, _('Cuchilla San Salvador'), _('Try again')),
    (_('the %(m)s') % {'m': _('Cerro Espinillo')}, 5, _('Cerro Espinillo'), _("It is near %s") % _('Dolores')),
    (_('the %(m)s') % {'m': _('Cerro Curupí')}, 5, _('Cerro Curupí'), _("It's in the north"))
]
]

LEVEL5 = [
        5,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('Route %s') % 2, _('Passes through %s') % _('Palmitas')),
    (_('Route %s') % 21, _('Passes through %s') % _('Dolores')),
    (_('Route %s') % 14, _('Ends in %s') % _('Flores')),
    (_('Route %s') % 96, _('Ends in %s') % _('Villa Soriano')),
    (_('Route %s') % 95, _('Try again')),
    (_('Route %s') % 105, _('Try again')),
    (_('Route %s') % 55, _('Ends in %s') % _('José Enrique Rodó')),
    (_('Route %s') % 12, _("It's on the border\nwith %s") % _('Colonia')),
    (_('Route %s') % 57, _('Ends in %s') % _('Flores'))
]
]

LEVELS = [LEVEL2, LEVEL3, LEVEL4, LEVEL5]

