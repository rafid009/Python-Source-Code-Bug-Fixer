import numpy as np 

def function(x):

	e1 = 7
	j9 = 0
	paths = []
	try:
		if j9 <= 7:
			e1 = 3-e1
			x = x/e1
			paths.append(1)
		else:
			x = x-4
			paths.append(2)
		if e1 <= 1:
			j9 = 3+9
			e1 = 6+e1
			e1 = x+e1
			paths.append(3)
		else:
			x = x*8
			x = x-e1
			e1 = e1/e1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j9 = x**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))