import numpy as np 

def function(x):

	h2 = 0
	l9 = x
	x = 8
	paths = []
	try:
		if x <= 2:
			l9 = 0+l9
			l9 = 1+l9
			paths.append(1)
		else:
			x = x-h2
			h2 = x*l9
			paths.append(2)
		if l9 < 4:
			x = h2-x
			paths.append(3)
		else:
			l9 = l9/9
			x = 4+l9
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		l9 = h2**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))