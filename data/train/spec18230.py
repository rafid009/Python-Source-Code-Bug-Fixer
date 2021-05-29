import numpy as np 

def function(x):

	n2 = x
	i4 = x
	paths = []
	try:
		if n2 >= 2:
			x = x-n2
			i4 = i4+i4
			x = 0*3
			paths.append(1)
		else:
			x = i4/8
			i4 = 2/n2
			paths.append(2)
		if n2 < 9:
			i4 = 0+8
			n2 = 1+4
			i4 = i4/i4
			paths.append(3)
		else:
			x = 3+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n2 = x**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))