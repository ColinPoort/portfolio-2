-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Gegenereerd op: 02 jun 2024 om 14:29
-- Serverversie: 10.4.32-MariaDB
-- PHP-versie: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `factsdb`
--

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `facts`
--

CREATE TABLE `facts` (
  `id` bigint(20) NOT NULL,
  `titel` varchar(255) NOT NULL,
  `beschrijving` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Gegevens worden geëxporteerd voor tabel `facts`
--

INSERT INTO `facts` (`id`, `titel`, `beschrijving`) VALUES
(1, 'Clouds', 'A cloud weighs around a million tonnes.'),
(2, 'Giraffes', 'Giraffes are 30 times more likely to get hit by lightning than people.'),
(3, 'Twins', 'Identical twins don’t have the same fingerprints.'),
(4, 'Earth-1218', 'Earth’s rotation is changing speed every year. Per century, the average day will become 1.8 seconds longer.'),
(5, '', '');

--
-- Indexen voor geëxporteerde tabellen
--

--
-- Indexen voor tabel `facts`
--
ALTER TABLE `facts`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT voor geëxporteerde tabellen
--

--
-- AUTO_INCREMENT voor een tabel `facts`
--
ALTER TABLE `facts`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
