import numpy as np 

def function(x):

	o1 = x
	g5 = 9
	paths = []
	try:
		if o1 < 5:
			o1 = 5*o1
			paths.append(1)
		else:
			x = 8-o1
			x = 5+o1
			paths.append(2)
		if o1 > 3:
			x = 7+x
			g5 = 6+g5
			paths.append(3)
		else:
			g5 = g5+1
			g5 = x*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g5 = x**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))