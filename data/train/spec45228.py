import numpy as np 

def function(x):

	k1 = x
	n5 = x
	paths = []
	try:
		if k1 < 2:
			n5 = k1*n5
			k1 = 0+x
			paths.append(1)
		else:
			x = k1*x
			x = 5-x
			k1 = 4/k1
			paths.append(2)
		if n5 >= 5:
			x = x*6
			x = x/k1
			x = n5-x
			paths.append(3)
		else:
			n5 = 0/9
			k1 = 7+9
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