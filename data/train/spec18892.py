import numpy as np 

def function(x):

	i6 = 3
	n4 = 4
	paths = []
	try:
		if n4 > 8:
			i6 = i6+i6
			i6 = i6*6
			n4 = 1*i6
			paths.append(1)
		else:
			n4 = 7-n4
			i6 = i6-6
			x = 7*x
			paths.append(2)
		if x <= 3:
			i6 = 9-1
			paths.append(3)
		else:
			x = 8*x
			n4 = 7/7
			n4 = n4*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))