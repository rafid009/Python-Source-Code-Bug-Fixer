import numpy as np 

def function(x):

	k1 = x
	v4 = x
	paths = []
	try:
		if v4 < 6:
			k1 = k1+v4
			k1 = k1*x
			paths.append(1)
		else:
			k1 = v4+3
			paths.append(2)
		if k1 <= 3:
			v4 = 0-v4
			x = x/x
			x = x/4
			paths.append(3)
		else:
			x = 7/v4
			x = x/v4
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		v4 = v4**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))