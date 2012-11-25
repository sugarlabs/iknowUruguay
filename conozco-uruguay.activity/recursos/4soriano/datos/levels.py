# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL2 = [
        1,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('the city of %s') % _('Mercedes'), 1, _('Mercedes'), _('Es la capital del\ndepartamento')),
    (_('the town of %s') % _('Sacachispas'), 2, _('Sacachispas'), _("It's in the north")),
    (_('the town of %s') % _('El Tala'), 2, _('El Tala'), _("It's in the northeast")),
    (_('the city of %s') % _('Palmitas'), 2, _('Palmitas'), _('Está en el centro')),
    (_('the town of %s') % _('Colonia Concordia'), 2, _('Colonia Concordia'), _("It's in the west")),
    (_('the town of %s') % _('Egaña'), 2, _('Egaña'), _('Está en el centro')),
    (_('the town of %s') % _('Risso'), 2, _('Risso'), _('Está en el centro')),
    (_('the town of %s') % _('Rodó'), 2, _('Rodó'), _('Está en el centro')),
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
    (_('the %s') % _('Arroyo de Espinillo'), 3, _('A. de Espinillo'), _("It's in the southwest")),
    (_('the %s') % _('Arroyo del Sauce'), 3, _('A. del Sauce'), _("It's in the southwest")),
    (_('the %s') % _('Arroyo Bizcocho'), 3, _('A. Bizcocho'), _("It's in the west")),
    (_('the %s') % _('Arroyo Magallanes'), 3, _('A. Magallanes'), _("It's in the west")),
    (_('the %s') % _('Arroyo del Águila'), 3, _('A. del Águila'), _("It's in the southwest")),
    (_('the %s') % _('Arroyo del Corralito'), 3, _('A. del Corralito'), _("It's in the southwest")),
    (_('the %s') % _('Arroyo Maciel'), 3, _('A. Maciel'), _("It's in the south")),
    (_('the %s') % _('Arroyo San Martín'), 3, _('A. San Martín'), _("It's in the south")),
    (_('the %s') % _('Arroyo del Medio'), 3, _('A. del Medio'), _("It's in the south")),
    (_('the %s') % _('Arroyo de las Maulas'), 3, _('A. de las Maulas'), _("It's in the west")),
    (_('the %s') % _('Arroyo Bequeló'), 3, _('A. Bequeló'), _('Está en el centro')),
    (_('the %s') % _('Arroyo Coquimbo'), 3, _('A. Coquimbo'), _('Está en el centro')),
    (_('the %s') % _('Arroyo Sarandí'), 3, _('A. Sarandí'), _('Está en el centro')),
    (_('the %s') % _('Arroyo Caballudo'), 3, _('A. Caballudo'), _('Está en el centro')),
    (_('the %s') % _('Arroyo Maia'), 3, _('A. Maia'), _("It's in the north")),
    (_('the %s') % _('Arroyo Cololó'), 3, _('A. Cololó'), _("It's in the north")),
    (_('the %s') % _('Arroyo Perico'), 3, _('A. Perico'), _("It's in the north")),
    (_('the %s') % _('Arroyo de Vera'), 3, _('A. de Vera'), _("It's in the north")),
    (_('the %s') % _('Arroyo Grande'), 3, _('A. Grande'), _("It's in the northeast")),
    (_('the %s') % _('Arroyo del Perdido'), 3, _('A. del Perdido'), _("It's in the southeast")),
    (_('the %s') % _('Arroyo del Durazno'), 3, _('A. del Durazno'), _("It's in the southeast")),
    (_('the %s') % _('Arroyo Monzón'), 3, _('A. Monzón'), _("It's in the southeast"))
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
        1,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('the %s') % _('Ruta 2'), 6, _('Ruta 2'), _('Pasa por Palmitas')),
    (_('the %s') % _('Ruta 21'), 6, _('Ruta 21'), _('Pasa por Dolores')),
    (_('the %s') % _('Ruta 14'), 6, _('Ruta 14'), _('Va hasta Flores')),
    (_('the %s') % _('Ruta 96'), 6, _('Ruta 96'), _('Va hasta Villa Soriano')),
    (_('the %s') % _('Ruta 95'), 6, _('Ruta 95'), _('Sale de Mercedes')),
    (_('the %s') % _('Ruta 105'), 6, _('Ruta 105'), _('Va de Dolores\na Palmitas')),
    (_('the %s') % _('Ruta 55'), 6, _('Ruta 55'), _('Termina en\nJosé Enrique Rodó')),
    (_('the %s') % _('Ruta 12'), 6, _('Ruta 12'), _('Está en el límite\ncon Colonia')),
    (_('the %s') % _('Ruta 57'), 6, _('Ruta 57'), _('Va hasta Flores'))
]
]

LEVELS = [LEVEL2, LEVEL3, LEVEL4, LEVEL5]

