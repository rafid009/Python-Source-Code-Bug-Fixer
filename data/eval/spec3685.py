import numpy as np 

def function(x):

	a0 = 0
	t2 = 6
	paths = []
	try:
		if x < 7:
			a0 = a0-7
			paths.append(1)
		else:
			x = t2/8
			x = x+6
			x = x*8
			paths.append(2)
		if t2 > 1:
			t2 = t2/3
			paths.append(3)
		else:
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		x = a0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))