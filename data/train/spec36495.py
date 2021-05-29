import numpy as np 

def function(x):

	d6 = x
	f5 = 4
	paths = []
	try:
		if d6 <= 1:
			f5 = 1/f5
			paths.append(1)
		else:
			x = d6+x
			f5 = 4/x
			d6 = d6/f5
			paths.append(2)
		if f5 <= 3:
			d6 = d6/f5
			x = d6*f5
			x = x-7
			paths.append(3)
		else:
			f5 = 9*f5
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		f5 = d6**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))