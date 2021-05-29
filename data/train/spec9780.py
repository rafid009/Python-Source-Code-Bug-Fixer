import numpy as np 

def function(x):

	i4 = 6
	d2 = x
	paths = []
	try:
		if d2 > 9:
			i4 = i4+8
			x = 9+x
			d2 = 0-d2
			paths.append(1)
		else:
			i4 = 1+i4
			paths.append(2)
		if i4 > 8:
			d2 = d2/x
			i4 = i4*9
			paths.append(3)
		else:
			x = 6-9
			x = x*5
			d2 = d2-i4
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