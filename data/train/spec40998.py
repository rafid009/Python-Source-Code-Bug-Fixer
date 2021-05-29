import numpy as np 

def function(x):

	b9 = x
	l9 = x
	paths = []
	try:
		if x > 6:
			l9 = l9*3
			l9 = b9*l9
			paths.append(1)
		else:
			x = x/x
			x = x/9
			paths.append(2)
		if b9 < 8:
			l9 = l9-5
			paths.append(3)
		else:
			l9 = l9/l9
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		b9 = l9**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))