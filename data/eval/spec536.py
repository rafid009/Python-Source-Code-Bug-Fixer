import numpy as np 

def function(x):

	v3 = x
	d1 = 4
	x = 3
	paths = []
	try:
		if d1 > 9:
			x = 8-x
			paths.append(1)
		else:
			d1 = d1-1
			paths.append(2)
		if x > 8:
			v3 = v3+x
			paths.append(3)
		else:
			d1 = 3*v3
			v3 = v3/1
			d1 = d1/v3
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		x = v3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))