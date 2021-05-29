import numpy as np 

def function(x):

	i8 = x
	v6 = 3
	paths = []
	try:
		if x <= 3:
			i8 = 0+i8
			i8 = i8+i8
			paths.append(1)
		else:
			i8 = 0+7
			x = 4+x
			v6 = v6+v6
			paths.append(2)
		if x < 8:
			x = 9+x
			i8 = 0/v6
			paths.append(3)
		else:
			x = 6-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v6 = x**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))