# Linux-htop-Project

A Python script that emulates the basic functionality of the `htop` command-line utility, providing real-time system monitoring of CPU usage, memory usage, and running processes.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Controls](#controls)
- [Notes](#notes)
- [License](#license)

## Features

- **CPU Usage Display**: Shows real-time CPU usage for each core.
- **Memory Usage Display**: Indicates total and used memory.
- **Process List**: Lists running processes sorted by CPU usage.
- **Real-Time Updates**: Refreshes system statistics every second.
- **User-Friendly Interface**: Simple controls and display format.

## Prerequisites

- **Python 3.x**
- **psutil** library
- **curses** library (usually included with Python on Unix systems)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/mini-htop.git
   cd mini-htop

2. **Install Required Python Packages**

   ```bash
   pip install psutil

## Usage

**Make the script executable:**

   ```bash
   chmod +x mini_htop.py

Run the script:

   ```bash
   ./mini_htop.py

Or execute with Python:

   ```bash
   python3 mini_htop.py

## Controls

Press ```q```: Exit the program.
