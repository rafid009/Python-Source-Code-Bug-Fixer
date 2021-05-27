import numpy as np 

def function(x):

	v7 = 5
	d9 = x
	paths = []
	try:
		if v7 > 9:
			d9 = d9/6
			x = 0+3
			paths.append(1)
		else:
			d9 = x+9
			paths.append(2)
		if x > 8:
			x = 0/v7
			d9 = d9*8
			paths.append(3)
		else:
			x = 3+x
			d9 = v7*d9
			d9 = d9/v7
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