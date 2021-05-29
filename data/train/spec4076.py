import numpy as np 

def function(x):

	i6 = 3
	e6 = 6
	paths = []
	try:
		if e6 < 8:
			e6 = x*e6
			e6 = e6/x
			i6 = 9*0
			paths.append(1)
		else:
			i6 = 6-e6
			paths.append(2)
		if i6 <= 2:
			x = 7/x
			e6 = 7-e6
			e6 = i6-e6
			paths.append(3)
		else:
			i6 = 8-x
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