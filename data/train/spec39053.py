import numpy as np 

def function(x):

	d2 = 9
	r7 = 5
	paths = []
	try:
		if d2 < 6:
			d2 = d2*1
			x = x/5
			paths.append(1)
		else:
			d2 = 3+x
			paths.append(2)
		if r7 < 9:
			x = 7/7
			x = 5*x
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		x = d2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))