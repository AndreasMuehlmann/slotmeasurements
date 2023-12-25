#!/bin/bash
source pyvenv/bin/activate
python live_plot.py measurements.csv 500 &
python live_display.py measurements.csv &
python main.py 
