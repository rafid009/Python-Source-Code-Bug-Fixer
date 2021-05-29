import numpy as np 

def function(x):

	d0 = 6
	f3 = x
	paths = []
	try:
		if x > 6:
			d0 = 4/d0
			paths.append(1)
		else:
			f3 = f3-5
			paths.append(2)
		if d0 <= 4:
			x = 7*x
			paths.append(3)
		else:
			d0 = d0+d0
			x = 3-x
			d0 = d0*d0
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