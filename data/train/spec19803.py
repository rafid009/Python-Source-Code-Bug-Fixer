import numpy as np 

def function(x):

	l6 = x
	o5 = 0
	x = x
	paths = []
	try:
		if x <= 9:
			l6 = 2/5
			l6 = 9*0
			l6 = l6*0
			paths.append(1)
		else:
			x = 8+2
			o5 = 9-l6
			l6 = 3+l6
			paths.append(2)
		if x > 9:
			o5 = l6+0
			o5 = 2+l6
			paths.append(3)
		else:
			l6 = 1*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l6 = x**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))