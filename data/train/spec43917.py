import numpy as np 

def function(x):

	l7 = 1
	d6 = x
	paths = []
	try:
		if x < 4:
			l7 = l7/5
			d6 = 6-d6
			paths.append(1)
		else:
			l7 = l7*d6
			paths.append(2)
		if d6 > 7:
			l7 = x/2
			d6 = d6/6
			paths.append(3)
		else:
			d6 = d6-l7
			l7 = 2+l7
			x = x+d6
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		l7 = l7**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))