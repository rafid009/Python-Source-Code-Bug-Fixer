import numpy as np 

def function(x):

	t8 = 3
	l3 = 6
	paths = []
	try:
		if t8 < 4:
			t8 = t8-9
			t8 = 3*9
			paths.append(1)
		else:
			t8 = 3/t8
			t8 = l3/t8
			paths.append(2)
		if t8 < 6:
			t8 = t8*x
			l3 = 4-l3
			paths.append(3)
		else:
			t8 = t8+x
			l3 = 9*t8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l3 = x**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))