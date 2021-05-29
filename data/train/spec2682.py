import numpy as np 

def function(x):

	k1 = 5
	h7 = 7
	paths = []
	try:
		if k1 <= 5:
			x = 4*x
			paths.append(1)
		else:
			x = x/7
			x = k1*x
			k1 = 6+x
			paths.append(2)
		if x > 4:
			k1 = k1/x
			x = k1+x
			x = x-1
			paths.append(3)
		else:
			h7 = x*x
			k1 = k1-0
			k1 = 6+k1
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