import numpy as np 

def function(x):

	a5 = 7
	l5 = x
	paths = []
	try:
		if l5 <= 4:
			x = x+x
			a5 = 8-6
			paths.append(1)
		else:
			a5 = a5/x
			l5 = l5*0
			paths.append(2)
		if l5 > 1:
			l5 = 8+a5
			l5 = l5+a5
			x = x*x
			paths.append(3)
		else:
			x = 5-x
			l5 = 6-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a5 = x**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))