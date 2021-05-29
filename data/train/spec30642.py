import numpy as np 

def function(x):

	n4 = x
	i0 = x
	paths = []
	try:
		if x <= 4:
			x = 3+2
			i0 = 3/3
			paths.append(1)
		else:
			x = 2*x
			x = 7+6
			i0 = i0*6
			paths.append(2)
		if n4 < 1:
			n4 = 2/n4
			x = x*x
			i0 = x+x
			paths.append(3)
		else:
			x = 6+8
			n4 = n4-x
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		x = n4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))