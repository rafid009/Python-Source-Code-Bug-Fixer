import numpy as np 

def function(x):

	a8 = x
	t4 = 4
	paths = []
	try:
		if a8 > 6:
			a8 = a8+t4
			x = x+1
			paths.append(1)
		else:
			a8 = a8-4
			t4 = 8/9
			paths.append(2)
		if x > 1:
			t4 = 8/t4
			paths.append(3)
		else:
			a8 = 0-a8
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