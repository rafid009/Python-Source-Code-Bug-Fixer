import numpy as np 

def function(x):

	k1 = x
	a3 = 2
	paths = []
	try:
		if a3 >= 4:
			x = a3+x
			a3 = a3+4
			k1 = k1/k1
			paths.append(1)
		else:
			x = a3+x
			k1 = k1-4
			paths.append(2)
		if x <= 5:
			x = 5-x
			paths.append(3)
		else:
			k1 = k1-a3
			k1 = k1-5
			x = x-k1
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