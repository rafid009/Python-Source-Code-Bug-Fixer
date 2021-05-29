import numpy as np 

def function(x):

	r6 = x
	w0 = 4
	paths = []
	try:
		if w0 > 9:
			w0 = 5*w0
			r6 = 4+r6
			paths.append(1)
		else:
			w0 = 5+4
			paths.append(2)
		if r6 < 6:
			x = 9-x
			paths.append(3)
		else:
			x = 1+x
			w0 = r6+9
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		w0 = r6**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))