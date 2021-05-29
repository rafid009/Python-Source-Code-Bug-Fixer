import numpy as np 

def function(x):

	w7 = 5
	u1 = x
	paths = []
	try:
		if x >= 1:
			u1 = u1+w7
			u1 = u1-8
			paths.append(1)
		else:
			w7 = w7/7
			x = u1-9
			paths.append(2)
		if u1 >= 8:
			x = x*x
			paths.append(3)
		else:
			x = u1+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w7 = x**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))