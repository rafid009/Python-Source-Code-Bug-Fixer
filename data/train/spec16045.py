import numpy as np 

def function(x):

	w6 = 5
	i7 = 0
	paths = []
	try:
		if w6 >= 7:
			w6 = w6/7
			paths.append(1)
		else:
			i7 = w6*1
			i7 = x*4
			i7 = 1-i7
			paths.append(2)
		if x >= 1:
			i7 = i7-x
			i7 = 2/i7
			paths.append(3)
		else:
			w6 = 3*w6
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