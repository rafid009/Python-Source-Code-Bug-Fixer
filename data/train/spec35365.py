import numpy as np 

def function(x):

	j7 = 0
	e8 = 1
	paths = []
	try:
		if e8 > 7:
			x = x+1
			e8 = e8+1
			paths.append(1)
		else:
			e8 = j7-2
			paths.append(2)
		if x > 3:
			x = x/x
			paths.append(3)
		else:
			x = 1+j7
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		x = e8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))