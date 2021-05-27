import numpy as np 

def function(x):

	k6 = 0
	b9 = 3
	paths = []
	try:
		if x <= 2:
			b9 = b9*x
			paths.append(1)
		else:
			x = x-3
			b9 = k6/x
			paths.append(2)
		if x <= 1:
			b9 = x+b9
			x = k6+5
			b9 = b9/3
			paths.append(3)
		else:
			b9 = x+b9
			k6 = k6-2
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		k6 = k6**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))