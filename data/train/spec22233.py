import numpy as np 

def function(x):

	l2 = x
	d3 = 3
	paths = []
	try:
		if l2 <= 5:
			l2 = l2+x
			paths.append(1)
		else:
			x = 2/d3
			d3 = 1+d3
			d3 = 0*5
			paths.append(2)
		if x > 7:
			l2 = 1-l2
			x = 5/x
			x = 7+x
			paths.append(3)
		else:
			x = x*l2
			d3 = d3-l2
			x = d3+2
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		l2 = d3**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))