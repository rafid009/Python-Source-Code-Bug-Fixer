import numpy as np 

def function(x):

	i4 = x
	k4 = 4
	paths = []
	try:
		if k4 <= 1:
			x = 3-k4
			paths.append(1)
		else:
			i4 = i4/6
			x = 2+x
			k4 = 2+7
			paths.append(2)
		if x <= 8:
			k4 = i4+k4
			paths.append(3)
		else:
			k4 = k4/4
			x = k4-x
			i4 = i4+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k4 = x**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))