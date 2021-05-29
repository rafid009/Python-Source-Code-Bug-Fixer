import numpy as np 

def function(x):

	h3 = x
	l1 = x
	paths = []
	try:
		if x < 9:
			h3 = 4+5
			paths.append(1)
		else:
			l1 = l1/1
			x = l1-x
			x = h3/l1
			paths.append(2)
		if l1 > 3:
			l1 = h3*l1
			h3 = h3-l1
			h3 = 7*h3
			paths.append(3)
		else:
			h3 = h3+x
			l1 = l1+l1
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		l1 = h3**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))