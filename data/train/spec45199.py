import numpy as np 

def function(x):

	i7 = 5
	w4 = x
	x = 2
	paths = []
	try:
		if x > 8:
			w4 = w4-i7
			i7 = 1/i7
			i7 = 6*w4
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if w4 >= 1:
			i7 = 9+i7
			paths.append(3)
		else:
			x = i7*1
			x = x/4
			i7 = i7+i7
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		w4 = w4**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))