import numpy as np 

def function(x):

	e1 = x
	a2 = 8
	paths = []
	try:
		if e1 <= 7:
			a2 = 9*1
			e1 = 6/e1
			paths.append(1)
		else:
			x = a2-5
			x = 0-x
			a2 = a2+a2
			paths.append(2)
		if x < 4:
			x = 7/e1
			paths.append(3)
		else:
			a2 = a2+a2
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		x = e1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))