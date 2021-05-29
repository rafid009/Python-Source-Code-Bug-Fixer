import numpy as np 

def function(x):

	f4 = 5
	k1 = 9
	paths = []
	try:
		if x > 3:
			k1 = k1-4
			paths.append(1)
		else:
			x = x-6
			k1 = k1*0
			paths.append(2)
		if x >= 2:
			k1 = 8/k1
			paths.append(3)
		else:
			f4 = f4+9
			k1 = k1/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k1 = x**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))