import numpy as np 

def function(x):

	j7 = 6
	e1 = 7
	paths = []
	try:
		if x < 1:
			x = 3*2
			paths.append(1)
		else:
			e1 = e1/6
			x = 5/e1
			e1 = e1*j7
			paths.append(2)
		if x < 1:
			x = 2-e1
			j7 = 5*j7
			paths.append(3)
		else:
			e1 = 2-e1
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		x = e1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))