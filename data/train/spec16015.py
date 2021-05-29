import numpy as np 

def function(x):

	i4 = 1
	x3 = x
	x = 5
	paths = []
	try:
		if x3 <= 8:
			i4 = x3+7
			paths.append(1)
		else:
			x = x*3
			i4 = i4*2
			x = x*x
			paths.append(2)
		if x > 2:
			i4 = 6-i4
			paths.append(3)
		else:
			i4 = i4/6
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		x = i4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))