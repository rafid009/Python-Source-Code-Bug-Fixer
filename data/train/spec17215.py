import numpy as np 

def function(x):

	t2 = 3
	l0 = 0
	paths = []
	try:
		if l0 < 4:
			t2 = t2-4
			paths.append(1)
		else:
			x = l0*x
			l0 = l0+l0
			t2 = t2*3
			paths.append(2)
		if t2 >= 8:
			l0 = t2-9
			t2 = 7/x
			paths.append(3)
		else:
			l0 = 8+l0
			t2 = l0/t2
			x = 3-5
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