import numpy as np 

def function(x):

	w8 = 8
	t4 = 2
	paths = []
	try:
		if x <= 5:
			t4 = w8+t4
			paths.append(1)
		else:
			x = x*8
			t4 = 4-5
			paths.append(2)
		if w8 <= 1:
			w8 = t4-6
			t4 = w8/t4
			paths.append(3)
		else:
			w8 = t4-w8
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		w8 = t4**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))