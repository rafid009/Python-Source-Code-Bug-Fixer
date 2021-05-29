import numpy as np 

def function(x):

	v7 = 7
	e3 = x
	paths = []
	try:
		if x > 9:
			e3 = e3-6
			paths.append(1)
		else:
			x = v7*x
			paths.append(2)
		if v7 < 5:
			x = x+9
			paths.append(3)
		else:
			e3 = 5-9
			x = x/3
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		e3 = e3**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))