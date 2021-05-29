import numpy as np 

def function(x):

	v2 = 1
	q8 = 4
	paths = []
	try:
		if q8 < 6:
			q8 = q8-v2
			paths.append(1)
		else:
			x = 0-x
			v2 = v2+3
			v2 = x/v2
			paths.append(2)
		if q8 > 2:
			v2 = v2-8
			q8 = v2-2
			q8 = 4-q8
			paths.append(3)
		else:
			v2 = 9*v2
			x = 8+x
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		x = v2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))