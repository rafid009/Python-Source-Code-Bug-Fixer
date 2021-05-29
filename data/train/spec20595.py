import numpy as np 

def function(x):

	a6 = x
	j5 = x
	paths = []
	try:
		if j5 >= 0:
			x = a6*x
			j5 = j5/8
			paths.append(1)
		else:
			a6 = 2-7
			a6 = a6+x
			paths.append(2)
		if a6 <= 0:
			a6 = x/3
			x = x+4
			paths.append(3)
		else:
			j5 = j5+j5
			x = 6-0
			j5 = 3*j5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j5 = x**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))