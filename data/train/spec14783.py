import numpy as np 

def function(x):

	r6 = 1
	w3 = x
	paths = []
	try:
		if x <= 3:
			x = x/9
			paths.append(1)
		else:
			w3 = w3/5
			paths.append(2)
		if x >= 4:
			r6 = r6+5
			paths.append(3)
		else:
			w3 = 3*w3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r6 = x**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))