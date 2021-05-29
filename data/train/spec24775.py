import numpy as np 

def function(x):

	d9 = 7
	v0 = x
	paths = []
	try:
		if v0 >= 5:
			x = x*v0
			paths.append(1)
		else:
			x = x*7
			v0 = v0/4
			paths.append(2)
		if x < 8:
			d9 = d9*3
			paths.append(3)
		else:
			d9 = v0-d9
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		v0 = d9**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))