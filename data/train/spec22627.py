import numpy as np 

def function(x):

	t9 = 0
	f2 = 1
	x = 3
	paths = []
	try:
		if t9 > 8:
			x = 8/f2
			t9 = t9+2
			paths.append(1)
		else:
			f2 = f2-x
			paths.append(2)
		if t9 < 5:
			x = x-9
			paths.append(3)
		else:
			t9 = 7*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t9 = x**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))