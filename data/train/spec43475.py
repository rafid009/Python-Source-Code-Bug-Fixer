import numpy as np 

def function(x):

	v5 = 7
	i8 = x
	paths = []
	try:
		if x < 3:
			v5 = v5+v5
			v5 = 1+v5
			paths.append(1)
		else:
			v5 = x+v5
			v5 = v5/2
			paths.append(2)
		if x > 8:
			x = 0+i8
			paths.append(3)
		else:
			x = v5/x
			x = i8/x
			v5 = 0-v5
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