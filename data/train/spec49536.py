import numpy as np 

def function(x):

	d5 = 7
	k1 = x
	paths = []
	try:
		if k1 >= 4:
			d5 = 0+7
			paths.append(1)
		else:
			x = 7+2
			paths.append(2)
		if x < 6:
			x = 6+7
			d5 = d5/4
			d5 = d5/3
			paths.append(3)
		else:
			k1 = k1+k1
			k1 = 9/k1
			x = 3-d5
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