import numpy as np 

def function(x):

	x1 = x
	j4 = 4
	paths = []
	try:
		if x1 <= 0:
			j4 = j4+8
			x1 = x1+x1
			x = x-0
			paths.append(1)
		else:
			x = 2*x
			x = x1+5
			paths.append(2)
		if x1 < 6:
			j4 = 6*8
			x = x-j4
			paths.append(3)
		else:
			j4 = x/8
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x = x1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))