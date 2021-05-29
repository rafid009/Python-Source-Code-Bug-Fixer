import numpy as np 

def function(x):

	d0 = 8
	i0 = x
	paths = []
	try:
		if i0 > 5:
			d0 = d0*x
			x = d0-d0
			d0 = i0/9
			paths.append(1)
		else:
			i0 = i0*5
			paths.append(2)
		if d0 < 2:
			x = 4*x
			i0 = i0*7
			i0 = 7/i0
			paths.append(3)
		else:
			i0 = 1*i0
			x = x-1
			d0 = d0+7
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