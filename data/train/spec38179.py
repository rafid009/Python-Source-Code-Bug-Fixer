import numpy as np 

def function(x):

	d9 = x
	w8 = x
	paths = []
	try:
		if d9 <= 6:
			w8 = w8+7
			d9 = d9*9
			paths.append(1)
		else:
			d9 = w8-x
			d9 = 0+2
			x = x+d9
			paths.append(2)
		if x < 6:
			x = 5/x
			paths.append(3)
		else:
			d9 = 4+d9
			d9 = x/x
			w8 = w8*9
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