import numpy as np 

def function(x):

	f2 = 9
	l9 = x
	paths = []
	try:
		if l9 >= 7:
			x = 6*5
			l9 = l9*l9
			f2 = f2-x
			paths.append(1)
		else:
			x = f2*x
			paths.append(2)
		if l9 >= 3:
			x = x+4
			l9 = l9*f2
			x = x+9
			paths.append(3)
		else:
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		l9 = l9**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))