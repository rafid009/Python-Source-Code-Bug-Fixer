import numpy as np 

def function(x):

	t8 = x
	t6 = x
	paths = []
	try:
		if t8 < 5:
			t8 = 0-t8
			t8 = 5*x
			paths.append(1)
		else:
			x = 3+x
			x = 9-6
			paths.append(2)
		if t6 > 5:
			t8 = 2+t6
			t8 = t8-1
			paths.append(3)
		else:
			x = t6*x
			x = x+t6
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