import numpy as np 

def function(x):

	l9 = x
	k5 = x
	x = 2
	paths = []
	try:
		if l9 < 7:
			k5 = x*8
			k5 = 0+k5
			x = 8/x
			paths.append(1)
		else:
			k5 = 1/k5
			k5 = 1-k5
			paths.append(2)
		if x <= 1:
			l9 = l9+2
			k5 = 0*3
			paths.append(3)
		else:
			k5 = k5-8
			k5 = l9/x
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		l9 = k5**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))