import numpy as np 

def function(x):

	x5 = x
	k6 = 2
	paths = []
	try:
		if k6 <= 6:
			k6 = k6+1
			x5 = 3+4
			k6 = k6+6
			paths.append(1)
		else:
			k6 = k6-x5
			k6 = k6+6
			x5 = x5*7
			paths.append(2)
		if x5 > 4:
			x5 = 5/k6
			paths.append(3)
		else:
			x5 = x5+k6
			x = 2+x
			x = k6+2
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