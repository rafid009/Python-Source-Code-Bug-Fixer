import numpy as np 

def function(x):

	t2 = 6
	w4 = 5
	paths = []
	try:
		if t2 >= 9:
			w4 = w4/w4
			paths.append(1)
		else:
			t2 = t2/1
			t2 = w4-6
			paths.append(2)
		if x <= 9:
			x = t2/7
			paths.append(3)
		else:
			t2 = 5+3
			t2 = t2*t2
			x = 4-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t2 = x**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))