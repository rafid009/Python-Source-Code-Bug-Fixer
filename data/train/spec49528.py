import numpy as np 

def function(x):

	s9 = 7
	t1 = x
	x = 7
	paths = []
	try:
		if t1 <= 8:
			t1 = 7+t1
			x = 9-x
			paths.append(1)
		else:
			t1 = t1-t1
			x = x*3
			x = 2-9
			paths.append(2)
		if x >= 9:
			x = 3-s9
			paths.append(3)
		else:
			t1 = t1+7
			t1 = 0+t1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))