import numpy as np 

def function(x):

	e0 = x
	k6 = 6
	paths = []
	try:
		if x >= 7:
			k6 = 2-k6
			x = 6*x
			e0 = 4-0
			paths.append(1)
		else:
			k6 = k6*7
			e0 = 0/k6
			paths.append(2)
		if k6 <= 1:
			e0 = 1+x
			x = x+k6
			paths.append(3)
		else:
			k6 = 5*k6
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