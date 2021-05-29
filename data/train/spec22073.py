import numpy as np 

def function(x):

	t9 = x
	p8 = 8
	paths = []
	try:
		if t9 >= 6:
			t9 = 1+x
			paths.append(1)
		else:
			p8 = x-8
			t9 = t9/9
			t9 = t9*t9
			paths.append(2)
		if p8 < 3:
			p8 = t9/p8
			paths.append(3)
		else:
			x = 5*p8
			t9 = t9-x
			x = 5-t9
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		x = p8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))