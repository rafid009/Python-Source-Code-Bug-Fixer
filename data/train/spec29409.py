import numpy as np 

def function(x):

	i0 = 3
	x5 = 9
	paths = []
	try:
		if x > 6:
			i0 = i0-x
			paths.append(1)
		else:
			x = i0/x
			i0 = 3+9
			x = x5+x5
			paths.append(2)
		if i0 <= 3:
			x = x+2
			x = x/4
			x5 = 8-0
			paths.append(3)
		else:
			i0 = i0*x
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		x5 = i0**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))