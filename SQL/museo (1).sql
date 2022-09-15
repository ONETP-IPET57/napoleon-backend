-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 15-09-2022 a las 22:00:13
-- Versión del servidor: 10.1.38-MariaDB
-- Versión de PHP: 7.1.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `museo`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `exhibition`
--

CREATE TABLE `exhibition` (
  `id_exhibition` int(11) NOT NULL,
  `name_exhibition` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `author` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `created_at` int(11) NOT NULL,
  `information` text COLLATE utf8_unicode_ci NOT NULL,
  `image` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `exhibition`
--

INSERT INTO `exhibition` (`id_exhibition`, `name_exhibition`, `author`, `created_at`, `information`, `image`) VALUES
(1, 'Sagrada Familia', 'Buglioni, Benedetto', 1459, 'Origen:Donación Torcuato Di Tella (Fundación e Instituto), 1971\r\nFecha:Fines del siglo XV - comienzos del siglo XVI\r\nPeríodo:Arte Siglo XII al Siglo XVIII\r\nEscuela:Italiana S.XV\r\nTécnica:Terracota esmaltada\r\nObjeto:Escultura\r\nEstilo:renacimiento\r\nGénero:religioso', ''),
(2, 'Bodas místicas de Santa Catalina', 'Negróni Pietro', 1503, 'Origen:Madariaga, Carlos y Anchorena de Madariaga, Josefa\r\nPeríodo:Arte Siglo XII al Siglo XVIII\r\nEscuela:Italiana S.XVI\r\nTécnica:Óleo\r\nObjeto:Pintura\r\nEstilo:manierismo\r\nGénero:religioso', ''),
(3, 'Santa Ana triple', 'Anónimo', 1971, 'Origen:Donación Torcuato Di Tella (Fundación e Instituto)\r\nFecha:Último cuarto del siglo XV\r\nPeríodo:Arte Siglo XII al Siglo XVIII\r\nEscuela:Alemana S.XV\r\nTécnica:Madera no policromada\r\nObjeto:Escultura\r\nEstilo:renacimiento, medieval\r\nGénero:gótico, religioso', ''),
(4, 'Retrato de mujer joven', 'Rembrandt Harmensz van Rijn', 1634, 'Origen:Donación, Hirsch (Quentin, Claudia Leonor Caraballo de- Hirsch, Sarah Saavedra Guani de- Caraballo, Octavio Alfredo y Hirsch, Mario).\r\nPeríodo:Arte Siglo XII al Siglo XVIII\r\nEscuela:Holandesa S.XVII\r\nTécnica:Óleo\r\nObjeto:Pintura\r\nEstilo:barroco\r\nGénero:retrato', ''),
(5, 'Presentación al templo', 'Willensz De Wet, Jacob', 1610, 'Origen:Adquisición a Pedro Noceti & Cía (Venta Lamas-Lavega, Bs. As. 1898)\r\nFecha:S. XVII\r\nPeríodo:Arte Siglo XII al Siglo XVIII\r\nEscuela:Holandesa S.XVII\r\nTécnica:Oleo\r\nObjeto: Pintura', ''),
(6, 'Retrato de un caballero', 'Anonimo', 1600, 'Origen:Donación Quentin Hirsch, Claudia Leonor Caraballo de Hirsch, Sarah Saavedra Guani de Hirsch, Octavio Caraballo Alfredo y Mario Hirsch, 1983\r\nFecha:c.1600\r\nPeríodo:Arte Siglo XII al Siglo XVIII\r\nEscuela:Holandesa S.XVII\r\nTécnica:Óleo\r\nObjeto:Pintura', ''),
(7, 'Baño de Ninfas (Las ninfas de Diana regresando de la pesca)', 'Balen, Hendrick van - Brueghel I, Jan', 1612, 'Origen: Legado Tempel de Bennewitz, Margarita Paulina Anna Minna. 1988\r\nFecha:Ca. 1612-1625\r\nPeríodo: Arte Siglo XII al Siglo XVIII\r\nEscuela: Flamenca S.XVII\r\nTécnica: Óleo\r\nObjeto: Pintura\r\nEstilo: barroco\r\nGénero: paisaje, mitológico', ''),
(8, 'El naufragio', 'Bakhuizen, Ludolf', 1631, 'Origen:Misión Schiaffino (en Amberes)\r\nPeríodo:Arte Siglo XII al Siglo XVIII\r\nEscuela:Holandesa S.XVII\r\nTécnica:Óleo\r\nObjeto:Pintura\r\nEstilo:barroco\r\nGénero:marina', ''),
(9, 'El triunfo de Baco', 'Yperen, Jan Thomas van', 1650, 'El triunfo de Baco\r\nAutor:Yperen, Jan Thomas van\r\n(Bélgica, Ypres, 1617 - Austria, Viena, 1673)\r\nOrigen:Donación de Emilio A. Candiani, 1933\r\nFecha:ca.1650\r\nPeríodo:Arte Siglo XII al Siglo XVIII\r\nEscuela:Flamenca S.XVII\r\nTécnica:Óleo\r\nObjeto:Pintura\r\nEstilo:barroco\r\nGénero:mitológico', ''),
(10, 'Aparición de San Isidoro al Rey Fernando el Santo ante los muros de Sevilla', 'Goya y Lucientes, Francisco José', 1798, '(España, Fuendetodos, 1746 - Francia, Burdeos, 1828)\r\nOrigen:Artal, José\r\nPeríodo:Arte Siglo XIX (1800-1910)\r\nEscuela:Española S.XIX\r\nTécnica:Óleo\r\nObjeto:Pintura\r\nEstilo:romanticismo\r\nGénero:religioso', ''),
(11, 'Incendio de un hospital', 'Goya y Lucientes, Francisco José', 1808, 'Origen:Donación Carlos Alberto, Arturo y Eduardo Acevedo, 1958\r\nPeríodo:Arte Siglo XIX (1800-1910)\r\nEscuela:Española S.XIX\r\nTécnica:Óleo\r\nObjeto:Pintura\r\nEstilo:romanticismo\r\nGénero:costumbres', ''),
(12, 'El estanque de la Ville d\'Avray', 'Corot, Jean-Baptiste Camille', 1865, 'Fecha:1865-1870\r\nPeríodo:Arte Siglo XIX (1800-1910)\r\nEscuela:Francesa S.XIX\r\nTécnica:Óleo\r\nObjeto:Pintura\r\nEstilo:naturalismo, realismo\r\nGénero:barbizon, paisaje', ''),
(13, 'El Canal de Briare', 'Harpignies, Henri Joseph', 1800, '(Francia, Valenciennes, 1819 - Francia, Saint-Privé, 1916)\r\nOrigen: Galería Witcomb (Buenos Aires)\r\nPeríodo:Arte Siglo XIX (1800-1910)\r\nEscuela:Francesa S.XIX\r\nTécnica:Óleo\r\nObjeto:Pintura\r\nEstilo:naturalismo, realismo\r\nGénero:barbizon, paisaje', ''),
(14, 'La tarde', 'Daubigny, Charles-François', 1817, '(Francia, París, 1817 - Francia, París, 1878)\r\nOrigen:Emilio Furt y Elena Gutiérrez de Furt\r\nPeríodo:Arte Siglo XIX (1800-1910)\r\nEscuela:Francesa S.XIX\r\nTécnica:Óleo\r\nObjeto:Pintura\r\nEstilo:naturalismo, realismo\r\nGénero:barbizon, paisaje', ''),
(15, 'Los primeros funerales', 'Barrias, Louis-Ernest', 1841, 'Origen:Ángel Roverano\r\nPeríodo:Arte Siglo XIX (1800-1910)\r\nEscuela:Francesa S.XIX\r\nTécnica:Talla\r\nObjeto:Escultura\r\nEstilo:naturalismo, académico\r\nGénero:salón, bíblico\r\nSoporte:Mármol', ''),
(16, 'Centauro', 'Barye, Antoine Louis', 1795, 'Origen:María Zoila Godoy de Cobo\r\nPeríodo:Arte Siglo XIX (1800-1910)\r\nEscuela:Francesa S.XIX\r\nTécnica:Modelado, vaciado\r\nObjeto:Escultura\r\nEstilo:clasicismo\r\nGénero:mitológico', ''),
(17, 'Roses blanches', 'Fantin Latour, Ignace Henri', 1836, '(Francia, Grenoble, 1836 - Francia, Buré, 1904)\r\nOrigen:Legado María Angélica Bancalari de Casenave, 1983\r\nFecha:1887\r\nPeríodo:Arte Siglo XIX (1800-1910)\r\nEscuela:Francesa S.XIX\r\nTécnica:Óleo\r\nObjeto:Pintura', ''),
(18, 'Violetas y azaleas', 'Fantin Latour, Ignace Henri', 1875, '(Francia, Grenoble, 1836 - Francia, Buré, 1904)\r\nOrigen:Misión Schiaffino (París)\r\nPeríodo:Arte Siglo XIX (1800-1910)\r\nEscuela:Francesa S.XIX\r\nTécnica:Óleo\r\nObjeto:Pintura\r\nEstilo:naturalismo\r\nGénero:naturaleza muerta', ''),
(19, 'Gran Canal y San Simeone Piccolo', 'Guardi, Francesco', 1971, 'Origen:Donación Torcuato Di Tella (Fundación e Instituto), 1971\r\nFecha:S. XVIII\r\nPeríodo:Arte Siglo XII al Siglo XVIII\r\nEscuela:Italiana S.XVIII\r\nTécnica:Óleo\r\nObjeto:Pintura', ''),
(20, 'Veduta dell\'Anfiteatro Flavio, detto il Colosseo.', 'Piranesi, Giovanni Battista', 1748, 'Origen:Donación del Ministerio de Justicia e Instrucción Pública, anterior a 1910\r\nFecha:1748-1778\r\nPeríodo:Arte Siglo XII al Siglo XVIII\r\nEscuela:Italiana S.XVIII\r\nTécnica:Aguafuerte\r\nObjeto:Grabado', ''),
(21, 'San Agustín meditando sobre la Trinidad', 'Petrini, Giuseppe Antonio', 1905, 'Origen:Donación Emilio Goldaracena, 1905\r\nPeríodo:Arte Siglo XII al Siglo XVIII\r\nEscuela:Italiana S.XVIII\r\nTécnica:Óleo\r\nObjeto:Pintura\r\nGénero:religioso', ''),
(22, 'Abel', 'Correa Morales, Lucio', 1902, 'Origen:Adquisición al autor, 1906. Fundición en bronce a cargo del MNBA en el taller de Alejo Joris, Buenos Aires, 1907-1908\r\nPeríodo:Arte Siglo XIX (1800-1910)\r\nEscuela:Argentina S.XX\r\nTécnica:Modelado, vaciado\r\nObjeto:Escultura\r\nEstilo:naturalismo, académico\r\nGénero:bíblico, salón, desnudo', ''),
(23, 'La vuelta al hogar', 'Mendilaharzu, Graciano', 1885, 'Período:Arte Siglo XIX (1800-1910)\r\nEscuela:Argentina S.XIX\r\nTécnica:Óleo\r\nObjeto:Pintura\r\nEstilo:naturalismo\r\nGénero:costumbrismo', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `guided_tours`
--

CREATE TABLE `guided_tours` (
  `id_guided_tours` int(11) NOT NULL,
  `name_guided_tours` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `id_schedule` int(11) NOT NULL,
  `description` text COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `guided_tours`
--

INSERT INTO `guided_tours` (`id_guided_tours`, `name_guided_tours`, `id_schedule`, `description`) VALUES
(1, 'Welcome tour', 1, 'Description tour');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `review`
--

CREATE TABLE `review` (
  `id_review` int(11) NOT NULL,
  `id_exhibition` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `score` float NOT NULL,
  `message` text COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `role`
--

CREATE TABLE `role` (
  `id_role` int(11) NOT NULL,
  `role` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `role`
--

INSERT INTO `role` (`id_role`, `role`) VALUES
(1, 'administrator'),
(2, 'user');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `schedule`
--

CREATE TABLE `schedule` (
  `id_schedule` int(11) NOT NULL,
  `hour_start` time NOT NULL,
  `hour_end` time NOT NULL,
  `days` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `schedule`
--

INSERT INTO `schedule` (`id_schedule`, `hour_start`, `hour_end`, `days`) VALUES
(1, '10:30:00', '12:00:00', 'Monday');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id_user` int(11) NOT NULL,
  `username` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `password` char(65) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `id_role` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id_user`, `username`, `password`, `email`, `id_role`) VALUES
(1, 'root', '1234', '', 1),
(3, 'Thejairex', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'yairjesus777@gmail.com', 2),
(4, 'Zenithv53', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'Claumont2011@live.com.ar', 2),
(5, 'Jair', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'jair@live.com.ar', 2),
(6, 'Jair2', 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35', 'jair2@live.com.ar', 2),
(7, 'Tikki', 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35', 'Tikki@live.com.ar', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `visit`
--

CREATE TABLE `visit` (
  `id_visit` int(11) NOT NULL,
  `id_guided_tours` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `reference_name` varchar(200) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `visit`
--

INSERT INTO `visit` (`id_visit`, `id_guided_tours`, `id_user`, `reference_name`) VALUES
(1, 1, 3, 'suiogb');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `exhibition`
--
ALTER TABLE `exhibition`
  ADD PRIMARY KEY (`id_exhibition`);

--
-- Indices de la tabla `guided_tours`
--
ALTER TABLE `guided_tours`
  ADD PRIMARY KEY (`id_guided_tours`),
  ADD KEY `id_schedule` (`id_schedule`);

--
-- Indices de la tabla `review`
--
ALTER TABLE `review`
  ADD PRIMARY KEY (`id_review`),
  ADD KEY `id_exhibition` (`id_exhibition`),
  ADD KEY `id_user` (`id_user`);

--
-- Indices de la tabla `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`id_role`);

--
-- Indices de la tabla `schedule`
--
ALTER TABLE `schedule`
  ADD PRIMARY KEY (`id_schedule`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id_user`),
  ADD KEY `id_role` (`id_role`);

--
-- Indices de la tabla `visit`
--
ALTER TABLE `visit`
  ADD PRIMARY KEY (`id_visit`),
  ADD KEY `id_guided_tours` (`id_guided_tours`),
  ADD KEY `id_user` (`id_user`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `exhibition`
--
ALTER TABLE `exhibition`
  MODIFY `id_exhibition` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT de la tabla `guided_tours`
--
ALTER TABLE `guided_tours`
  MODIFY `id_guided_tours` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `review`
--
ALTER TABLE `review`
  MODIFY `id_review` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `role`
--
ALTER TABLE `role`
  MODIFY `id_role` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `schedule`
--
ALTER TABLE `schedule`
  MODIFY `id_schedule` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `visit`
--
ALTER TABLE `visit`
  MODIFY `id_visit` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `guided_tours`
--
ALTER TABLE `guided_tours`
  ADD CONSTRAINT `guided_tours_ibfk_1` FOREIGN KEY (`id_schedule`) REFERENCES `schedule` (`id_schedule`);

--
-- Filtros para la tabla `review`
--
ALTER TABLE `review`
  ADD CONSTRAINT `review_ibfk_1` FOREIGN KEY (`id_exhibition`) REFERENCES `exhibition` (`id_exhibition`),
  ADD CONSTRAINT `review_ibfk_2` FOREIGN KEY (`id_user`) REFERENCES `user` (`id_user`);

--
-- Filtros para la tabla `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`id_role`) REFERENCES `role` (`id_role`);

--
-- Filtros para la tabla `visit`
--
ALTER TABLE `visit`
  ADD CONSTRAINT `visit_ibfk_1` FOREIGN KEY (`id_guided_tours`) REFERENCES `guided_tours` (`id_guided_tours`),
  ADD CONSTRAINT `visit_ibfk_2` FOREIGN KEY (`id_user`) REFERENCES `user` (`id_user`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
