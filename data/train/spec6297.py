import numpy as np 

def function(x):

	w5 = x
	k5 = 0
	x = 7
	paths = []
	try:
		if w5 <= 4:
			w5 = w5/8
			paths.append(1)
		else:
			x = 3-x
			w5 = 5*w5
			paths.append(2)
		if x > 2:
			w5 = 2+w5
			paths.append(3)
		else:
			w5 = w5*w5
			k5 = k5-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k5 = x**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))