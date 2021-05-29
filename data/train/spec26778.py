import numpy as np 

def function(x):

	d2 = x
	d9 = 6
	x = 4
	paths = []
	try:
		if d2 > 3:
			x = x+x
			d2 = x/8
			d9 = d9-4
			paths.append(1)
		else:
			d9 = d9*0
			x = 3/3
			d9 = d9*7
			paths.append(2)
		if x >= 8:
			d9 = d9/d9
			x = 7+2
			paths.append(3)
		else:
			d9 = d9-7
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