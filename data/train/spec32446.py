import numpy as np 

def function(x):

	t7 = 4
	w4 = 0
	paths = []
	try:
		if x >= 7:
			w4 = w4-x
			paths.append(1)
		else:
			w4 = 5*4
			w4 = 8+w4
			t7 = 3/1
			paths.append(2)
		if w4 > 9:
			t7 = 0+4
			paths.append(3)
		else:
			t7 = 4+6
			t7 = x+5
			t7 = 2-w4
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		x = w4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))