import numpy as np 

def function(x):

	a3 = x
	e9 = 4
	paths = []
	try:
		if x > 5:
			e9 = x+x
			paths.append(1)
		else:
			a3 = a3-0
			a3 = a3-8
			e9 = e9*5
			paths.append(2)
		if x <= 4:
			a3 = a3/9
			x = 5*x
			paths.append(3)
		else:
			e9 = 7+a3
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		e9 = a3**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))