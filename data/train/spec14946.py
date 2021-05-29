import numpy as np 

def function(x):

	r5 = x
	a4 = x
	paths = []
	try:
		if a4 < 3:
			x = 3*r5
			paths.append(1)
		else:
			a4 = a4+1
			paths.append(2)
		if r5 < 6:
			x = x+a4
			x = 6+x
			r5 = r5-3
			paths.append(3)
		else:
			r5 = 4/r5
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		x = a4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))