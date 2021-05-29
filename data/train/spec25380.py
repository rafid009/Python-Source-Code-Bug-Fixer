import numpy as np 

def function(x):

	b6 = x
	j5 = 0
	x = 1
	paths = []
	try:
		if x >= 8:
			j5 = b6*3
			x = x*x
			x = j5+x
			paths.append(1)
		else:
			x = x+2
			x = 3*b6
			x = 5+x
			paths.append(2)
		if j5 >= 8:
			j5 = 0*b6
			b6 = 6*b6
			x = 9-x
			paths.append(3)
		else:
			b6 = b6-0
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		j5 = b6**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))