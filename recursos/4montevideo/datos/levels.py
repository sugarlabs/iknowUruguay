# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL1 = [
        17,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('Santiago Vázquez'), _("It's on the border\nwith %s") % _('San José')),
    (_('Ciudad Vieja'), _('Try again')),
    (_('Centro'), _("It's near of %s") % _('Ciudad Vieja')),
    (_('Sur'), _("It's in the south")),
    (_('Palermo'), _("It's in the south")),
    (_('Cordón'), _("It's near of %s") % _('Centro')),
    (_('Aguada'), _('Try again')),
    (_('Punta Carretas'), _('Try again')),
    (_('Pocitos'), _('Try again')),
    (_('Buceo'), _('Try again')),
    (_('Malvín'), _('Try again')),
    (_('Punta Gorda'), _('Try again')),
    (_('Carrasco'), _("It's in the east")),
    (_('Parque Batlle'), _('Try again')),
    (_('Unión'), _("It's in the east")),
    (_('Maroñas'), _("It's near of %s") % _('Unión')),
    (_('Villa Española'), _("It's near of %s") % _('Unión')),
    (_('Capurro'), _('It is on the bay')),
    (_('Prado'), _('Queda al norte de la bahía')),
    (_('Belvedere'), _("It's near of %s") % _('Prado')),
    (_('Cerro'), _('It is on the bay')),
    (_('Casabó'), _("It's near of %s") % _('Cerro')),
    (_('La Teja'), _('It is on the bay')),
    (_('Nuevo París'), _("It's in the northwest")),
    (_('Sayago'), _("It's in the north")),
    (_('Peñarol'), _("It's in the north")),
    (_('Colón'), _("It's in the north")),
    (_('Casavalle'), _("It's in the north")),
    (_('Cerrito de la Victoria'), _("It's in the north")),
    (_('Jardines del Hipódromo'), _("It's in the northeast")),
    (_('Piedras Blancas'), _("It's in the north")),
    (_('Punta de Rieles'), _("It's in the northeast")),
    (_('Brazo Oriental'), _("It's near of %s") % _('Prado')),
    (_('Jacinto Vera'), _("It's in the north")),
    (_('Lezica'), _("It's near of %s") % _('Colón')),
    (_('Paso de la Arena'), _("It's in the west")),
    (_('Villa García'), _("It's in the northeast")),
    (_('Manga'), _("It's in the north"))
]
]

LEVEL2 = [
        1,
        _('Information'),
        ['lineasDepto', 'capitales', 'ciudades'],
        ['capitales', 'ciudades'],
[
    (_('the highest point\nof the department'), 5, _('Cerro de Montevideo'), _('It is the symbol of the department')),
    (_('the second highest\npoint in the department'), 2, _('Cerrito de la Victoria'), _('It is a popular neighborhood')),
    (_('the stream that borders with Canelones'), 3, _('Arroyo Carrasco'), _('Flows in the %s') % _('Río de la Plata')),
    (_('the neighborhood where\nthe city was originally\nfounded in San Felipe\nand Santiago of Montevideo'), 2, _('Ciudad Vieja'), _('It is on the bay')),
    (_('the neighborhood where\nthey operated railway\nworkshops'), 2, _('Peñarol'), _('An important football\nteam named after him')),
    (_('The neighborhood is\nnamed after the area\nwhere there were\nnumerous water wells'), 2, _('Aguada'), _('It is currently\nlocated where the \nLegislative Palace')),
    (_('the beach where\nattending washerwomen\ndoing laundry wells'), 2, _('Pocitos'), _('It is a very busy beach')),
    (_('the neighborhood\nfrom where the parade of Llamadas start'), 2, _('Sur'), _("It's in the south")),
    (_('where is the\n"World Football Monument"'), 2, _('Parque Batlle'), _('The "World Soccer Monument" is the Estadio Centenario')),
    (_('the river that supplies\ndrinking water to\nthe department of\nMontevideo'), 3, _('Río Santa Lucía'), _("It's on the border\nwith %s") % _('San José'))
]
]
	
