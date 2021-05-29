import numpy as np 

def function(x):

	d6 = x
	i1 = x
	x = 5
	paths = []
	try:
		if d6 < 3:
			i1 = 3/d6
			i1 = 5*d6
			d6 = 5*d6
			paths.append(1)
		else:
			i1 = 4-i1
			paths.append(2)
		if d6 > 0:
			d6 = 7+x
			x = 3*x
			paths.append(3)
		else:
			x = x*7
			x = d6/4
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		i1 = d6**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))