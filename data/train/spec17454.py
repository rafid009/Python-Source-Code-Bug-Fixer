import numpy as np 

def function(x):

	a3 = x
	t3 = 5
	paths = []
	try:
		if x >= 0:
			t3 = t3*t3
			a3 = 2*t3
			x = 8+x
			paths.append(1)
		else:
			t3 = x-t3
			paths.append(2)
		if x < 5:
			x = 3+x
			paths.append(3)
		else:
			t3 = t3/t3
			t3 = x-x
			a3 = 7+a3
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