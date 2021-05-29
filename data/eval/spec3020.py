import numpy as np 

def function(x):

	a1 = x
	t9 = x
	paths = []
	try:
		if t9 < 9:
			t9 = 0+t9
			paths.append(1)
		else:
			x = x/t9
			t9 = t9-3
			paths.append(2)
		if x >= 3:
			t9 = t9*8
			paths.append(3)
		else:
			a1 = a1-5
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