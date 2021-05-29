import numpy as np 

def function(x):

	f7 = 5
	i4 = 6
	paths = []
	try:
		if i4 >= 9:
			f7 = 1/f7
			x = x+8
			paths.append(1)
		else:
			i4 = 0/x
			paths.append(2)
		if x <= 0:
			f7 = i4*5
			x = x*3
			f7 = f7+i4
			paths.append(3)
		else:
			x = x-3
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