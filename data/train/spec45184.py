import numpy as np 

def function(x):

	q8 = x
	i8 = x
	paths = []
	try:
		if q8 < 6:
			x = 2*8
			q8 = 1+q8
			q8 = q8*2
			paths.append(1)
		else:
			i8 = i8-0
			i8 = 6*i8
			paths.append(2)
		if x < 3:
			q8 = 0-q8
			i8 = 6-i8
			i8 = 3*i8
			paths.append(3)
		else:
			i8 = i8/3
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