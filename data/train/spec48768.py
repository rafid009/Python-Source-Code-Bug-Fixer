import numpy as np 

def function(x):

	r7 = 7
	l8 = x
	paths = []
	try:
		if l8 >= 2:
			l8 = l8-3
			x = 5+x
			r7 = r7+7
			paths.append(1)
		else:
			r7 = 1+r7
			x = r7+1
			paths.append(2)
		if l8 >= 6:
			r7 = r7+r7
			r7 = r7*1
			paths.append(3)
		else:
			l8 = l8-4
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		r7 = l8**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))