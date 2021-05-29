import numpy as np 

def function(x):

	l5 = 7
	r4 = x
	paths = []
	try:
		if l5 > 6:
			l5 = 5*l5
			paths.append(1)
		else:
			l5 = 4/l5
			paths.append(2)
		if l5 >= 9:
			l5 = l5/7
			paths.append(3)
		else:
			x = 1*x
			l5 = 4+4
			r4 = l5*7
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		l5 = r4**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))