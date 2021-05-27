import numpy as np 

def function(x):

	t9 = x
	t3 = x
	paths = []
	try:
		if x <= 9:
			x = x-5
			t3 = 0-t3
			paths.append(1)
		else:
			t3 = t3-4
			x = x+x
			paths.append(2)
		if t3 <= 8:
			t3 = 7*t3
			x = t3/x
			t3 = t3*3
			paths.append(3)
		else:
			x = 0-0
			t9 = t9+8
			x = x-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t3 = x**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))