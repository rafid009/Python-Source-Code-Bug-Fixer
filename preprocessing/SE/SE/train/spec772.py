import numpy as np 

def function(x):

	o2 = 7
	a3 = x
	x = 3
	paths = []
	try:
		if a3 <= 2:
			a3 = a3-7
			x = a3+4
			paths.append(1)
		else:
			o2 = o2*2
			x = 8*x
			paths.append(2)
		if o2 >= 4:
			a3 = 4-a3
			o2 = 9-o2
			x = 4*a3
			paths.append(3)
		else:
			x = 6/x
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		x = a3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))