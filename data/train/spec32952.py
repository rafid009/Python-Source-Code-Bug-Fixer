import numpy as np 

def function(x):

	r3 = 2
	a0 = x
	paths = []
	try:
		if a0 > 7:
			r3 = r3+0
			a0 = a0+0
			paths.append(1)
		else:
			r3 = 0/r3
			paths.append(2)
		if x <= 7:
			r3 = 0-0
			x = 8+x
			paths.append(3)
		else:
			r3 = 4+r3
			r3 = r3-3
			a0 = 5-x
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