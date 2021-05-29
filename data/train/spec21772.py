import numpy as np 

def function(x):

	p8 = 9
	f3 = x
	paths = []
	try:
		if f3 > 2:
			p8 = p8*f3
			paths.append(1)
		else:
			x = 0/x
			paths.append(2)
		if f3 > 7:
			f3 = f3-7
			paths.append(3)
		else:
			x = x+4
			f3 = f3+6
			x = x+3
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		x = f3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))