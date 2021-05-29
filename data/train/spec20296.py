import numpy as np 

def function(x):

	v3 = x
	a4 = 2
	paths = []
	try:
		if a4 < 4:
			x = 0/x
			a4 = x+v3
			paths.append(1)
		else:
			a4 = 0*5
			x = a4+3
			paths.append(2)
		if x > 9:
			a4 = 4-7
			paths.append(3)
		else:
			x = a4*0
			a4 = 8*a4
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