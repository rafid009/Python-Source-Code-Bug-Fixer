import numpy as np 

def function(x):

	i8 = 9
	f8 = x
	paths = []
	try:
		if x > 0:
			x = x-6
			i8 = i8*4
			paths.append(1)
		else:
			x = x/x
			x = 2*4
			x = x/1
			paths.append(2)
		if i8 >= 9:
			i8 = x+f8
			paths.append(3)
		else:
			i8 = 5+3
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		x = i8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))