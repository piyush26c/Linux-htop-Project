#!/usr/bin/env python3

import curses
import time
import psutil
import os

def draw_menu(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Non-blocking input
    max_y, max_x = stdscr.getmaxyx()
    
    while True:
        stdscr.erase()
        height, width = stdscr.getmaxyx()

        # CPU Usage
        cpu_percents = psutil.cpu_percent(percpu=True)
        cpu_usage_str = "CPU Usage: " + " | ".join([f"CPU{i}: {perc}%" for i, perc in enumerate(cpu_percents)])
        stdscr.addstr(0, 0, cpu_usage_str[:width])

        # Memory Usage
        mem = psutil.virtual_memory()
        mem_usage_str = f"Memory Usage: {mem.percent}% ({mem.used // (1024 ** 2)}MB / {mem.total // (1024 ** 2)}MB)"
        stdscr.addstr(1, 0, mem_usage_str[:width])

        # Process List Header
        stdscr.addstr(3, 0, f"{'PID':<6}{'USER':<10}{'CPU%':<6}{'MEM%':<6}{'NAME':<20}"[:width])

        # Process List
        processes = []
        for proc in psutil.process_iter(['pid', 'username', 'cpu_percent', 'memory_percent', 'name']):
            try:
                processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        # Sort processes by CPU usage
        processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)
        for idx, proc in enumerate(processes[:height - 5]):
            proc_str = f"{proc['pid']:<6}{proc['username'][:9]:<10}{proc['cpu_percent']:<6.1f}{proc['memory_percent']:<6.1f}{proc['name'][:19]:<20}"
            stdscr.addstr(4 + idx, 0, proc_str[:width])

        stdscr.refresh()
        time.sleep(1)

        # Exit on 'q' key press
        key = stdscr.getch()
        if key == ord('q'):
            break

def main():
    curses.wrapper(draw_menu)

if __name__ == '__main__':
    main()
