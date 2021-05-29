import numpy as np 

def function(x):

	j7 = 9
	l7 = 9
	paths = []
	try:
		if l7 > 3:
			j7 = j7-j7
			j7 = j7+4
			paths.append(1)
		else:
			j7 = j7*8
			l7 = 9+l7
			paths.append(2)
		if l7 > 3:
			x = l7+9
			j7 = 0-j7
			paths.append(3)
		else:
			j7 = j7-j7
			l7 = l7-2
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		l7 = j7**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))