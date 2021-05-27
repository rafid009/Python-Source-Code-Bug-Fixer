import numpy as np 

def function(x):

	l9 = 7
	u3 = 8
	paths = []
	try:
		if x < 7:
			l9 = 2/u3
			paths.append(1)
		else:
			u3 = 1*u3
			x = 0+x
			paths.append(2)
		if u3 <= 5:
			l9 = 6+l9
			l9 = 9*l9
			paths.append(3)
		else:
			l9 = l9*u3
			x = x+8
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u3 = x**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))