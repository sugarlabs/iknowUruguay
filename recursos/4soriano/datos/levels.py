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
    (_('the town of %s') % _('Cuch. del Perdido'), 2, _('Cuch. del Perdido'), _("It's in the southeast")),
    (_('the city of %s') % _('Sta. Catalina'), 2, _('Sta. Catalina'), _("It's in the southeast")),
    (_('the city of %s') % _('Cardona'), 2, _('Cardona'), _("It's in the southeast")),
    (_('the town of %s') % _('Villa Soriano'), 2, _('Villa Soriano'), _("It's in the northwest")),
    (_('the city of %s') % _('Dolores'), 2, _('Dolores'), _("It's in the west"))
]
]

LEVEL3 = [
        1,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('the %s') % _('Río Uruguay'), 3, _('Río Uruguay'), _("It's in the west")),
    (_('the %s') % _('Río de la Plata'), 3, _('Río de la Plata'), _("It's in the southwest")),
    (_('the %s') % _('Río Negro'), 3, _('Río Negro'), _("It's in the north")),
    (_('the %s') % _('Río San Salvador'), 3, _('Río San Salvador'), _("It's in the south")),
    (_('the %s river') % _('de Espinillo'), 3, _('de Espinillo'), _("It's in the southwest")),
    (_('the %s river') % _('del Sauce'), 3, _('del Sauce'), _("It's in the southwest")),
    (_('the %s river') % _('Bizcocho'), 3, _('Bizcocho'), _("It's in the west")),
    (_('the %s river') % _('Magallanes'), 3, _('Magallanes'), _("It's in the west")),
    (_('the %s river') % _('del Águila'), 3, _('del Águila'), _("It's in the southwest")),
    (_('the %s river') % _('del Corralito'), 3, _('del Corralito'), _("It's in the southwest")),
    (_('the %s river') % _('Maciel'), 3, _('Maciel'), _("It's in the south")),
    (_('the %s river') % _('San Martín'), 3, _('San Martín'), _("It's in the south")),
    (_('the %s river') % _('del Medio'), 3, _('del Medio'), _("It's in the south")),
    (_('the %s river') % _('de las Maulas'), 3, _('de las Maulas'), _("It's in the west")),
    (_('the %s river') % _('Bequeló'), 3, _('Bequeló'), _("It's in the center")),
    (_('the %s river') % _('Coquimbo'), 3, _('Coquimbo'), _("It's in the center")),
    (_('the %s river') % _('Sarandí'), 3, _('Sarandí'), _("It's in the center")),
    (_('the %s river') % _('Caballudo'), 3, _('Caballudo'), _("It's in the center")),
    (_('the %s river') % _('Maia'), 3, _('Maia'), _("It's in the north")),
    (_('the %s river') % _('Cololó'), 3, _('Cololó'), _("It's in the north")),
    (_('the %s river') % _('Perico'), 3, _('Perico'), _("It's in the north")),
    (_('the %s river') % _('de Vera'), 3, _('de Vera'), _("It's in the north")),
    (_('the %s river') % _('Grande'), 3, _('Grande'), _("It's in the northeast")),
    (_('the %s river') % _('del Perdido'), 3, _('del Perdido'), _("It's in the southeast")),
    (_('the %s river') % _('del Durazno'), 3, _('del Durazno'), _("It's in the southeast")),
    (_('the %s river') % _('Monzón'), 3, _('Monzón'), _("It's in the southeast"))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %s') % _('Cuchilla de Bequeló'), 4, _('Cuchilla de Bequeló'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cuchilla del Perdido'), 4, _('Cuchilla del Perdido'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cuchilla del Bizcocho'), 4, _('Cuchilla del Bizcocho'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cuchilla San Salvador'), 4, _('Cuchilla San Salvador'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cerro Espinillo'), 5, _('Co. Espinillo'), _('Queda cerca de Dolores')),
    (_('the %s') % _('Cerro Curupí'), 5, _('Co. Curupí'), _('Queda al norte'))
]
]

LEVEL5 = [
        5,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('Route %s') % 2, _('Pasa por Palmitas')),
    (_('Route %s') % 21, _('Pasa por Dolores')),
    (_('Route %s') % 14, _('Va hasta Flores')),
    (_('Route %s') % 96, _('Va hasta Villa Soriano')),
    (_('Route %s') % 95, _('Sale de Mercedes')),
    (_('Route %s') % 105, _('Va de Dolores\na Palmitas')),
    (_('Route %s') % 55, _('Termina en\nJosé Enrique Rodó')),
    (_('Route %s') % 12, _('Está en el límite\ncon Colonia')),
    (_('Route %s') % 57, _('Va hasta Flores'))
]
]

LEVELS = [LEVEL2, LEVEL3, LEVEL4, LEVEL5]

