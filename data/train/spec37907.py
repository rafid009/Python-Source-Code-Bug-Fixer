import numpy as np 

def function(x):

	l3 = 2
	g1 = 2
	paths = []
	try:
		if g1 >= 8:
			g1 = g1*7
			x = x/g1
			l3 = 1/l3
			paths.append(1)
		else:
			l3 = l3-2
			paths.append(2)
		if g1 < 5:
			l3 = 3-l3
			g1 = g1+9
			paths.append(3)
		else:
			l3 = x-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l3 = x**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))