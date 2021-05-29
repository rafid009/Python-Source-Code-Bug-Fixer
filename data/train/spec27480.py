import numpy as np 

def function(x):

	l1 = x
	paths = []
	try:
		if l1 >= 8:
			l1 = l1/9
			paths.append(1)
		else:
			l1 = x*0
			paths.append(2)
		if l1 > 1:
			x = 9*l1
			l1 = x*8
			l1 = l1+3
			paths.append(3)
		else:
			l1 = x-l1
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