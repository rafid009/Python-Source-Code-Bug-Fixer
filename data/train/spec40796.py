import numpy as np 

def function(x):

	e7 = x
	l3 = x
	paths = []
	try:
		if l3 < 3:
			l3 = l3+1
			x = x*9
			x = 8+6
			paths.append(1)
		else:
			x = x/5
			e7 = e7+3
			paths.append(2)
		if x > 8:
			x = l3/l3
			e7 = e7+2
			e7 = 5/5
			paths.append(3)
		else:
			l3 = 0-7
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