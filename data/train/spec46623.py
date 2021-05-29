import numpy as np 

def function(x):

	l5 = 1
	o1 = 0
	paths = []
	try:
		if x < 4:
			x = 6/9
			l5 = l5+6
			l5 = 5*l5
			paths.append(1)
		else:
			x = x-1
			paths.append(2)
		if l5 < 0:
			o1 = 2*o1
			l5 = l5+7
			l5 = l5+o1
			paths.append(3)
		else:
			o1 = o1-5
			l5 = 0*l5
			l5 = 8/2
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		l5 = o1**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))