import numpy as np 

def function(x):

	u3 = x
	l5 = x
	paths = []
	try:
		if l5 >= 4:
			l5 = 1*l5
			x = x/2
			u3 = 9/u3
			paths.append(1)
		else:
			x = 5+l5
			l5 = 3-u3
			paths.append(2)
		if u3 <= 1:
			l5 = l5*9
			paths.append(3)
		else:
			l5 = l5-9
			l5 = 1-7
			u3 = u3-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l5 = x**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))