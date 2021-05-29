import numpy as np 

def function(x):

	f3 = x
	l3 = x
	paths = []
	try:
		if l3 >= 8:
			f3 = x-3
			f3 = f3+9
			f3 = 7-3
			paths.append(1)
		else:
			l3 = l3*4
			x = 3*1
			l3 = 9-l3
			paths.append(2)
		if f3 >= 7:
			x = 7+x
			paths.append(3)
		else:
			x = 2/x
			l3 = 9*6
			x = 4+l3
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		l3 = l3**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))