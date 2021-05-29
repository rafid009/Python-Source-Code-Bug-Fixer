import numpy as np 

def function(x):

	l9 = x
	r1 = 9
	paths = []
	try:
		if l9 < 5:
			r1 = 5*r1
			paths.append(1)
		else:
			r1 = r1/3
			x = 1-x
			x = 1-x
			paths.append(2)
		if x <= 6:
			r1 = 9-4
			r1 = r1-r1
			r1 = x/1
			paths.append(3)
		else:
			x = x*5
			l9 = l9*r1
			l9 = l9-r1
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		r1 = l9**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))