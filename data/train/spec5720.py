import numpy as np 

def function(x):

	i8 = x
	n2 = x
	paths = []
	try:
		if n2 < 2:
			x = x+x
			x = i8+3
			paths.append(1)
		else:
			i8 = n2-0
			i8 = 1/i8
			n2 = n2/2
			paths.append(2)
		if x > 9:
			x = 2*x
			paths.append(3)
		else:
			n2 = x*n2
			n2 = n2*7
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		x = n2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))