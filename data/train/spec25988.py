import numpy as np 

def function(x):

	w7 = x
	f2 = 8
	paths = []
	try:
		if x < 0:
			x = x+0
			x = x*4
			f2 = w7/x
			paths.append(1)
		else:
			x = 0/6
			paths.append(2)
		if x <= 1:
			f2 = f2+3
			f2 = f2-x
			w7 = w7-3
			paths.append(3)
		else:
			w7 = x-2
			f2 = f2*w7
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		w7 = w7**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))