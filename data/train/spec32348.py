import numpy as np 

def function(x):

	x0 = x
	i0 = x
	paths = []
	try:
		if x <= 7:
			x = 4*i0
			paths.append(1)
		else:
			x = i0+x
			x = x-x0
			x = 6/8
			paths.append(2)
		if x0 < 8:
			x = 8+x
			paths.append(3)
		else:
			i0 = 2*0
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		x0 = i0**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))