import numpy as np 

def function(x):

	k1 = x
	u4 = 5
	paths = []
	try:
		if x >= 9:
			x = x+k1
			k1 = 9+u4
			u4 = u4+k1
			paths.append(1)
		else:
			u4 = u4+4
			x = 0-k1
			paths.append(2)
		if k1 > 6:
			u4 = 8+k1
			paths.append(3)
		else:
			x = 8+5
			k1 = 4*k1
			u4 = u4*1
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