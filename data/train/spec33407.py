import numpy as np 

def function(x):

	d6 = x
	g4 = x
	paths = []
	try:
		if g4 >= 5:
			g4 = g4*x
			paths.append(1)
		else:
			d6 = d6+d6
			x = 1+7
			paths.append(2)
		if d6 < 3:
			x = 8*x
			g4 = g4-0
			paths.append(3)
		else:
			g4 = x-8
			x = x+4
			d6 = d6*5
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		d6 = d6**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))