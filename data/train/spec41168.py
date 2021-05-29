import numpy as np 

def function(x):

	e6 = 8
	a6 = x
	paths = []
	try:
		if a6 >= 1:
			e6 = x/e6
			x = 7-2
			e6 = e6-6
			paths.append(1)
		else:
			x = 6*e6
			e6 = a6+7
			e6 = 9-e6
			paths.append(2)
		if a6 >= 1:
			a6 = a6-9
			e6 = x*2
			e6 = 1+1
			paths.append(3)
		else:
			e6 = 6*e6
			x = a6/5
			x = x/x
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		e6 = a6**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))