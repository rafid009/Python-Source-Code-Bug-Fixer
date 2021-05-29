import numpy as np 

def function(x):

	a3 = 6
	l5 = x
	x = x
	paths = []
	try:
		if a3 <= 0:
			x = 9+l5
			a3 = a3-l5
			x = l5+5
			paths.append(1)
		else:
			a3 = a3+x
			a3 = x*a3
			x = l5*9
			paths.append(2)
		if a3 <= 4:
			l5 = l5-4
			a3 = a3+l5
			paths.append(3)
		else:
			a3 = 4-x
			l5 = 3-l5
			l5 = l5-l5
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		a3 = a3**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))