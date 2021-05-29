import numpy as np 

def function(x):

	v0 = x
	q0 = 2
	paths = []
	try:
		if v0 >= 4:
			x = 5*x
			q0 = 4-x
			q0 = q0+1
			paths.append(1)
		else:
			q0 = q0+0
			x = 1+0
			v0 = 2+v0
			paths.append(2)
		if x <= 3:
			x = x-4
			q0 = 0+8
			v0 = 0+1
			paths.append(3)
		else:
			x = 5-x
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