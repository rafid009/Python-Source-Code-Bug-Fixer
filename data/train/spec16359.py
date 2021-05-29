import numpy as np 

def function(x):

	r7 = 2
	e3 = x
	paths = []
	try:
		if x <= 7:
			e3 = 1-9
			paths.append(1)
		else:
			e3 = e3/4
			e3 = e3/2
			paths.append(2)
		if r7 <= 6:
			r7 = 4+r7
			paths.append(3)
		else:
			r7 = 2-r7
			e3 = 5+r7
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		x = e3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))