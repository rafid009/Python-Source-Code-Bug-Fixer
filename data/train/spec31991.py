import numpy as np 

def function(x):

	i4 = 2
	k6 = 1
	paths = []
	try:
		if k6 <= 5:
			i4 = i4+1
			x = 1*x
			i4 = 6/2
			paths.append(1)
		else:
			k6 = 6-i4
			i4 = 6-i4
			x = x/6
			paths.append(2)
		if k6 > 5:
			x = 5+x
			k6 = 9-k6
			paths.append(3)
		else:
			k6 = k6+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k6 = x**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))