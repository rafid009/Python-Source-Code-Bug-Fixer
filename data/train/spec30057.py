import numpy as np 

def function(x):

	t2 = x
	w8 = 3
	x = x
	paths = []
	try:
		if x > 3:
			t2 = t2+5
			w8 = w8*x
			t2 = t2-4
			paths.append(1)
		else:
			t2 = t2-5
			paths.append(2)
		if t2 >= 2:
			t2 = t2-w8
			x = x+t2
			t2 = t2+1
			paths.append(3)
		else:
			t2 = 7-t2
			w8 = w8+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))