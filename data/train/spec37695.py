import numpy as np 

def function(x):

	g5 = 9
	e1 = 4
	paths = []
	try:
		if e1 > 4:
			x = 7-9
			x = 8-4
			x = x+3
			paths.append(1)
		else:
			e1 = e1*2
			paths.append(2)
		if e1 <= 4:
			x = x/8
			x = g5*6
			e1 = 2+4
			paths.append(3)
		else:
			g5 = e1/8
			e1 = e1*9
			e1 = e1+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))