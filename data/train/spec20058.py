import numpy as np 

def function(x):

	r7 = x
	w4 = x
	paths = []
	try:
		if x <= 5:
			r7 = r7*3
			r7 = w4-6
			paths.append(1)
		else:
			r7 = 9+3
			paths.append(2)
		if r7 > 5:
			r7 = r7-6
			x = x-x
			x = x*r7
			paths.append(3)
		else:
			w4 = w4-4
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		r7 = w4**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))