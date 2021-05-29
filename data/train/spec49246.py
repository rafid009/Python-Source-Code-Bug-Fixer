import numpy as np 

def function(x):

	w6 = 8
	f7 = 8
	paths = []
	try:
		if w6 >= 6:
			f7 = f7*3
			w6 = f7-8
			paths.append(1)
		else:
			x = 9+w6
			w6 = w6+w6
			w6 = w6/6
			paths.append(2)
		if f7 < 7:
			f7 = 3*x
			w6 = 1-w6
			w6 = 1*w6
			paths.append(3)
		else:
			f7 = 8+1
			f7 = x-4
			w6 = w6-6
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