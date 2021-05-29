import numpy as np 

def function(x):

	l6 = x
	k7 = 6
	paths = []
	try:
		if x > 4:
			k7 = 0*l6
			paths.append(1)
		else:
			k7 = 9/k7
			l6 = 8*k7
			k7 = k7/2
			paths.append(2)
		if x < 5:
			l6 = l6-0
			x = 6*x
			paths.append(3)
		else:
			k7 = 1-7
			l6 = 4-l6
			x = x/6
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		k7 = l6**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))