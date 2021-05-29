import numpy as np 

def function(x):

	l3 = x
	d0 = 8
	x = 5
	paths = []
	try:
		if d0 >= 0:
			l3 = l3+d0
			paths.append(1)
		else:
			d0 = x*8
			l3 = l3+d0
			paths.append(2)
		if d0 > 4:
			d0 = l3-0
			paths.append(3)
		else:
			x = x*x
			l3 = x-6
			x = x*3
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