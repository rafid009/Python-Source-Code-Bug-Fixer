import numpy as np 

def function(x):

	l5 = 6
	d3 = x
	paths = []
	try:
		if d3 <= 4:
			l5 = d3-l5
			d3 = 7+x
			paths.append(1)
		else:
			l5 = l5+1
			x = x*x
			paths.append(2)
		if d3 <= 5:
			d3 = d3-x
			l5 = l5-1
			x = 7-x
			paths.append(3)
		else:
			x = l5+9
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		x = l5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))