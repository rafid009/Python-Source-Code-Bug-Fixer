import numpy as np 

def function(x):

	f1 = x
	d9 = x
	paths = []
	try:
		if d9 >= 8:
			x = 5+x
			paths.append(1)
		else:
			f1 = 2-1
			f1 = 2+f1
			d9 = d9+0
			paths.append(2)
		if x >= 1:
			x = d9/6
			d9 = 7+4
			x = d9/1
			paths.append(3)
		else:
			x = 9*d9
			f1 = x/7
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		x = d9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))