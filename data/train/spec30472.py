import numpy as np 

def function(x):

	w7 = x
	t7 = x
	paths = []
	try:
		if w7 > 3:
			w7 = w7-7
			paths.append(1)
		else:
			x = t7+2
			x = 4*t7
			paths.append(2)
		if t7 >= 9:
			w7 = 1/w7
			x = 1/8
			t7 = t7*t7
			paths.append(3)
		else:
			x = w7-t7
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		w7 = t7**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))