import numpy as np 

def function(x):

	k2 = 9
	u6 = 6
	paths = []
	try:
		if x > 0:
			x = x*7
			paths.append(1)
		else:
			u6 = u6-k2
			paths.append(2)
		if u6 >= 2:
			u6 = u6-4
			k2 = k2/9
			k2 = k2/4
			paths.append(3)
		else:
			k2 = k2-4
			x = u6-x
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		k2 = u6**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))