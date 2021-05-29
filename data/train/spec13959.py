import numpy as np 

def function(x):

	j0 = x
	p2 = 3
	paths = []
	try:
		if j0 >= 6:
			j0 = 6*j0
			x = x+j0
			x = j0+x
			paths.append(1)
		else:
			p2 = p2*j0
			p2 = p2*p2
			paths.append(2)
		if j0 >= 1:
			j0 = p2-p2
			paths.append(3)
		else:
			p2 = 7/2
			j0 = p2*j0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j0 = x**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))