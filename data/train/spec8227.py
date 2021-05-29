import numpy as np 

def function(x):

	d3 = 3
	l9 = 4
	paths = []
	try:
		if l9 <= 4:
			l9 = l9-6
			d3 = l9/d3
			l9 = l9/7
			paths.append(1)
		else:
			x = l9+1
			l9 = 4-l9
			x = x+6
			paths.append(2)
		if d3 >= 6:
			x = x+5
			l9 = 3*l9
			paths.append(3)
		else:
			x = 6/1
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		x = l9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))