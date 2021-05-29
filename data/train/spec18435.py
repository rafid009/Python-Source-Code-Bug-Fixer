import numpy as np 

def function(x):

	q9 = 3
	l6 = 7
	x = x
	paths = []
	try:
		if x <= 7:
			l6 = x-2
			q9 = 3+q9
			l6 = 6*l6
			paths.append(1)
		else:
			l6 = l6-1
			q9 = q9+7
			x = x-8
			paths.append(2)
		if l6 <= 3:
			l6 = l6+3
			x = 1+x
			paths.append(3)
		else:
			x = 9+9
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		x = l6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))