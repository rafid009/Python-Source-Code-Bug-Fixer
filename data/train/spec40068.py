import numpy as np 

def function(x):

	d3 = x
	l3 = x
	paths = []
	try:
		if l3 < 1:
			l3 = l3+1
			paths.append(1)
		else:
			l3 = l3*4
			d3 = 7-d3
			paths.append(2)
		if x < 5:
			l3 = l3-7
			x = x/7
			paths.append(3)
		else:
			d3 = 8+2
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