import numpy as np 

def function(x):

	u6 = x
	i9 = 5
	paths = []
	try:
		if x >= 7:
			i9 = 8+i9
			paths.append(1)
		else:
			u6 = u6*2
			u6 = x-u6
			i9 = i9*u6
			paths.append(2)
		if i9 >= 5:
			x = 2-x
			i9 = u6*i9
			paths.append(3)
		else:
			i9 = 4-4
			u6 = i9+u6
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		x = u6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))