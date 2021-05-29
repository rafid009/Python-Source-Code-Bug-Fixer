import numpy as np 

def function(x):

	g9 = x
	o9 = 8
	paths = []
	try:
		if g9 > 4:
			g9 = 6-g9
			o9 = o9*5
			x = x-2
			paths.append(1)
		else:
			o9 = 1*o9
			o9 = 9*1
			g9 = 3-g9
			paths.append(2)
		if x > 0:
			x = x-3
			x = x-x
			paths.append(3)
		else:
			x = x-4
			o9 = o9*7
			x = x+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o9 = x**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))