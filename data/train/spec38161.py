import numpy as np 

def function(x):

	k1 = 5
	u6 = x
	paths = []
	try:
		if k1 >= 7:
			k1 = 9-8
			x = x*k1
			paths.append(1)
		else:
			k1 = 4-k1
			u6 = u6*6
			k1 = 4/k1
			paths.append(2)
		if x <= 6:
			k1 = x*5
			paths.append(3)
		else:
			x = 8/x
			x = x-x
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		k1 = k1**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))