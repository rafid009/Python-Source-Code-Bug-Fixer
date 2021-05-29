import numpy as np 

def function(x):

	y0 = 5
	v2 = 0
	paths = []
	try:
		if x < 1:
			v2 = 1+7
			paths.append(1)
		else:
			y0 = x*y0
			v2 = 7-5
			v2 = x*y0
			paths.append(2)
		if x <= 4:
			v2 = x+v2
			paths.append(3)
		else:
			y0 = x/y0
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		v2 = v2**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))