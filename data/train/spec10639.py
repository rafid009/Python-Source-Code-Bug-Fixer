import numpy as np 

def function(x):

	j7 = x
	x5 = 4
	paths = []
	try:
		if j7 >= 0:
			x = x+6
			x = x*8
			j7 = j7+j7
			paths.append(1)
		else:
			x = x*1
			x5 = x+2
			paths.append(2)
		if x5 > 3:
			x = 4*9
			paths.append(3)
		else:
			j7 = x5/j7
			x = x5*x
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x5 = x5**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))