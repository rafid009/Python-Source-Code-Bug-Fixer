import numpy as np 

def function(x):

	i0 = x
	e7 = 9
	x = 4
	paths = []
	try:
		if x > 7:
			x = x/3
			paths.append(1)
		else:
			i0 = e7*i0
			paths.append(2)
		if e7 <= 4:
			e7 = e7-9
			x = x/9
			x = 3+e7
			paths.append(3)
		else:
			e7 = e7-x
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		e7 = i0**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))