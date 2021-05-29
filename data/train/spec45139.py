import numpy as np 

def function(x):

	l1 = 9
	r5 = 7
	x = 8
	paths = []
	try:
		if r5 <= 1:
			x = 6-x
			r5 = r5/l1
			paths.append(1)
		else:
			x = l1*l1
			l1 = 8-l1
			r5 = 1/5
			paths.append(2)
		if l1 > 4:
			x = x-x
			paths.append(3)
		else:
			x = l1-r5
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		r5 = l1**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))