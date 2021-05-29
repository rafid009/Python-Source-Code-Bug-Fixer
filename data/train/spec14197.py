import numpy as np 

def function(x):

	k6 = 9
	i5 = x
	paths = []
	try:
		if x <= 0:
			k6 = 4-k6
			paths.append(1)
		else:
			k6 = k6/x
			i5 = 2*x
			paths.append(2)
		if k6 > 6:
			k6 = k6*4
			paths.append(3)
		else:
			i5 = 7/i5
			i5 = i5+i5
			x = x/x
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		x = i5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))