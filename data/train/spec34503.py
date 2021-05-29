import numpy as np 

def function(x):

	b2 = x
	f2 = x
	paths = []
	try:
		if x < 9:
			f2 = x-3
			paths.append(1)
		else:
			b2 = b2-b2
			b2 = b2/x
			x = 3-x
			paths.append(2)
		if f2 > 6:
			x = 5-5
			b2 = b2*x
			paths.append(3)
		else:
			x = 5*x
			x = x-x
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		x = f2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))