import numpy as np 

def function(x):

	w8 = x
	r4 = 2
	x = 0
	paths = []
	try:
		if r4 <= 3:
			r4 = r4/w8
			paths.append(1)
		else:
			x = x-w8
			x = 5/x
			paths.append(2)
		if r4 >= 4:
			w8 = x-w8
			w8 = w8-2
			paths.append(3)
		else:
			x = x*r4
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		w8 = w8**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))