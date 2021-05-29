import numpy as np 

def function(x):

	e1 = 0
	v6 = x
	paths = []
	try:
		if x > 9:
			e1 = 6-7
			paths.append(1)
		else:
			e1 = 5+e1
			x = x-0
			paths.append(2)
		if x <= 1:
			x = x-4
			x = x+3
			e1 = v6+e1
			paths.append(3)
		else:
			v6 = v6-1
			x = 7*5
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		e1 = v6**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))