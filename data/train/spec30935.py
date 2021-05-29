import numpy as np 

def function(x):

	l3 = 2
	g1 = 4
	paths = []
	try:
		if x >= 8:
			g1 = 2+g1
			g1 = g1*l3
			paths.append(1)
		else:
			g1 = g1*3
			x = l3-x
			g1 = l3/g1
			paths.append(2)
		if l3 <= 9:
			x = x+1
			l3 = l3*4
			x = x/8
			paths.append(3)
		else:
			g1 = g1/4
			l3 = l3*7
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