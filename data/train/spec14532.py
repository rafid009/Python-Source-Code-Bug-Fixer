import numpy as np 

def function(x):

	i8 = x
	w6 = 7
	paths = []
	try:
		if i8 >= 0:
			x = 2+x
			w6 = 2*3
			x = 1/9
			paths.append(1)
		else:
			x = 2+x
			paths.append(2)
		if i8 < 8:
			x = x*w6
			x = 8*9
			paths.append(3)
		else:
			i8 = 5/i8
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