import numpy as np 

def function(x):

	v9 = x
	d2 = 4
	paths = []
	try:
		if d2 > 9:
			x = 5/x
			x = 3+8
			paths.append(1)
		else:
			x = 3+1
			d2 = d2/7
			paths.append(2)
		if x >= 5:
			x = x+x
			v9 = d2-v9
			x = 0+v9
			paths.append(3)
		else:
			x = x-8
			d2 = d2/9
			d2 = 7-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v9 = x**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))