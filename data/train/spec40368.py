import numpy as np 

def function(x):

	e8 = x
	i1 = x
	paths = []
	try:
		if e8 < 6:
			i1 = i1*e8
			x = e8-x
			i1 = i1-3
			paths.append(1)
		else:
			x = 8-e8
			paths.append(2)
		if i1 <= 3:
			x = x*8
			x = 8/7
			i1 = e8-i1
			paths.append(3)
		else:
			e8 = e8+i1
			x = x-3
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		e8 = e8**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))