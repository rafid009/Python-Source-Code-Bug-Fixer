import numpy as np 

def function(x):

	e7 = x
	k1 = 6
	paths = []
	try:
		if k1 <= 5:
			e7 = 7*e7
			paths.append(1)
		else:
			k1 = 2*k1
			k1 = 0+x
			e7 = e7+7
			paths.append(2)
		if x > 5:
			k1 = k1+e7
			paths.append(3)
		else:
			k1 = x/3
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