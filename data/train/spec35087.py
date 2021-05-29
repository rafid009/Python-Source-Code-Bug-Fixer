import numpy as np 

def function(x):

	w7 = 1
	t7 = x
	paths = []
	try:
		if x > 0:
			t7 = t7*5
			w7 = w7+w7
			t7 = 0-9
			paths.append(1)
		else:
			t7 = t7*8
			w7 = w7/8
			paths.append(2)
		if t7 > 3:
			x = 3/x
			w7 = x*4
			paths.append(3)
		else:
			w7 = t7/w7
			x = 1-w7
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