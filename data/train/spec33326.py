import numpy as np 

def function(x):

	f1 = 2
	w7 = 5
	paths = []
	try:
		if f1 >= 8:
			x = 3/9
			x = 9-2
			paths.append(1)
		else:
			w7 = w7-8
			paths.append(2)
		if w7 >= 3:
			f1 = f1/f1
			w7 = w7-4
			x = f1-x
			paths.append(3)
		else:
			w7 = w7-1
			w7 = 7-x
			x = f1*x
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		f1 = w7**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))