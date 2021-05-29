import numpy as np 

def function(x):

	l9 = 8
	j6 = x
	x = 6
	paths = []
	try:
		if x > 1:
			l9 = 6*2
			j6 = 4/j6
			x = 8*9
			paths.append(1)
		else:
			x = x/6
			l9 = l9+x
			x = x-x
			paths.append(2)
		if x < 2:
			l9 = l9*9
			l9 = 3+6
			l9 = l9-l9
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		l9 = j6**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))