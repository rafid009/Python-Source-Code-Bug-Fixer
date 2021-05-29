import numpy as np 

def function(x):

	l2 = 4
	j9 = 5
	paths = []
	try:
		if j9 > 6:
			j9 = j9*j9
			x = x+x
			x = 6-l2
			paths.append(1)
		else:
			j9 = 6/5
			x = x-x
			x = x-l2
			paths.append(2)
		if j9 > 7:
			j9 = j9*2
			x = j9+2
			paths.append(3)
		else:
			l2 = l2*9
			j9 = j9/x
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		l2 = j9**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))