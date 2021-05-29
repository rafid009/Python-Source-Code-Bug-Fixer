import numpy as np 

def function(x):

	d5 = x
	v0 = 7
	paths = []
	try:
		if v0 < 5:
			x = x*d5
			v0 = v0*2
			v0 = d5-v0
			paths.append(1)
		else:
			v0 = v0-5
			paths.append(2)
		if x > 8:
			v0 = v0+6
			paths.append(3)
		else:
			d5 = 8+d5
			v0 = 0*v0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))