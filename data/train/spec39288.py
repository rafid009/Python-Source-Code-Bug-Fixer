import numpy as np 

def function(x):

	l2 = 9
	j7 = x
	paths = []
	try:
		if x < 6:
			l2 = j7*x
			j7 = j7-0
			j7 = j7/l2
			paths.append(1)
		else:
			l2 = l2-0
			x = 1-5
			x = x+8
			paths.append(2)
		if l2 < 8:
			x = x+1
			paths.append(3)
		else:
			l2 = l2-j7
			x = 0*l2
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		x = j7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))