import numpy as np 

def function(x):

	b6 = x
	l5 = x
	paths = []
	try:
		if x <= 9:
			b6 = 8-b6
			l5 = 0*l5
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if b6 <= 2:
			b6 = b6+0
			l5 = l5-4
			paths.append(3)
		else:
			x = 4/2
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		b6 = l5**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))