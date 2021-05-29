import numpy as np 

def function(x):

	l1 = x
	t8 = 6
	paths = []
	try:
		if t8 < 0:
			x = x*5
			x = l1/9
			x = 2+x
			paths.append(1)
		else:
			t8 = t8-t8
			paths.append(2)
		if t8 > 4:
			l1 = l1*x
			paths.append(3)
		else:
			t8 = t8*8
			l1 = l1-l1
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