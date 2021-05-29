import numpy as np 

def function(x):

	d0 = 5
	i4 = 4
	x = x
	paths = []
	try:
		if x > 3:
			d0 = 8+0
			x = 6/x
			paths.append(1)
		else:
			d0 = 7*d0
			d0 = d0*d0
			i4 = 6-i4
			paths.append(2)
		if x <= 4:
			d0 = 5+6
			d0 = d0-6
			paths.append(3)
		else:
			x = x-d0
			i4 = x+1
			i4 = i4/2
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