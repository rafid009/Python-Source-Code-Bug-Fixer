import numpy as np 

def function(x):

	i0 = x
	l5 = x
	x = x
	paths = []
	try:
		if l5 >= 7:
			l5 = i0*5
			x = i0*0
			x = 3-x
			paths.append(1)
		else:
			x = x+7
			paths.append(2)
		if x < 9:
			l5 = l5/l5
			paths.append(3)
		else:
			i0 = i0/x
			x = 1+5
			x = l5+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l5 = x**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))