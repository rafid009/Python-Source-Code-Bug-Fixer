import numpy as np 

def function(x):

	q8 = 0
	l1 = x
	paths = []
	try:
		if q8 >= 7:
			x = x*8
			q8 = 6+q8
			paths.append(1)
		else:
			q8 = x+4
			paths.append(2)
		if x <= 7:
			x = 8+x
			l1 = q8-0
			q8 = 4/x
			paths.append(3)
		else:
			q8 = q8+q8
			x = x+5
			x = x+q8
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		q8 = l1**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))