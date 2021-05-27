import numpy as np 

def function(x):

	n4 = 5
	e6 = 6
	paths = []
	try:
		if e6 <= 4:
			e6 = x+e6
			x = n4/x
			paths.append(1)
		else:
			e6 = 5-e6
			e6 = e6+1
			paths.append(2)
		if n4 <= 8:
			x = 3*x
			e6 = e6-2
			paths.append(3)
		else:
			n4 = 6/n4
			e6 = 5*e6
			e6 = e6-6
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