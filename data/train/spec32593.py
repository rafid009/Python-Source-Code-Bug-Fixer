import numpy as np 

def function(x):

	w1 = 6
	o6 = 4
	paths = []
	try:
		if x <= 2:
			x = 7-o6
			o6 = w1+x
			paths.append(1)
		else:
			o6 = o6-7
			o6 = 1-x
			w1 = w1-w1
			paths.append(2)
		if w1 >= 3:
			w1 = w1/4
			w1 = w1/8
			o6 = 0-6
			paths.append(3)
		else:
			w1 = 2-w1
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		x = o6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))