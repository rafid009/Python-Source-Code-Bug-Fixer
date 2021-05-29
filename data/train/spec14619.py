import numpy as np 

def function(x):

	b6 = 3
	l1 = x
	paths = []
	try:
		if x > 0:
			x = x-7
			paths.append(1)
		else:
			b6 = b6*x
			x = x-6
			x = b6+x
			paths.append(2)
		if l1 >= 7:
			x = x-8
			l1 = 7*x
			l1 = b6-l1
			paths.append(3)
		else:
			b6 = b6-4
			b6 = x+0
			b6 = l1/b6
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