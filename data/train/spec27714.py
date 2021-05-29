import numpy as np 

def function(x):

	e2 = x
	n8 = 1
	paths = []
	try:
		if n8 <= 0:
			e2 = e2-3
			n8 = 4+9
			paths.append(1)
		else:
			n8 = n8/9
			x = 3+n8
			n8 = e2+n8
			paths.append(2)
		if x > 9:
			x = 2+7
			e2 = 7/e2
			paths.append(3)
		else:
			e2 = e2-5
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		e2 = e2**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))