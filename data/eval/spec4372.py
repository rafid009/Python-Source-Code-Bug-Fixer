import numpy as np 

def function(x):

	o7 = 2
	l6 = 6
	x = 6
	paths = []
	try:
		if o7 <= 4:
			o7 = 2-7
			x = 9*x
			l6 = x*8
			paths.append(1)
		else:
			o7 = o7-l6
			l6 = l6/9
			o7 = 6+4
			paths.append(2)
		if o7 <= 5:
			x = x*5
			x = o7*l6
			paths.append(3)
		else:
			l6 = x-l6
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		l6 = o7**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))