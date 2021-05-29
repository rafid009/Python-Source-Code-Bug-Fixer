import numpy as np 

def function(x):

	b7 = 0
	t3 = 6
	paths = []
	try:
		if b7 > 1:
			b7 = t3*b7
			paths.append(1)
		else:
			t3 = 3-3
			t3 = 9*2
			t3 = x*t3
			paths.append(2)
		if b7 < 4:
			b7 = b7+9
			b7 = 1/b7
			t3 = 9/x
			paths.append(3)
		else:
			b7 = b7*5
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