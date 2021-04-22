#!/usr/bin/env python

# Copyright (C) 2017 Seeed Technology Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#	 http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import numpy
import time
import colorsys

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

class RainbowLedPattern(object):
	def __init__(self, show=None, num_led=12):
		self.num_led = num_led
		
		jump = 1.0 / (self.num_led * 1.0)
		pixels = numpy.array([0.0] * 4 * self.num_led)
		for i in range(self.num_led):
			color = [jump * i, 0.5, 0.5]
			for j in range(3):
				pixels[(i * 4) + j + 1] = color[j]
		self.pixels = pixels
		
		if not show or not callable(show):
			def dummy(data):
				pass
			show = dummy

		self.show = show
		self.stop = False

	def convert_to_rgb(self, pixels_hsv):
		pixels_rgb = numpy.copy(pixels_hsv)
		for i in range(self.num_led):
			color_rgb = hsv2rgb(pixels_hsv[(i*4)+1], pixels_hsv[(i*4)+2], pixels_hsv[(i*4)+3])
			for j in range(3):
				pixels_rgb[(i*4)+j+1] = color_rgb[j]
		return pixels_rgb

	def wakeup(self, direction=0):
		position = int((direction + 15) / (360 / self.num_led)) % self.num_led
		pixels = self.convert_to_rgb(self.pixels)
		self.show(pixels)

	def listen(self):
		self.show(self.pixels)

	def think(self):
		pixels  = self.convert_to_rgb(self.pixels)
		while not self.stop:
			self.show(pixels)
			time.sleep(0.2)
			pixels = numpy.roll(pixels, 4)

	def change_sv(self, pixels_hsv, incr):
		pixels = numpy.copy(pixels_hsv)
		for i in range(self.num_led):
			pixels[(i*4)+2] += incr
			pixels[(i*4)+3] += incr
		return pixels

	def speak(self):
		pixels_hsv = numpy.copy(self.pixels)
		step = 0.025
		while not self.stop:
			pixels_hsv = self.change_sv(pixels_hsv, step)
			pixels_rgb = self.convert_to_rgb(pixels_hsv)
			self.show(pixels_rgb)
			time.sleep(0.1)
			if pixels_hsv[2] <= 0.5:
				step = 0.1
				time.sleep(0.4)
			elif pixels_hsv[2] >= 0.8:
				step = -0.1
				time.sleep(0.4)

	def off(self):
		self.show([0] * 4 * self.num_led)
