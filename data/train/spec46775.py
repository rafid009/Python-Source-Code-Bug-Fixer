import numpy as np 

def function(x):

	w4 = x
	i7 = x
	x = x
	paths = []
	try:
		if i7 > 4:
			i7 = i7/2
			x = 8/x
			x = x/8
			paths.append(1)
		else:
			x = 7+7
			x = 0-5
			paths.append(2)
		if i7 <= 5:
			i7 = w4+i7
			paths.append(3)
		else:
			i7 = i7-2
			i7 = i7/5
			w4 = w4*i7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))