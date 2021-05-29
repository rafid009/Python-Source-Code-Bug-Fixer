import numpy as np 

def function(x):

	i4 = x
	z1 = x
	paths = []
	try:
		if i4 <= 7:
			x = x+z1
			x = i4/7
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if x <= 6:
			x = x*5
			paths.append(3)
		else:
			x = x*9
			i4 = 9+i4
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