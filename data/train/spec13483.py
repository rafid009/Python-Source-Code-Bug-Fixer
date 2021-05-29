import numpy as np 

def function(x):

	l3 = x
	b0 = x
	paths = []
	try:
		if l3 > 5:
			b0 = x-9
			paths.append(1)
		else:
			l3 = l3+2
			paths.append(2)
		if b0 < 5:
			b0 = 5*4
			paths.append(3)
		else:
			l3 = l3+2
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		l3 = l3**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))