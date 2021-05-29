import numpy as np 

def function(x):

	t9 = x
	f1 = 3
	paths = []
	try:
		if f1 <= 3:
			t9 = 9*t9
			f1 = 5+x
			paths.append(1)
		else:
			t9 = t9/3
			paths.append(2)
		if t9 > 2:
			t9 = t9+f1
			paths.append(3)
		else:
			t9 = x-t9
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