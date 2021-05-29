import numpy as np 

def function(x):

	i4 = x
	d4 = x
	x = x
	paths = []
	try:
		if x <= 9:
			x = i4+7
			paths.append(1)
		else:
			x = 8-5
			d4 = d4+x
			paths.append(2)
		if i4 < 6:
			d4 = i4+2
			paths.append(3)
		else:
			i4 = i4+1
			x = 1/x
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		x = d4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))