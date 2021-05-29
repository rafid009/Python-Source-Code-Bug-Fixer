import numpy as np 

def function(x):

	t0 = x
	b8 = 3
	paths = []
	try:
		if b8 > 7:
			x = 0*0
			b8 = b8-b8
			paths.append(1)
		else:
			x = 1+x
			b8 = 7/b8
			paths.append(2)
		if x <= 5:
			t0 = t0-9
			paths.append(3)
		else:
			b8 = 9-b8
			b8 = b8+5
			b8 = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))