import numpy as np 

def function(x):

	v0 = x
	e0 = 6
	paths = []
	try:
		if e0 <= 1:
			e0 = e0/6
			v0 = 4+v0
			x = x/x
			paths.append(1)
		else:
			v0 = 9*0
			v0 = v0/9
			paths.append(2)
		if e0 <= 6:
			v0 = v0/6
			x = x*6
			paths.append(3)
		else:
			e0 = x+1
			e0 = v0*e0
			e0 = e0-v0
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