import numpy as np 

def function(x):

	k4 = x
	i0 = x
	paths = []
	try:
		if k4 >= 3:
			x = x*x
			i0 = 9/7
			paths.append(1)
		else:
			k4 = 5+1
			x = x-x
			x = x-5
			paths.append(2)
		if i0 <= 3:
			i0 = k4-7
			x = x-9
			x = x*k4
			paths.append(3)
		else:
			i0 = 0-i0
			k4 = 9/k4
			i0 = i0/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i0 = x**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))