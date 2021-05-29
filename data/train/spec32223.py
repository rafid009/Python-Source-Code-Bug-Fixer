import numpy as np 

def function(x):

	f2 = 8
	w6 = 9
	paths = []
	try:
		if w6 >= 9:
			w6 = w6-0
			w6 = 8-w6
			f2 = 9-0
			paths.append(1)
		else:
			w6 = f2+w6
			x = 1-6
			w6 = 5/w6
			paths.append(2)
		if w6 > 3:
			x = 7*7
			paths.append(3)
		else:
			w6 = w6/8
			f2 = f2*6
			w6 = 6/x
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