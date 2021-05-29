import numpy as np 

def function(x):

	j8 = x
	l6 = 4
	paths = []
	try:
		if x < 4:
			l6 = x/l6
			l6 = l6-l6
			paths.append(1)
		else:
			j8 = 5+j8
			paths.append(2)
		if x <= 0:
			x = x/6
			paths.append(3)
		else:
			x = x/5
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		l6 = j8**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))