LEVEL3 = [
        15,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('Río de la Plata'), _("It's in the south")),
    (_('Río Santa Lucía'), _("It's on the border\nwith %s") % _('San José')),
    (_('Arroyo Colorado'), _('Flows in the %s') % _('Río Santa Lucía')),
    (_('Arroyo de Melilla'), _('Flows in the %s') % _('Río Santa Lucía')),
    (_('Arroyo San Gregorio'), _('Flows in the %s') % _('Río Santa Lucía')),
    (_('Arroyo Pantanoso'), _('Flows in the %s') % _('Bahía de Montevideo')),
    (_('Arroyo Miguelete'), _('Flows in the %s') % _('Bahía de Montevideo')),
    (_('Arroyo Mendoza'), __('Flows in the %s') % _('Arroyo Miguelete')),
    (_('Arroyo de las Piedras'), _("It's on the border\nwith %s") % _('Canelones')),
    (_('Arroyo Toledo'), _("It's on the border\nwith %s") % _('Canelones')),
    (_('Arroyo Carrasco'), _("It's in the east")),
    (_('Arroyo Manga'), _("It's in the northeast"))
]
]

LEVEL4 = [
        1,
        _('Elevations'),
        ['cuchillas', 'cerros'],
        [],
[
    (_('the %(f)s') % {'f': _('Cuchilla Grande')}, 4, _('Cuchilla Grande'), _('Try again')),
    (_('the %(m)s') % {'m': _('Cabo de Pereira')}, 4, _('Cabo de Pereira'), _('Try again')),
    (_('the %(m)s') % {'m': _('Cerro de Montevideo')}, 5, _('Cerro de Montevideo'), _('Try again'))
]
]

LEVEL5 = [
        1,
        _('Avenues and routes'),
        ['rutas', 'capitales'],
        ['capitales', 'ciudades'],
[
    (_('la Avenida\n18 de Julio'), 6, _('18 de Julio'), _('Try again')),
    (_('Boulevard Artigas'), 6, _('Boulevard Artigas'), _('Try again')),
    (_('la Avenida Rivera'), 6, _('Rivera'), _('Try again')),
    (_('Avenida Italia'), 6, _('Avenida Italia'), _('Try again')),
    (_('Camino Carrasco'), 6, _('Camino Carrasco'), _('Try again')),
    (_('Camino Maldonado'), 6, _('Camino Maldonado'), _('Try again')),
    (_('la Avenida\n8 de Octubre'), 6, _('8 de Octubre'), _('Try again')),
    (_('la Avenida Belloni'), 6, _('Belloni'), _('Try again')),
    (_('Camino Mendoza'), 6, _('Mendoza'), _('Try again')),
    (_('la Avenida\nGeneral Flores'), 6, _('General Flores'), _('Try again')),
    (_('la Avenida J. Batlle\ny Ordóñez (Propios)'), 6, _('Propios'), _('Try again')),
    (_('la Avenida de las\nInstrucciones'), 6, _('Instrucciones'), _('Try again')),
    (_('la Avenida Agraciada'), 6, _('Agraciada'), _('Try again')),
    (_('la Avenida Garzón'), 6, _('Garzón'), _('Try again')),
    (_('los Accesos de las\Rutas 1 y 5'), 6, _('Accesos'), _('Try again')),
    (_('Ruta 1'), 6, _('Ruta 1'), _('Try again')),
    (_('Ruta 5'), 6, _('Ruta 5'), _('Try again')),
    (_('la Avenida Luis\nB. Berres'), 6, _('Luis Batlle Berres'), _('Try again')),
    (_('Camino Sanguinetti'), 6, _('Camino Sanguinetti'), _('Try again')),
    (_('Camino Tomkinson'), 6, _('Camino Tomkinson'), _('Try again')),
    (_('Camino Cibils'), 6, _('Camino Cibils'), _('Try again')),
    (_('Camino Melilla'), 6, _('Camino Melilla'), _('Try again'))
]
]

LEVELS = [LEVEL1, LEVEL2, LEVEL3, LEVEL4, LEVEL5]

