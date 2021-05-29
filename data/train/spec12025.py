import numpy as np 

def function(x):

	i4 = 2
	b3 = 4
	paths = []
	try:
		if i4 >= 8:
			x = 4-x
			paths.append(1)
		else:
			x = 3/x
			b3 = 4/b3
			paths.append(2)
		if x < 8:
			i4 = b3*b3
			i4 = i4*i4
			paths.append(3)
		else:
			i4 = 8*i4
			i4 = x*8
			i4 = i4*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i4 = x**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))