#!/bin/bash
source pyvenv/bin/activate
python live_plot.py measurements.csv 500 &
python main.py 
