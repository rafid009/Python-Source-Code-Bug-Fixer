import numpy as np 

def function(x):

	v5 = 7
	i7 = x
	x = 3
	paths = []
	try:
		if x >= 4:
			x = i7+5
			paths.append(1)
		else:
			x = 4*i7
			paths.append(2)
		if i7 >= 5:
			x = x-8
			i7 = i7-v5
			paths.append(3)
		else:
			v5 = i7/4
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