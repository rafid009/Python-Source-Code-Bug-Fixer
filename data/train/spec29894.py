import numpy as np 

def function(x):

	w5 = x
	t8 = x
	paths = []
	try:
		if t8 >= 0:
			x = 3+x
			t8 = 2+6
			paths.append(1)
		else:
			w5 = 4*w5
			paths.append(2)
		if t8 < 0:
			x = x/3
			paths.append(3)
		else:
			w5 = w5*4
			w5 = 4-w5
			x = 9+t8
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		x = w5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))