import numpy as np 

def function(x):

	k6 = 4
	x2 = x
	paths = []
	try:
		if x2 > 1:
			x2 = x2-2
			x = x-9
			paths.append(1)
		else:
			x = k6*k6
			x = 0/x2
			k6 = k6+k6
			paths.append(2)
		if x2 > 7:
			k6 = k6+1
			x = 7-x
			paths.append(3)
		else:
			k6 = 7-k6
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x2 = x2**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))