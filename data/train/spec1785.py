import numpy as np 

def function(x):

	v4 = 5
	j0 = x
	paths = []
	try:
		if j0 <= 2:
			x = x*2
			v4 = v4+v4
			paths.append(1)
		else:
			x = x-x
			x = x-9
			paths.append(2)
		if j0 > 0:
			x = x/5
			j0 = j0/x
			paths.append(3)
		else:
			j0 = x*j0
			j0 = j0*0
			j0 = j0+1
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