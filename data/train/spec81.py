import numpy as np 

def function(x):

	r1 = x
	w4 = 5
	paths = []
	try:
		if x < 5:
			x = x*1
			w4 = 9*r1
			paths.append(1)
		else:
			r1 = r1*9
			x = w4/x
			paths.append(2)
		if x <= 0:
			r1 = r1*3
			w4 = x+w4
			r1 = 3/r1
			paths.append(3)
		else:
			x = x-1
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