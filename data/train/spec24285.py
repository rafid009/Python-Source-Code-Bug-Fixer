import numpy as np 

def function(x):

	b0 = x
	t8 = x
	paths = []
	try:
		if b0 > 8:
			b0 = x/b0
			t8 = t8*b0
			b0 = 9*b0
			paths.append(1)
		else:
			x = 4+x
			b0 = t8/2
			paths.append(2)
		if t8 > 0:
			x = 9-7
			paths.append(3)
		else:
			x = t8/9
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		x = b0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))