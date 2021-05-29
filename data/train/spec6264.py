import numpy as np 

def function(x):

	t2 = x
	a8 = x
	paths = []
	try:
		if x > 3:
			x = x/a8
			t2 = t2/a8
			paths.append(1)
		else:
			a8 = 7+a8
			x = 1-x
			paths.append(2)
		if a8 >= 1:
			t2 = t2/2
			a8 = a8*9
			a8 = t2+0
			paths.append(3)
		else:
			t2 = 4+t2
			a8 = 8/2
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