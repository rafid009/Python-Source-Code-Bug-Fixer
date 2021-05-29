import numpy as np 

def function(x):

	k6 = x
	y8 = x
	paths = []
	try:
		if k6 < 2:
			x = x+3
			paths.append(1)
		else:
			k6 = k6*k6
			x = x+4
			paths.append(2)
		if k6 < 4:
			y8 = 3+y8
			y8 = y8*2
			paths.append(3)
		else:
			k6 = k6/5
			y8 = 7+6
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		x = k6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))