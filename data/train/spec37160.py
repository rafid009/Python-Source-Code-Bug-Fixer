import numpy as np 

def function(x):

	j5 = x
	l4 = 5
	paths = []
	try:
		if x >= 5:
			x = x*9
			x = 2-x
			j5 = j5/7
			paths.append(1)
		else:
			l4 = l4+4
			paths.append(2)
		if l4 <= 3:
			x = j5/x
			l4 = 9*l4
			l4 = 0*l4
			paths.append(3)
		else:
			x = l4/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j5 = x**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))