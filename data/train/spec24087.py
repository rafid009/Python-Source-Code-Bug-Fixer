import numpy as np 

def function(x):

	p6 = 0
	a3 = x
	paths = []
	try:
		if x < 2:
			p6 = p6+1
			paths.append(1)
		else:
			x = 6*x
			a3 = a3-9
			paths.append(2)
		if x > 2:
			p6 = p6-7
			paths.append(3)
		else:
			x = 3+x
			p6 = p6+x
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		x = p6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))