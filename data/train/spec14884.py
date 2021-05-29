import numpy as np 

def function(x):

	j5 = 6
	p4 = 1
	paths = []
	try:
		if j5 < 2:
			x = p4*j5
			x = 0-x
			j5 = 7-3
			paths.append(1)
		else:
			x = x*p4
			paths.append(2)
		if j5 > 3:
			x = x*j5
			paths.append(3)
		else:
			p4 = 8-3
			x = 0-x
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j5 = x**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))