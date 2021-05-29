import numpy as np 

def function(x):

	a4 = x
	e6 = x
	paths = []
	try:
		if e6 < 6:
			a4 = x+9
			e6 = 1/e6
			paths.append(1)
		else:
			e6 = e6/a4
			e6 = 7+e6
			paths.append(2)
		if x <= 7:
			e6 = x-4
			a4 = a4+x
			paths.append(3)
		else:
			e6 = e6+1
			a4 = e6-2
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