import numpy as np 

def function(x):

	t9 = 2
	a0 = 2
	paths = []
	try:
		if a0 < 0:
			x = a0+x
			paths.append(1)
		else:
			a0 = a0*7
			paths.append(2)
		if a0 >= 5:
			a0 = t9*6
			t9 = x*3
			paths.append(3)
		else:
			t9 = 9/t9
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