import numpy as np 

def function(x):

	t6 = 1
	l0 = x
	paths = []
	try:
		if l0 <= 4:
			l0 = x*6
			l0 = l0-5
			l0 = t6-l0
			paths.append(1)
		else:
			x = l0/t6
			x = 3/x
			t6 = 8-t6
			paths.append(2)
		if t6 >= 1:
			t6 = t6+1
			x = l0/x
			paths.append(3)
		else:
			x = 5-l0
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