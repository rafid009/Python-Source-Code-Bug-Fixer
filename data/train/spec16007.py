import numpy as np 

def function(x):

	i1 = 8
	k6 = 4
	paths = []
	try:
		if i1 >= 1:
			i1 = 8-i1
			k6 = k6*k6
			paths.append(1)
		else:
			k6 = x/k6
			i1 = i1/4
			paths.append(2)
		if i1 > 6:
			i1 = i1+4
			i1 = i1-6
			x = i1*4
			paths.append(3)
		else:
			i1 = 9/k6
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