import numpy as np 

def function(x):

	a9 = 1
	k6 = x
	paths = []
	try:
		if k6 > 2:
			k6 = k6*6
			paths.append(1)
		else:
			a9 = x*9
			x = a9-7
			paths.append(2)
		if k6 < 1:
			x = 2/9
			paths.append(3)
		else:
			k6 = k6+9
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		a9 = k6**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))