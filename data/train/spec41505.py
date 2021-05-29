import numpy as np 

def function(x):

	j0 = 6
	r5 = x
	paths = []
	try:
		if j0 >= 4:
			j0 = j0*j0
			paths.append(1)
		else:
			x = x*6
			x = x*r5
			paths.append(2)
		if x <= 7:
			x = 1*9
			j0 = r5-x
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		r5 = j0**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))