import numpy as np 

def function(x):

	j8 = 0
	k1 = x
	paths = []
	try:
		if j8 > 4:
			x = x-j8
			k1 = k1*k1
			j8 = j8+2
			paths.append(1)
		else:
			j8 = j8-j8
			j8 = j8-0
			x = x+8
			paths.append(2)
		if j8 < 2:
			j8 = j8*2
			k1 = k1+0
			k1 = 9+2
			paths.append(3)
		else:
			x = 1-x
			x = 9-j8
			k1 = 3-k1
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