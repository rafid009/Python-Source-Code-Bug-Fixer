import numpy as np 

def function(x):

	t3 = 4
	b3 = 2
	paths = []
	try:
		if b3 <= 3:
			t3 = 6+t3
			b3 = b3-b3
			x = 6+x
			paths.append(1)
		else:
			b3 = b3/b3
			paths.append(2)
		if t3 <= 7:
			t3 = 3+t3
			b3 = 2+2
			paths.append(3)
		else:
			x = 9*x
			b3 = t3*b3
			b3 = b3+3
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