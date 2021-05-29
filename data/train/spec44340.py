import numpy as np 

def function(x):

	t9 = x
	w1 = x
	paths = []
	try:
		if t9 < 5:
			x = 6/x
			w1 = x-9
			x = 9-x
			paths.append(1)
		else:
			w1 = w1/w1
			t9 = t9-5
			paths.append(2)
		if t9 < 0:
			w1 = 4/w1
			x = x*5
			w1 = t9-2
			paths.append(3)
		else:
			x = x-3
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		t9 = w1**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))