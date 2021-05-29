import numpy as np 

def function(x):

	w7 = x
	i8 = 5
	paths = []
	try:
		if w7 >= 6:
			i8 = i8+2
			w7 = 6-i8
			i8 = i8*w7
			paths.append(1)
		else:
			i8 = w7*0
			paths.append(2)
		if i8 >= 3:
			i8 = i8-w7
			i8 = 5/i8
			w7 = w7+w7
			paths.append(3)
		else:
			w7 = 1-w7
			i8 = 2*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w7 = x**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))