import numpy as np 

def function(x):

	q7 = 3
	k6 = 1
	paths = []
	try:
		if k6 <= 9:
			k6 = k6/6
			x = x/3
			paths.append(1)
		else:
			k6 = 3+3
			q7 = 1-6
			paths.append(2)
		if x <= 7:
			x = 9+x
			paths.append(3)
		else:
			q7 = 5-q7
			x = 8-7
			k6 = q7/k6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k6 = x**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))