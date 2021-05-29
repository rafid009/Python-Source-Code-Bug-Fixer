import numpy as np 

def function(x):

	d9 = 1
	i8 = x
	x = x
	paths = []
	try:
		if x < 9:
			d9 = d9+0
			i8 = 8-i8
			d9 = 1+d9
			paths.append(1)
		else:
			x = i8*8
			paths.append(2)
		if d9 > 5:
			d9 = d9/i8
			d9 = d9+i8
			i8 = i8/x
			paths.append(3)
		else:
			x = 3*x
			d9 = x+d9
			d9 = 1-x
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		d9 = d9**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))