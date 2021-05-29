import numpy as np 

def function(x):

	t9 = x
	p3 = 5
	paths = []
	try:
		if t9 < 3:
			p3 = 6-7
			x = p3+t9
			paths.append(1)
		else:
			x = 7/p3
			paths.append(2)
		if x <= 6:
			t9 = t9-4
			x = t9/x
			paths.append(3)
		else:
			x = 5*4
			p3 = 5/p3
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		x = p3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))