import numpy as np 

def function(x):

	t0 = 0
	b5 = x
	paths = []
	try:
		if x > 6:
			t0 = x+2
			paths.append(1)
		else:
			b5 = b5-b5
			paths.append(2)
		if t0 > 4:
			x = b5-x
			b5 = t0/b5
			paths.append(3)
		else:
			x = x+4
			t0 = 2+t0
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