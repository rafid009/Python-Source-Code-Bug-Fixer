import numpy as np 

def function(x):

	j8 = x
	l2 = 4
	x = x
	paths = []
	try:
		if l2 <= 3:
			l2 = l2*5
			j8 = j8-4
			x = l2*x
			paths.append(1)
		else:
			j8 = j8+2
			l2 = 6/x
			paths.append(2)
		if j8 <= 2:
			x = x+8
			paths.append(3)
		else:
			l2 = l2+x
			j8 = j8/l2
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		l2 = j8**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))