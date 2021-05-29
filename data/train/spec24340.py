import numpy as np 

def function(x):

	i4 = 8
	d4 = x
	x = x
	paths = []
	try:
		if i4 <= 5:
			d4 = 0+d4
			paths.append(1)
		else:
			x = 6-x
			i4 = i4-d4
			i4 = i4-9
			paths.append(2)
		if x >= 7:
			i4 = i4/x
			paths.append(3)
		else:
			x = 2+2
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		x = i4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))