#!/bin/bash
cd convexHullNaive && python -m unittest convex_hull_test.py -v
cd ..
cd convexHullGrahamsScan && python -m unittest convex_hull_grahams_test.py -v
cd ..
cd insertionSort && python -m unittest insertion_sort_test.py -v
cd ..
cd quickSort && python -m unittest quick_sort_test.py -v 
