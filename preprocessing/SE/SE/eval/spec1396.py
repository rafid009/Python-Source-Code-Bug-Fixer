import numpy as np 

def function(x):

	l1 = 1
	e3 = x
	paths = []
	try:
		if l1 >= 0:
			x = 5-x
			l1 = l1/1
			paths.append(1)
		else:
			e3 = 0/e3
			paths.append(2)
		if x < 4:
			x = 6/x
			l1 = l1+l1
			x = e3/x
			paths.append(3)
		else:
			l1 = l1*2
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