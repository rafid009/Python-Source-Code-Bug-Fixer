import numpy as np 

def function(x):

	e8 = x
	n6 = x
	paths = []
	try:
		if n6 <= 6:
			x = 0*3
			e8 = x-1
			paths.append(1)
		else:
			e8 = e8-n6
			paths.append(2)
		if e8 < 4:
			n6 = 6+n6
			x = x*1
			paths.append(3)
		else:
			x = x+x
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		e8 = n6**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))