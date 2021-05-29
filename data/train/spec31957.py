import numpy as np 

def function(x):

	k2 = 9
	l7 = 9
	paths = []
	try:
		if x > 5:
			k2 = k2/5
			paths.append(1)
		else:
			x = 6+k2
			x = 7*9
			paths.append(2)
		if x > 6:
			l7 = l7/k2
			k2 = k2-7
			paths.append(3)
		else:
			x = x/9
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