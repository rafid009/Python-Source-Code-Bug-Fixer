import numpy as np 

def function(x):

	w9 = x
	w4 = 5
	paths = []
	try:
		if w9 >= 7:
			w9 = w9/6
			x = 9*0
			paths.append(1)
		else:
			w4 = x-w4
			w4 = w4-x
			paths.append(2)
		if x >= 6:
			x = x/9
			w4 = w4+0
			paths.append(3)
		else:
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		w4 = w9**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))