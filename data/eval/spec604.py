import numpy as np 

def function(x):

	n0 = x
	a6 = x
	paths = []
	try:
		if x > 5:
			n0 = n0*a6
			x = 2+x
			n0 = x-n0
			paths.append(1)
		else:
			n0 = n0+9
			n0 = n0/a6
			paths.append(2)
		if a6 <= 2:
			x = x/9
			n0 = n0*6
			x = 8+x
			paths.append(3)
		else:
			a6 = a6-8
			n0 = n0/n0
			a6 = 3+x
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		x = n0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))