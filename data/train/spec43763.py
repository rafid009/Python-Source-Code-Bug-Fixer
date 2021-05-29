import numpy as np 

def function(x):

	r1 = x
	l2 = 6
	paths = []
	try:
		if r1 > 5:
			x = 1-x
			paths.append(1)
		else:
			r1 = r1*6
			paths.append(2)
		if l2 > 5:
			r1 = 8-r1
			l2 = x*5
			l2 = l2+8
			paths.append(3)
		else:
			x = l2+8
			x = 5+x
			r1 = r1*r1
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		x = r1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))