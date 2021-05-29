import numpy as np 

def function(x):

	l0 = 2
	j9 = 1
	paths = []
	try:
		if l0 < 3:
			j9 = 6*x
			paths.append(1)
		else:
			l0 = l0*2
			x = 6/7
			l0 = 3-l0
			paths.append(2)
		if l0 <= 3:
			l0 = 3-l0
			l0 = 2*4
			paths.append(3)
		else:
			x = 7*5
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j9 = x**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))