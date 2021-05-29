import numpy as np 

def function(x):

	u3 = 6
	w5 = 8
	paths = []
	try:
		if x > 7:
			w5 = 3/6
			x = w5+5
			x = 9/w5
			paths.append(1)
		else:
			x = x-2
			paths.append(2)
		if w5 < 1:
			u3 = u3-u3
			w5 = w5*x
			paths.append(3)
		else:
			w5 = w5*4
			x = x-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u3 = x**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))