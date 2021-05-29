import numpy as np 

def function(x):

	a5 = 1
	d3 = x
	paths = []
	try:
		if a5 <= 3:
			d3 = d3-x
			paths.append(1)
		else:
			a5 = 3+d3
			paths.append(2)
		if a5 < 7:
			d3 = d3+8
			a5 = x+a5
			x = x/d3
			paths.append(3)
		else:
			a5 = 4*a5
			d3 = d3/2
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		a5 = a5**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))