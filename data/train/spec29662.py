import numpy as np 

def function(x):

	j4 = x
	e2 = x
	paths = []
	try:
		if x <= 1:
			x = j4-7
			e2 = 2*j4
			paths.append(1)
		else:
			x = x*3
			j4 = j4+6
			e2 = j4+x
			paths.append(2)
		if e2 >= 8:
			x = x+6
			e2 = 7*j4
			paths.append(3)
		else:
			e2 = x-4
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		j4 = e2**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))