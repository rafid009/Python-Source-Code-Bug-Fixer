import numpy as np 

def function(x):

	n3 = 6
	v2 = x
	paths = []
	try:
		if n3 > 2:
			n3 = 6+9
			paths.append(1)
		else:
			n3 = n3-n3
			x = 8/5
			n3 = 4-x
			paths.append(2)
		if n3 >= 8:
			n3 = n3+3
			x = x+7
			v2 = 5/v2
			paths.append(3)
		else:
			x = 6-2
			n3 = 4*6
			x = 1*x
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