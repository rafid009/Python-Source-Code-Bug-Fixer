import numpy as np 

def function(x):

	v0 = 9
	o7 = x
	paths = []
	try:
		if x > 4:
			x = v0*x
			x = v0*5
			paths.append(1)
		else:
			x = x+6
			x = 7+x
			paths.append(2)
		if v0 > 0:
			v0 = 1+1
			paths.append(3)
		else:
			x = 0+v0
			o7 = 6+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))