import numpy as np 

def function(x):

	f0 = 9
	o7 = 6
	paths = []
	try:
		if x <= 5:
			f0 = 6*f0
			paths.append(1)
		else:
			f0 = 8-f0
			x = x/1
			f0 = 2+f0
			paths.append(2)
		if f0 < 4:
			o7 = o7*f0
			paths.append(3)
		else:
			f0 = 9*f0
			f0 = 1/f0
			o7 = 8-o7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o7 = x**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))