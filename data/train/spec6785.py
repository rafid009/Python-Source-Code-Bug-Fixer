import numpy as np 

def function(x):

	t9 = x
	b9 = 8
	paths = []
	try:
		if b9 >= 2:
			b9 = b9-b9
			x = 1+8
			b9 = b9+3
			paths.append(1)
		else:
			b9 = 8+x
			t9 = t9*x
			x = t9/x
			paths.append(2)
		if t9 > 4:
			t9 = 5/6
			paths.append(3)
		else:
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		x = t9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))