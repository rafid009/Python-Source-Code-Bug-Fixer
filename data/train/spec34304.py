import numpy as np 

def function(x):

	l8 = x
	t9 = x
	paths = []
	try:
		if l8 >= 6:
			t9 = t9-t9
			paths.append(1)
		else:
			x = t9/8
			x = x*l8
			l8 = l8+2
			paths.append(2)
		if x < 5:
			t9 = t9/x
			paths.append(3)
		else:
			l8 = 6-l8
			l8 = 2*l8
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