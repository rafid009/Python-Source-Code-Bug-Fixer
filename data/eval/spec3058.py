import numpy as np 

def function(x):

	w6 = x
	l1 = 2
	paths = []
	try:
		if x < 7:
			l1 = l1-3
			paths.append(1)
		else:
			x = x-l1
			l1 = l1*x
			w6 = w6-4
			paths.append(2)
		if l1 > 1:
			w6 = w6+l1
			x = l1*6
			paths.append(3)
		else:
			l1 = w6/l1
			l1 = l1/x
			w6 = w6*1
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		l1 = l1**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))