import numpy as np 

def function(x):

	b4 = 1
	t1 = x
	paths = []
	try:
		if x >= 8:
			t1 = 1-b4
			b4 = b4/1
			b4 = t1-9
			paths.append(1)
		else:
			t1 = 0/7
			paths.append(2)
		if t1 <= 1:
			x = 0-x
			b4 = 8-x
			b4 = b4+2
			paths.append(3)
		else:
			b4 = b4-4
			b4 = x/b4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b4 = x**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))