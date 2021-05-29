import numpy as np 

def function(x):

	t2 = 3
	h7 = x
	paths = []
	try:
		if x <= 5:
			x = 0+5
			x = 9*0
			x = x-9
			paths.append(1)
		else:
			t2 = t2-t2
			x = 1/x
			paths.append(2)
		if h7 > 9:
			x = 7-x
			t2 = 8-x
			paths.append(3)
		else:
			t2 = h7+6
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