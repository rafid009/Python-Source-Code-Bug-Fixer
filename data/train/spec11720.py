import numpy as np 

def function(x):

	t8 = 5
	f5 = 4
	paths = []
	try:
		if t8 <= 8:
			t8 = t8+2
			t8 = 3+t8
			paths.append(1)
		else:
			x = t8/x
			f5 = f5/x
			t8 = 7-2
			paths.append(2)
		if f5 <= 8:
			f5 = f5/4
			paths.append(3)
		else:
			f5 = f5*x
			t8 = t8+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t8 = x**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))