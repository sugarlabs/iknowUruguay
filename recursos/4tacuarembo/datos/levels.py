# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL1 = [
        7,
        _('Departments'),
        ['lineasDepto'],
        [],
[
    (_('Artigas'), _("It's easy")),
    (_('Rivera'), _("It's easy")),
    (_('Cerro Largo'), _("It's easy")),
    (_('Durazno'), _("It's easy")),
    (_('Río Negro'), _("It's easy")),
    (_('Paysandú'), _("It's easy")),
    (_('Salto'), _("It's easy")),
    (_('Tacuarembó'), _("It's easy")),
    (_('Treinta y Tres'), _("It's easy"))
]
]

LEVEL2 = [
        1,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('the city of %s') % _('Tacuarembó'), 2, _('Tacuarembó'), _("It's the capital of\nthe department")),
    (_('the town of %s') % _('Paso del Cerro'), 2, _('Paso del Cerro'), _("It's in the north")),
    (_('the city of %s') % _('Ansina'), 2, _('Ansina'), _("It's in the northeast")),
    (_('the town of %s') % _('Piedra Sola'), 2, _('Piedra Sola'), _("It's in the west")),
    (_('the town of %s') % _('Curtina'), 2, _('Curtina'), _('Está en el centro')),
    (_('the town of %s') % _('Achar'), 2, _('Achar'), _("It's in the southwest")),
    (_('the town of %s') % _('Peralta'), 2, _('Peralta'), _("It's in the southwest")),
    (_('the health resort of %s') % _('San Gregorio de Polanco'), 2, _('San Gregorio de Polanco'), _("It's in the south")),
    (_('the town of %s') % _('Rincón de Pereira'), 2, _('Rincón de Pereira'), _("It's in the southeast")),
    (_('the city of %s') % _('Paso de los Toros'), 2, _('Paso de los Toros'), _("It's in the southwest")),
    (_('the town of %s') % _('Cuchilla de Caraguatá'), 2, _('Cuchilla de Caraguatá'), _("It's in the southeast")),
    (_('the town of %s') % _('Picada de Cuello'), 2, _('Picada de Cuello'), _("It's in the east")),
    (_('the town of %s') % _('Valle Edén'), 2, _('Valle Edén'), _("It's in the west")),
    (_('the town of %s') % _('Martinote'), 2, _('Martinote'), _('Está en el centro'))
]
]

LEVEL3 = [
        15,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('Tacuarembó'), _('Está en el centro')),
    (_('Negro'), _("It's in the south")),
    (_('Salsipuedes Gr.'), _("It's in the southwest")),
    (_('Salsipuedes Ch.'), _("It's in the southeast")),
    (_('Cardoso'), _("It's in the southwest")),
    (_('Malo'), _("It's in the west")),
    (_('de la Quebrada'), _('Está en el centro')),
    (_('Rolón'), _("It's in the southwest")),
    (_('de Clara'), _("It's in the south")),
    (_('Caraguatá'), _("It's in the southeast")),
    (_('Yaguarí'), _("It's in the east")),
    (_('de los Sauces'), _("It's in the east")),
    (_('Laureles'), _("It's in the north")),
    (_('Tacuarembó Ch.'), _("It's in the northwest")),
    (_('Tranqueras'), _('Está al nororeste')),
    (_('Batoví'), _('Está en el centro')),
    (_('Tres Cruces'), _("It's in the northwest")),
    (_('Cañas'), _("It's in the north"))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %s') % _('Cuchilla de\las Tres Cruces'), 4, _('Cuchilla de las Tres Cruces'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cuchilla de Yaguarí'), 4, _('Cuchilla de Yaguarí'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cuchilla del Caraguata'), 4, _('Cuchilla del Caraguata'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cuchilla de Peralta'), 4, _('Cuchilla de Peralta'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cuchilla de Haedo'), 4, _('Cuchilla de Haedo'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cerro de las Minas'), 5, _('Co. de las Minas'), _("It's in the west")),
    (_('the %s') % _('Cerros de Batoví'), 5, _('Cos. de Batoví'), _('Están cerca de la capital')),
    (_('the %s') % _('Cerro Lambaré'), 5, _('Co. Lambaré'), _("It's in the northwest")),
    (_('the %s') % _('Cerro del Ñandubal'), 5, _('Co. del Ñandubal'), _("It's in the northeast"))
]
]

LEVEL5 = [
        5,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('Route %s') % 5, _('Cruza el departamento\nde norte a sur')),
    (_('Route %s') % 6, _('Pasa por\nCuchilla de Caraguatá')),
    (_('Route %s') % 26, _('Pasa por Ansina')),
    (_('Route %s') % 31, _('Viene de Salto')),
    (_('Route %s') % 43, _('Va hasta\nSan Gregorio de Polanco')),
    (_('Route %s') % 20, _('Viene de Río Negro'))
]
]

LEVELS = [LEVEL1, LEVEL2, LEVEL3, LEVEL4, LEVEL5]

