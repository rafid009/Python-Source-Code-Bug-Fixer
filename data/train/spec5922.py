import numpy as np 

def function(x):

	i6 = x
	f8 = x
	paths = []
	try:
		if f8 < 5:
			f8 = 6+2
			paths.append(1)
		else:
			x = 8-7
			paths.append(2)
		if f8 >= 8:
			i6 = x+0
			x = x/2
			f8 = 2-f8
			paths.append(3)
		else:
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		x = i6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))