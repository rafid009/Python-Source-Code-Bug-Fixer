import numpy as np 

def function(x):

	j7 = 7
	k1 = x
	paths = []
	try:
		if j7 >= 9:
			x = k1/x
			j7 = 9+j7
			x = x/3
			paths.append(1)
		else:
			x = 0-x
			paths.append(2)
		if k1 > 3:
			k1 = 0*2
			k1 = j7+8
			paths.append(3)
		else:
			x = 5+k1
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