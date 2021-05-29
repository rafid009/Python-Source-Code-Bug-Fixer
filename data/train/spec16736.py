import numpy as np 

def function(x):

	o2 = 5
	g7 = 4
	paths = []
	try:
		if o2 < 7:
			g7 = g7+0
			o2 = o2+9
			paths.append(1)
		else:
			o2 = o2/9
			x = 8-8
			g7 = g7*g7
			paths.append(2)
		if o2 < 7:
			g7 = g7*7
			paths.append(3)
		else:
			o2 = o2-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o2 = x**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))