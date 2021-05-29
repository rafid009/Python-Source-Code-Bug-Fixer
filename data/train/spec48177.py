import numpy as np 

def function(x):

	h8 = x
	j0 = x
	paths = []
	try:
		if x < 4:
			x = 5+x
			j0 = j0*9
			paths.append(1)
		else:
			x = 5/x
			x = x/9
			paths.append(2)
		if j0 < 7:
			x = 7+h8
			j0 = x-j0
			x = j0-8
			paths.append(3)
		else:
			j0 = j0-8
			j0 = j0-1
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