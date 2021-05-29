import numpy as np 

def function(x):

	j5 = 5
	e0 = 4
	paths = []
	try:
		if x < 9:
			e0 = e0*9
			j5 = 6/j5
			x = x*x
			paths.append(1)
		else:
			x = x+7
			paths.append(2)
		if e0 >= 8:
			e0 = j5*1
			x = 8-x
			paths.append(3)
		else:
			j5 = j5-6
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		x = j5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))