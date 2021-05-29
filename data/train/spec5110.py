import numpy as np 

def function(x):

	j6 = x
	e6 = 0
	paths = []
	try:
		if x > 2:
			e6 = j6+e6
			paths.append(1)
		else:
			e6 = 7-e6
			x = x/3
			j6 = 1*7
			paths.append(2)
		if x >= 7:
			e6 = 3-e6
			paths.append(3)
		else:
			j6 = 0/4
			x = x+3
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		e6 = e6**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))