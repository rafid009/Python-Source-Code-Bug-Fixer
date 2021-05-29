import numpy as np 

def function(x):

	z0 = x
	p6 = 3
	paths = []
	try:
		if x < 5:
			p6 = p6/1
			p6 = p6*x
			x = 2-8
			paths.append(1)
		else:
			p6 = x*9
			x = 0+1
			paths.append(2)
		if x <= 0:
			p6 = 4/p6
			p6 = 3+p6
			paths.append(3)
		else:
			p6 = 9/x
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		x = z0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))