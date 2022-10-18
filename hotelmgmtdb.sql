-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 11, 2022 at 12:58 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotelmgmtdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `checkout`
--

CREATE TABLE `checkout` (
  `AllocatedRoomNumber` varchar(100) NOT NULL,
  `IDNumber` varchar(100) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `CheckInTime` varchar(100) NOT NULL,
  `CheckOutTime` varchar(100) NOT NULL,
  `AmountPaid` varchar(100) NOT NULL,
  `AmountLeft` varchar(100) NOT NULL,
  `PendingAmountPayment` varchar(100) NOT NULL,
  `CheckOutCustomerPic` varchar(100) NOT NULL,
  `UniqueCustomerHotelID` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `ID` varchar(100) NOT NULL,
  `ID_number` varchar(100) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Gender` varchar(20) NOT NULL,
  `PhoneNumber` varchar(100) NOT NULL,
  `Room_Type` varchar(20) NOT NULL,
  `Allocated_Room_Nnumber` varchar(20) NOT NULL,
  `Check_in_time` varchar(100) NOT NULL,
  `Amount_to_pay` varchar(100) NOT NULL,
  `Deposit` int(50) NOT NULL,
  `CustomerPic` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `Name` varchar(100) NOT NULL,
  `DOB` date NOT NULL,
  `Gender` varchar(50) NOT NULL,
  `Job` varchar(100) NOT NULL,
  `Salary` int(100) NOT NULL,
  `Phone` varchar(100) NOT NULL,
  `Aadhar` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `ProfilePic` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `rooms`
--

CREATE TABLE `rooms` (
  `RoomNumber` int(100) NOT NULL,
  `Availability` varchar(100) NOT NULL,
  `CleaningStatus` varchar(100) NOT NULL,
  `Price` int(100) NOT NULL,
  `BedType` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `usertable`
--

CREATE TABLE `usertable` (
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `usertype` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `checkout`
--
ALTER TABLE `checkout`
  ADD PRIMARY KEY (`UniqueCustomerHotelID`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`ID_number`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`Aadhar`);

--
-- Indexes for table `rooms`
--
ALTER TABLE `rooms`
  ADD PRIMARY KEY (`RoomNumber`);

--
-- Indexes for table `usertable`
--
ALTER TABLE `usertable`
  ADD PRIMARY KEY (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
