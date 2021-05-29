import numpy as np 

def function(x):

	e0 = x
	l3 = 0
	paths = []
	try:
		if l3 >= 3:
			e0 = 1-e0
			paths.append(1)
		else:
			x = x+3
			x = 8*l3
			paths.append(2)
		if e0 >= 0:
			e0 = e0*x
			e0 = e0*1
			paths.append(3)
		else:
			l3 = 1-7
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		x = l3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))