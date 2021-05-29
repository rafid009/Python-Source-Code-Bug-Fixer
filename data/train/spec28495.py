import numpy as np 

def function(x):

	l4 = x
	e5 = 0
	paths = []
	try:
		if e5 > 5:
			x = x/7
			x = x+7
			paths.append(1)
		else:
			l4 = 1-4
			e5 = e5-x
			e5 = e5-5
			paths.append(2)
		if l4 <= 8:
			x = x+6
			l4 = x+x
			x = 5*x
			paths.append(3)
		else:
			e5 = 3-1
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		x = e5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))