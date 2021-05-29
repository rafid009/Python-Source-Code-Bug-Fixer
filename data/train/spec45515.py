import numpy as np 

def function(x):

	w1 = x
	t9 = 5
	paths = []
	try:
		if t9 <= 3:
			x = x+x
			t9 = 1/x
			w1 = t9/4
			paths.append(1)
		else:
			t9 = 4+t9
			paths.append(2)
		if w1 >= 7:
			w1 = w1+4
			x = 2+x
			paths.append(3)
		else:
			t9 = 6-8
			w1 = w1*w1
			t9 = 8/t9
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