import numpy as np 

def function(x):

	o6 = 6
	l6 = x
	paths = []
	try:
		if o6 <= 9:
			l6 = 1*l6
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if o6 >= 5:
			l6 = l6-5
			l6 = l6+3
			paths.append(3)
		else:
			l6 = 0+l6
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		o6 = l6**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))