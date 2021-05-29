import numpy as np 

def function(x):

	w8 = 9
	r6 = x
	paths = []
	try:
		if r6 > 4:
			w8 = w8/2
			r6 = 4-r6
			r6 = x-x
			paths.append(1)
		else:
			w8 = x-w8
			x = 3*x
			paths.append(2)
		if r6 <= 9:
			r6 = 0-r6
			paths.append(3)
		else:
			x = x+2
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		x = r6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))