import numpy as np 

def function(x):

	j6 = 5
	j4 = x
	paths = []
	try:
		if x < 9:
			j6 = j6*8
			x = x-1
			x = 9+2
			paths.append(1)
		else:
			x = 8*x
			j6 = 2+j4
			j6 = x-0
			paths.append(2)
		if j4 <= 4:
			x = 0-j6
			x = x-9
			paths.append(3)
		else:
			j6 = x/4
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