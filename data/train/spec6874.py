import numpy as np 

def function(x):

	l2 = 5
	d3 = 7
	paths = []
	try:
		if d3 > 6:
			l2 = l2*l2
			paths.append(1)
		else:
			d3 = 2-d3
			paths.append(2)
		if l2 >= 7:
			x = 5+x
			l2 = 2+l2
			d3 = 9+9
			paths.append(3)
		else:
			d3 = 1+d3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l2 = x**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))