import numpy as np 

def function(x):

	u4 = 3
	w1 = x
	paths = []
	try:
		if u4 >= 9:
			w1 = 5/w1
			u4 = u4*w1
			u4 = x*u4
			paths.append(1)
		else:
			w1 = 9/w1
			paths.append(2)
		if x >= 3:
			w1 = 6+w1
			x = x*w1
			paths.append(3)
		else:
			w1 = w1+0
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