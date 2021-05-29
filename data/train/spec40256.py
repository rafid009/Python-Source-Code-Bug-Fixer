import numpy as np 

def function(x):

	w9 = x
	v0 = x
	paths = []
	try:
		if w9 < 2:
			w9 = w9*0
			x = x-8
			paths.append(1)
		else:
			x = 3*v0
			x = 0+x
			w9 = 8*4
			paths.append(2)
		if v0 >= 3:
			x = 2-x
			x = 8/x
			paths.append(3)
		else:
			x = x/2
			v0 = 6-v0
			v0 = v0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w9 = x**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))