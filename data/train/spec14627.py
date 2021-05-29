import numpy as np 

def function(x):

	a7 = x
	l9 = 9
	paths = []
	try:
		if a7 < 4:
			a7 = a7-7
			paths.append(1)
		else:
			l9 = l9+2
			paths.append(2)
		if l9 > 2:
			a7 = a7+5
			l9 = x/5
			paths.append(3)
		else:
			a7 = 8+a7
			l9 = l9-9
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