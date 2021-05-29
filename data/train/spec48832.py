import numpy as np 

def function(x):

	j0 = x
	o1 = x
	paths = []
	try:
		if j0 > 5:
			j0 = 8+2
			paths.append(1)
		else:
			o1 = j0*o1
			x = x/j0
			o1 = 7*9
			paths.append(2)
		if o1 <= 5:
			j0 = 1/j0
			paths.append(3)
		else:
			o1 = j0-9
			o1 = 6*j0
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		j0 = j0**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))