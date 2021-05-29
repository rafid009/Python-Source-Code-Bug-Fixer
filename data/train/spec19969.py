import numpy as np 

def function(x):

	u7 = 7
	l6 = x
	paths = []
	try:
		if u7 <= 0:
			l6 = l6*8
			x = x+6
			paths.append(1)
		else:
			l6 = l6+x
			x = x+0
			paths.append(2)
		if l6 >= 4:
			u7 = u7+u7
			x = x*u7
			paths.append(3)
		else:
			x = x-7
			l6 = 5*l6
			u7 = 0-x
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