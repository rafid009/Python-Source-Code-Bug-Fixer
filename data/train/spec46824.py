import numpy as np 

def function(x):

	r6 = 9
	w8 = x
	paths = []
	try:
		if w8 >= 5:
			r6 = x/x
			r6 = 0-r6
			paths.append(1)
		else:
			w8 = w8/x
			paths.append(2)
		if r6 <= 0:
			r6 = r6*8
			paths.append(3)
		else:
			x = 0*r6
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		w8 = r6**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))