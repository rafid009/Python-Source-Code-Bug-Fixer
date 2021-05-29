import numpy as np 

def function(x):

	u3 = x
	w4 = 5
	paths = []
	try:
		if w4 > 1:
			u3 = 4+5
			x = 3/x
			paths.append(1)
		else:
			w4 = u3*w4
			paths.append(2)
		if u3 < 7:
			u3 = u3/x
			u3 = u3+5
			paths.append(3)
		else:
			w4 = x*w4
			w4 = x-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w4 = x**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))