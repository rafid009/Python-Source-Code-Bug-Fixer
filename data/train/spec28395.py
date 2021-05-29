import numpy as np 

def function(x):

	y2 = x
	v7 = x
	paths = []
	try:
		if x <= 0:
			x = x/8
			x = y2-1
			paths.append(1)
		else:
			v7 = 1*v7
			paths.append(2)
		if y2 < 4:
			v7 = 3+v7
			paths.append(3)
		else:
			y2 = x/2
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		v7 = y2**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))