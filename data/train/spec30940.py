import numpy as np 

def function(x):

	t2 = x
	i8 = x
	paths = []
	try:
		if i8 >= 4:
			t2 = 3+x
			t2 = 7-t2
			x = x/2
			paths.append(1)
		else:
			x = t2/x
			i8 = t2*7
			paths.append(2)
		if t2 < 7:
			t2 = 3*t2
			x = x/t2
			x = x-2
			paths.append(3)
		else:
			t2 = t2/i8
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