import numpy as np 

def function(x):

	a0 = 1
	s4 = x
	paths = []
	try:
		if x <= 8:
			x = x/5
			paths.append(1)
		else:
			x = x/3
			a0 = a0+0
			paths.append(2)
		if x > 5:
			a0 = 0-a0
			paths.append(3)
		else:
			x = x*8
			x = 5/x
			x = 3+x
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