import numpy as np 

def function(x):

	l3 = 9
	r2 = 8
	paths = []
	try:
		if r2 > 4:
			x = x/2
			l3 = 5/7
			paths.append(1)
		else:
			l3 = r2*5
			paths.append(2)
		if r2 > 2:
			l3 = 8-x
			r2 = 5+r2
			l3 = l3*6
			paths.append(3)
		else:
			l3 = r2+0
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		r2 = l3**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))