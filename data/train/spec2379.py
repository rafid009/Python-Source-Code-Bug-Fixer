import numpy as np 

def function(x):

	d6 = x
	f6 = 1
	paths = []
	try:
		if d6 <= 2:
			f6 = f6+8
			paths.append(1)
		else:
			x = 8*6
			paths.append(2)
		if f6 <= 1:
			f6 = 5-7
			d6 = d6*d6
			x = 5/d6
			paths.append(3)
		else:
			f6 = x+9
			d6 = 7*d6
			x = d6+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))