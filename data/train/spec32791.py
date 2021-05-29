import numpy as np 

def function(x):

	i0 = x
	l6 = x
	paths = []
	try:
		if x <= 5:
			l6 = x*8
			i0 = i0*l6
			paths.append(1)
		else:
			i0 = 9+2
			x = x/7
			l6 = l6-8
			paths.append(2)
		if l6 <= 2:
			i0 = x-3
			l6 = l6/5
			paths.append(3)
		else:
			i0 = i0+2
			l6 = l6+6
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		l6 = l6**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))