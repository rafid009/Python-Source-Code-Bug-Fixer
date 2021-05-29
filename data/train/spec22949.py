import numpy as np 

def function(x):

	l5 = x
	j8 = 6
	paths = []
	try:
		if j8 > 8:
			l5 = l5*9
			paths.append(1)
		else:
			l5 = 6-l5
			paths.append(2)
		if l5 >= 0:
			l5 = j8/4
			paths.append(3)
		else:
			j8 = 6*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j8 = x**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))