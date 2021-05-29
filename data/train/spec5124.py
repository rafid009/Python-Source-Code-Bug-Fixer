import numpy as np 

def function(x):

	t2 = 4
	b6 = 6
	paths = []
	try:
		if b6 < 3:
			t2 = t2*7
			x = x+3
			x = x+x
			paths.append(1)
		else:
			t2 = t2-b6
			t2 = t2-6
			paths.append(2)
		if b6 > 1:
			x = 9+x
			b6 = b6+4
			x = 8+x
			paths.append(3)
		else:
			b6 = b6+t2
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