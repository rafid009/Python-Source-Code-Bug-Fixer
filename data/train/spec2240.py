import numpy as np 

def function(x):

	f6 = x
	l4 = x
	x = 4
	paths = []
	try:
		if x > 2:
			l4 = l4-6
			x = 2-8
			paths.append(1)
		else:
			l4 = l4-4
			paths.append(2)
		if l4 <= 4:
			x = x+f6
			x = 4/6
			paths.append(3)
		else:
			l4 = 2*x
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		f6 = l4**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))