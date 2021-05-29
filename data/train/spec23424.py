import numpy as np 

def function(x):

	k1 = 7
	t3 = 6
	paths = []
	try:
		if k1 > 1:
			x = 6+x
			x = t3/t3
			k1 = k1/8
			paths.append(1)
		else:
			k1 = 6/k1
			k1 = 2+0
			paths.append(2)
		if k1 > 6:
			k1 = k1*3
			paths.append(3)
		else:
			x = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t3 = x**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))