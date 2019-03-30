#!/bin/bash
cd convexHullNaive && python -m unittest convex_hull_test.py -v && cd ..
cd convexHullGrahamsScan && python -m unittest convex_hull_grahams_test.py -v && cd ..
