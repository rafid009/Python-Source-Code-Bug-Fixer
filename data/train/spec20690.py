import numpy as np 

def function(x):

	v0 = 2
	q4 = 6
	paths = []
	try:
		if v0 < 5:
			x = x-0
			x = 5*x
			paths.append(1)
		else:
			v0 = x*v0
			q4 = x+1
			paths.append(2)
		if x >= 4:
			x = 4*x
			paths.append(3)
		else:
			q4 = v0/8
			x = q4+x
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