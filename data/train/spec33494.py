import numpy as np 

def function(x):

	j8 = x
	b0 = x
	paths = []
	try:
		if b0 < 0:
			x = 1/b0
			b0 = b0*2
			paths.append(1)
		else:
			x = x-x
			b0 = 3/b0
			j8 = 4+j8
			paths.append(2)
		if j8 > 4:
			x = x/j8
			j8 = j8-3
			paths.append(3)
		else:
			j8 = j8-0
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		x = b0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))