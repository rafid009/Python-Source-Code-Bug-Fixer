import numpy as np 

def function(x):

	a5 = x
	l1 = 3
	paths = []
	try:
		if l1 < 4:
			l1 = 4+5
			paths.append(1)
		else:
			x = x*4
			paths.append(2)
		if x < 3:
			a5 = 0-4
			paths.append(3)
		else:
			l1 = l1/l1
			x = 8+6
			a5 = 3+x
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		a5 = a5**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))