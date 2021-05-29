import numpy as np 

def function(x):

	k6 = 5
	i5 = 0
	x = x
	paths = []
	try:
		if x < 1:
			i5 = i5-k6
			paths.append(1)
		else:
			x = i5+i5
			k6 = 3/7
			paths.append(2)
		if x > 4:
			k6 = 8/k6
			i5 = 4*i5
			paths.append(3)
		else:
			x = x+x
			k6 = 6/k6
			k6 = 9+k6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i5 = x**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))