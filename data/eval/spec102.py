import numpy as np 

def function(x):

	t4 = x
	o9 = 1
	paths = []
	try:
		if x <= 2:
			t4 = 7*t4
			x = o9-x
			paths.append(1)
		else:
			t4 = 9-o9
			t4 = 9*4
			paths.append(2)
		if o9 > 0:
			o9 = o9+5
			x = 3-o9
			paths.append(3)
		else:
			x = x/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t4 = x**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))