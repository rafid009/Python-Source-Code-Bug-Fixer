import numpy as np 

def function(x):

	v2 = x
	n4 = x
	paths = []
	try:
		if v2 > 9:
			n4 = n4-7
			paths.append(1)
		else:
			x = 4+7
			n4 = 7/n4
			v2 = n4/v2
			paths.append(2)
		if n4 < 1:
			v2 = 8+n4
			paths.append(3)
		else:
			x = 2*n4
			v2 = 2/6
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