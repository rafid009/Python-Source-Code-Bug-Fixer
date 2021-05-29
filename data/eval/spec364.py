import numpy as np 

def function(x):

	f8 = 0
	w6 = x
	paths = []
	try:
		if f8 <= 6:
			f8 = 7/w6
			w6 = w6*6
			x = x+w6
			paths.append(1)
		else:
			f8 = 6-f8
			f8 = f8+w6
			f8 = f8-1
			paths.append(2)
		if w6 < 2:
			f8 = f8/9
			f8 = w6/f8
			paths.append(3)
		else:
			f8 = 4-2
			w6 = 6+f8
			w6 = 5*w6
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