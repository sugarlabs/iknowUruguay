# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL1 = [
        1,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('the city of %s') % _('Maldonado'), 2, _('Maldonado'), _('Es la capital del\ndepartamento')),
    (_('the town of %s') % _('Los Talas'), 2, _('Los Talas'), _("It's in the north")),
    (_('the town of %s') % _('Aiguá'), 2, _('Aiguá'), _("It's in the north")),
    (_('the health resort of %s') % _('José Ignacio'), 2, _('José Ignacio'), _("It's in the south")),
    (_('the city of %s') % _('San Carlos'), 2, _('San Carlos'), _("It's in the south")),
    (_('the city of %s') % _('Punta del Este'), 2, _('Punta del Este'), _("It's in the south")),
    (_('the city of %s') % _('Pan de Azúcar'), 2, _('Pan de Azúcar'), _("It's in the south")),
    (_('the city of %s') % _('Piriápolis'), 2, _('Piriápolis'), _("It's in the south")),
    (_('the health resort of %s') % _('Punta Ballena'), 2, _('Punta Ballena'), _("It's in the south")),
    (_('the town of %s') % _('Garzón'), 2, _('Garzón'), _("It's in the east")),
    (_('the health resort of %s') % _('Las Flores'), 2, _('Las Flores'), _("It's in the southwest")),
    (_('the health resort of %s') % _('La Barra'), 2, _('La Barra'), _("It's in the south"))
]
]

LEVEL2 = [
        1,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('the %s') % _('Río de la Plata'), 3, _('Río de la Plata'), _("It's in the south")),
    (_('the %s') % _('Océano Atlántico'), 3, _('Océano Atlántico'), _("It's in the south")),
    (_('the %s') % _('Arroyo Garzón'), 3, _('A. Garzón'), _("It's in the southeast")),
    (_('the %s') % _('Arroyo de Rocha'), 3, _('A. de Rocha'), _("It's in the east")),
    (_('the %s') % _('Arroyo Valdivia'), 3, _('A. Valdivia'), _("It's in the east")),
    (_('the %s') % _('Arroyo del Alferez'), 3, _('A. del Alferez'), _("It's in the east")),
    (_('the %s') % _('Arroyo del Aiguá'), 3, _('A. del Aiguá'), _("It's in the north")),
    (_('the %s') % _('Arroyo Sarandí'), 3, _('A. Sarandí'), _("It's in the north")),
    (_('the %s') % _('Arroyo del León'), 3, _('A. del León'), _("It's in the north")),
    (_('the %s') % _('Arroyo Solís Gr.'), 3, _('A. Solís Gr.'), _("It's in the southwest")),
    (_('the %s') % _('Arroyo Coronilla'), 3, _('A. Coronilla'), _('Está en el centro')),
    (_('the %s') % _('Arroyo Sauce'), 3, _('A. Sauce'), _("It's in the southwest")),
    (_('the %s') % _('Arroyo Pan de Azúcar'), 3, _('A. Pan de Azúcar'), _("It's in the south")),
    (_('the %s') % _('Arroyo del Sauce'), 3, _('A. del Sauce'), _("It's in the south")),
    (_('the %s') % _('Arroyo Mataojo'), 3, _('A. Mataojo'), _("It's in the south")),
    (_('the %s') % _('Arroyo de las Cañas'), 3, _('A. de las Cañas'), _('Está en el centro')),
    (_('the %s') % _('Arroyo de los Caracoles'), 3, _('A. de los Caracoles'), _('Está en el centro')),
    (_('the %s') % _('Arroyo de los Carpés'), 3, _('A. de los Carpés'), _('Está en el centro')),
    (_('the %s') % _('Arroyo San Carlos'), 3, _('A. San Carlos'), _("It's in the south")),
    (_('the %s') % _('Arroyo Maldonado'), 3, _('A. Maldonado'), _("It's in the south")),
    (_('the %s') % _('Arroyo J. Ignacio'), 3, _('A. J. Ignacio'), _("It's in the southeast")),
    (_('the %s') % _('Laguna Garzón'), 3, _('Lag. Garzón'), _("It's in the southeast")),
    (_('the %s') % _('Laguna J. Ignacio'), 3, _('Lag. J. Ignacio'), _("It's in the southeast")),
    (_('the %s') % _('Laguna del Sauce'), 3, _('Lag. del Sauce'), _("It's in the southwest"))
]
]

LEVEL3 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %s') % _('Sierra de las Cañas'), 4, _('Sierra de las Cañas'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Sierra de los Caracoles'), 4, _('Sierra de los Caracoles'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Sierra de las Ánimas'), 4, _('Sierra de las Ánimas'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Sierra de la Ballena'), 4, _('Sierra de la Ballena'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Sierra de Carapé'), 4, _('Sierra de Carapé'), _('Dále, probá de nuevo')),
    (_('the %s') % _('Cerro del Toro'), 5, _('Co. del Toro'), _('Queda cerca de Piriápolis')),
    (_('the %s') % _('Cerro San Antonio'), 5, _('Co. San Antonio'), _('Queda cerca de Piriápolis')),
    (_('the %s') % _('Cerro Pan de Azúcar'), 5, _('Co. Pan de Azúcar'), _('Queda al sur')),
    (_('the %s') % _('Cerro Catedral'), 5, _('Co. Catedral'), _('Es el más alto del país'))
]
]

LEVEL4 = [
        1,
        _('Routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('the %s') % _('Ruta 9'), 6, _('Ruta 9'), _('Cruza el departamento\nde oeste a este')),
    (_('the %s') % _('Ruta Interbalnearia'), 6, _('Ruta IB'), _('Viene de los balnearios\nde Canelones')),
    (_('the %s') % _('Ruta 60'), 6, _('Ruta 60'), _('Viene de Minas')),
    (_('the %s') % _('Ruta 37'), 6, _('Ruta 37'), _('Va hasta Piriápolis')),
    (_('the %s') % _('Ruta 12'), 6, _('Ruta 12'), _('Viene de Minas')),
    (_('the %s') % _('Ruta 93'), 6, _('Ruta 93'), _('Pasa por el principal balneario')),
    (_('the %s') % _('Ruta 39'), 6, _('Ruta 39'), _('Pasa por San Carlos')),
    (_('the %s') % _('Ruta 13'), 6, _('Ruta 13'), _('Pasa por Aiguá')),
    (_('the %s') % _('Ruta 109'), 6, _('Ruta 109'), _('Pasa por Aiguá'))
]
]

LEVELS = [LEVEL1, LEVEL2, LEVEL3, LEVEL4]

