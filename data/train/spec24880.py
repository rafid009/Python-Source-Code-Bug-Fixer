import numpy as np 

def function(x):

	l3 = x
	a7 = 4
	x = x
	paths = []
	try:
		if l3 > 0:
			a7 = 3*9
			paths.append(1)
		else:
			a7 = a7/a7
			a7 = 0/x
			a7 = l3*a7
			paths.append(2)
		if x <= 5:
			a7 = a7*6
			l3 = l3+9
			paths.append(3)
		else:
			l3 = 0-l3
			a7 = a7+4
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		a7 = l3**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))