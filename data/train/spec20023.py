import numpy as np 

def function(x):

	o6 = x
	l5 = 6
	paths = []
	try:
		if o6 >= 9:
			o6 = o6-x
			x = x/8
			paths.append(1)
		else:
			x = x*l5
			x = l5*x
			x = x-0
			paths.append(2)
		if x >= 7:
			x = 7+0
			l5 = 3-o6
			paths.append(3)
		else:
			l5 = 1-l5
			o6 = o6+8
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		l5 = o6**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))