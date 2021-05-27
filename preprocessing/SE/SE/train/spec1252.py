import numpy as np 

def function(x):

	l9 = 9
	t5 = x
	paths = []
	try:
		if x < 6:
			t5 = 1/2
			l9 = 1/9
			t5 = t5/t5
			paths.append(1)
		else:
			l9 = 4+l9
			t5 = 5/t5
			paths.append(2)
		if x < 0:
			t5 = x/6
			x = 8+x
			paths.append(3)
		else:
			l9 = l9+6
			l9 = l9*x
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