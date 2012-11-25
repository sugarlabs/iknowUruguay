# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL2 = [
        1,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('the city of %s') % _('Fray Bentos'), 2, _('Fray Bentos'), _('Es la capital del\ndepartamento')),
    (_('the town of %s') % _('Merinos'), 2, _('Merinos'), _("It's in the northeast")),
    (_('the town of %s') % _('Algorta'), 2, _('Algorta'), _("It's in the north")),
    (_('the town of %s') % _('P. de los Mellizos'), 2, _('P. de los Mellizos'), _("It's in the northeast")),
    (_('the town of %s') % _('Sarandí de Navarro'), 2, _('Sarandí de Navarro'), _("It's in the northeast")),
    (_('the town of %s') % _('Paso de la Cruz'), 2, _('Paso de la Cruz'), _("It's in the north")),
    (_('the town of %s') % _('San Javier'), 2, _('San Javier'), _("It's in the northwest")),
    (_('the town of %s') % _('Young'), 2, _('Young'), _('Está en el centro')),
    (_('the town of %s') % _('Tres Quintas'), 2, _('Tres Quintas'), _("It's in the west")),
    (_('the town of %s') % _('Bellaco'), 2, _('Bellaco'), _("It's in the west")),
    (_('the town of %s') % _('Grecco'), 2, _('Grecco'), _("It's in the southeast")),
    (_('the town of %s') % _('Nuevo Berlín'), 2, _('Nuevo Berlín'), _("It's in the southwest"))
]
]

LEVEL3 = [
        1,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('the %s') % _('Río Uruguay'), 3, _('Río Uruguay'), _("It's in the west")),
    (_('the %s') % _('Río Negro'), 3, _('Río Negro'), _("It's in the south")),
    (_('the %s') % _('Arroyo Grande'), 3, _('A. Grande'), _("It's in the south")),
    (_('the %s') % _('Arroyo de las Flores'), 3, _('A. de las Flores'), _("It's in the southeast")),
    (_('the %s') % _('Arroyo Averías Gr.'), 3, _('A. Averías Gr.'), _("It's in the northeast")),
    (_('the %s') % _('Arroyo Averías Ch.'), 3, _('. Averías Ch.'), _('Está en el centro')),
    (_('the %s') % _('Arroyo Ñandubay'), 3, _('A. Ñandubay'), _("It's in the south")),
    (_('the %s') % _('Arroyo Don Esteban'), 3, _('A. Don Esteban'), _("It's in the north")),
    (_('the %s') % _('Arroyo Santa María'), 3, _('A. Santa María'), _("It's in the north")),
    (_('the %s') % _('Arroyo Negro'), 3, _('A. Negro'), _("It's in the northwest")),
    (_('the %s') % _('Arroyo Bellaco'), 3, _('A. Bellaco'), _("It's in the northwest")),
    (_('the %s') % _('Arroyo Gutiérrez'), 3, _('A. Gutiérrez'), _("It's in the northwest")),
    (_('the %s') % _('Arroyo Coladeras'), 3, _('A. Coladeras'), _("It's in the southwest")),
    (_('the %s') % _('Arroyo Sánchez'), 3, _('A. Sánchez'), _("It's in the southwest")),
    (_('the %s') % _('Arroyo Salsipuedes Gr.'), 3, _('A. Salsipuedes Gr.'), _("It's in the northeast")),
    (_('the %s') % _('Arroyo Tres Árboles'), 3, _('A. Tres Árboles'), _("It's in the northeast")),
    (_('the %s') % _('Arroyo Rolón'), 3, _('A. Rolón'), _("It's in the northwest")),
    (_('the %s') % _('Arroyo Molles'), 3, _('A. Molles'), _("It's in the southeast"))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %s') % _('Cuchilla de Haedo'), 4, _('Cuchilla de Haedo'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cuchilla de Navarro'), 4, _('Cuchilla de Navarro'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cerro Pelado'), 5, _('Co. Pelado'), _('Queda al sur')),
    (_('the %s') % _('Cerro del Quebracho'), 5, _('Co. del Quebracho'), _('Queda en el centro'))
]
]

LEVEL5 = [
        1,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('the %s') % _('Ruta 2'), 6, _('Ruta 2'), _('Viene de Mercedes')),
    (_('the %s') % _('Ruta 24'), 6, _('Ruta 24'), _('Va a Paysandú')),
    (_('the %s') % _('Ruta 3'), 6, _('Ruta 3'), _('Pasa por Young')),
    (_('the %s') % _('Ruta 20'), 6, _('Ruta 20'), _('Va hacia el este')),
    (_('the %s') % _('Ruta 25'), 6, _('Ruta 25'), _('Pasa por Young')),
    (_('the %s') % _('Ruta 4'), 6, _('Ruta 4'), _('Pasa por la represa\nde Baygorria'))
]
]

LEVELS = [LEVEL2, LEVEL3, LEVEL4, LEVEL5]

