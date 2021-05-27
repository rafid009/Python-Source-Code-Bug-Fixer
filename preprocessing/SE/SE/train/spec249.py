import numpy as np 

def function(x):

	l9 = 4
	b6 = x
	paths = []
	try:
		if b6 < 2:
			x = x*0
			paths.append(1)
		else:
			x = 4-x
			l9 = l9+8
			x = 3/b6
			paths.append(2)
		if b6 <= 6:
			x = x+l9
			l9 = b6*l9
			l9 = 6*l9
			paths.append(3)
		else:
			b6 = x*x
			l9 = l9+x
			l9 = 5+l9
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		l9 = b6**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))