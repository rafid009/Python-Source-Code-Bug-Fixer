import numpy as np 

def function(x):

	w6 = x
	f1 = x
	paths = []
	try:
		if f1 >= 5:
			f1 = w6-1
			w6 = 9*3
			paths.append(1)
		else:
			w6 = 3/8
			f1 = f1-w6
			w6 = 0-2
			paths.append(2)
		if x < 6:
			x = x+8
			f1 = f1-f1
			paths.append(3)
		else:
			w6 = 4+w6
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		w6 = w6**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))