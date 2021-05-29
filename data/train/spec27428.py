import numpy as np 

def function(x):

	t2 = x
	p8 = x
	paths = []
	try:
		if x >= 2:
			t2 = t2-7
			paths.append(1)
		else:
			t2 = 2-1
			p8 = p8/t2
			p8 = p8+5
			paths.append(2)
		if t2 >= 5:
			t2 = 9+p8
			p8 = p8*t2
			paths.append(3)
		else:
			p8 = 5+p8
			t2 = p8/t2
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