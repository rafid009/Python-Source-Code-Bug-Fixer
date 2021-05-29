import numpy as np 

def function(x):

	k6 = 8
	i6 = x
	paths = []
	try:
		if x < 1:
			i6 = 3+k6
			k6 = 9+0
			paths.append(1)
		else:
			i6 = i6/k6
			x = 1+x
			paths.append(2)
		if x >= 4:
			x = 5+x
			paths.append(3)
		else:
			k6 = 3+k6
			x = x-k6
			i6 = k6/i6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))