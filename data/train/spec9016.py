import numpy as np 

def function(x):

	v0 = x
	b4 = 9
	paths = []
	try:
		if b4 > 4:
			b4 = 5+6
			v0 = v0*9
			v0 = 6/v0
			paths.append(1)
		else:
			b4 = 3*1
			paths.append(2)
		if v0 >= 8:
			x = x+0
			paths.append(3)
		else:
			v0 = 4-0
			v0 = v0+v0
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