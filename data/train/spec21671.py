import numpy as np 

def function(x):

	b1 = 0
	l9 = x
	paths = []
	try:
		if b1 <= 4:
			x = 4*l9
			x = x+8
			l9 = x-b1
			paths.append(1)
		else:
			b1 = x+b1
			paths.append(2)
		if l9 >= 7:
			l9 = l9*l9
			x = b1-x
			paths.append(3)
		else:
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		x = l9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))