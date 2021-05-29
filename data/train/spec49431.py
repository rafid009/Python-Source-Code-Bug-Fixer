import numpy as np 

def function(x):

	t0 = x
	w6 = x
	paths = []
	try:
		if w6 >= 6:
			w6 = w6/9
			x = x*1
			paths.append(1)
		else:
			x = x*3
			t0 = 1-9
			paths.append(2)
		if x <= 5:
			t0 = t0+t0
			t0 = 1-2
			paths.append(3)
		else:
			t0 = 9/7
			t0 = 0-2
			t0 = 5-t0
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		w6 = t0**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))