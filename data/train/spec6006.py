import numpy as np 

def function(x):

	f0 = 5
	i4 = 1
	paths = []
	try:
		if x > 0:
			x = x/f0
			x = x-4
			paths.append(1)
		else:
			f0 = 8-f0
			x = x/3
			f0 = i4-f0
			paths.append(2)
		if f0 >= 9:
			x = i4/f0
			i4 = i4-x
			i4 = 2-i4
			paths.append(3)
		else:
			i4 = 9+x
			f0 = 6+5
			i4 = 8*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))