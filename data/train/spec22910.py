import numpy as np 

def function(x):

	k2 = 4
	l7 = x
	paths = []
	try:
		if l7 >= 9:
			k2 = l7*6
			l7 = k2*l7
			paths.append(1)
		else:
			x = x*5
			x = 8*x
			l7 = 2-l7
			paths.append(2)
		if l7 < 8:
			l7 = l7-0
			paths.append(3)
		else:
			k2 = 1-x
			x = x+7
			l7 = x+k2
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		l7 = k2**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))