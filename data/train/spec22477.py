import numpy as np 

def function(x):

	v4 = x
	q8 = 7
	paths = []
	try:
		if v4 <= 9:
			q8 = q8+v4
			paths.append(1)
		else:
			x = 9+3
			paths.append(2)
		if q8 >= 8:
			v4 = 3*v4
			paths.append(3)
		else:
			v4 = v4/1
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		v4 = v4**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))