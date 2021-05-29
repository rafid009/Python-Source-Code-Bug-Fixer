import numpy as np 

def function(x):

	v5 = 2
	e3 = x
	paths = []
	try:
		if v5 < 6:
			v5 = v5-7
			x = 1-9
			paths.append(1)
		else:
			e3 = v5+4
			paths.append(2)
		if x < 7:
			e3 = e3+1
			paths.append(3)
		else:
			e3 = e3/x
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		e3 = v5**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))