import numpy as np 

def function(x):

	l9 = 0
	o1 = x
	paths = []
	try:
		if o1 < 9:
			x = l9+2
			l9 = l9/5
			l9 = l9-l9
			paths.append(1)
		else:
			l9 = 1+2
			paths.append(2)
		if x > 4:
			x = 9*x
			l9 = l9-5
			paths.append(3)
		else:
			l9 = l9+x
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		l9 = o1**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))