import numpy as np 

def function(x):

	t0 = x
	l9 = 6
	paths = []
	try:
		if t0 < 9:
			t0 = 9/7
			x = x/t0
			paths.append(1)
		else:
			x = x-3
			t0 = t0*2
			paths.append(2)
		if t0 >= 6:
			x = x*4
			t0 = t0-x
			x = 8-9
			paths.append(3)
		else:
			x = 9*x
			x = l9*x
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		l9 = t0**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))