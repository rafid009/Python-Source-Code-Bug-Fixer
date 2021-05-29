import numpy as np 

def function(x):

	b5 = 8
	t2 = 7
	paths = []
	try:
		if t2 < 1:
			b5 = 5+b5
			paths.append(1)
		else:
			x = x/9
			paths.append(2)
		if b5 < 9:
			b5 = 4*7
			x = 7/x
			t2 = 9-b5
			paths.append(3)
		else:
			t2 = x/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b5 = x**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))