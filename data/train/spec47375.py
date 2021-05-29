import numpy as np 

def function(x):

	i7 = x
	n5 = 8
	paths = []
	try:
		if n5 >= 6:
			n5 = n5*7
			i7 = i7-i7
			paths.append(1)
		else:
			x = x+7
			n5 = 0*x
			paths.append(2)
		if x < 9:
			i7 = 3-n5
			paths.append(3)
		else:
			i7 = i7-3
			n5 = n5+1
			i7 = n5-i7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i7 = x**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))