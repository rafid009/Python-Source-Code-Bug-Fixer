import numpy as np 

def function(x):

	t9 = x
	w6 = 8
	paths = []
	try:
		if t9 < 4:
			x = x+x
			w6 = 2-t9
			w6 = 7/w6
			paths.append(1)
		else:
			w6 = w6*1
			t9 = t9/3
			w6 = w6*w6
			paths.append(2)
		if w6 >= 6:
			t9 = t9+t9
			t9 = x/t9
			paths.append(3)
		else:
			t9 = t9-7
			w6 = 5-w6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w6 = x**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))