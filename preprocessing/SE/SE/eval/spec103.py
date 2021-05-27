import numpy as np 

def function(x):

	b1 = 8
	l3 = 1
	paths = []
	try:
		if x < 2:
			l3 = 7+l3
			l3 = 0/b1
			paths.append(1)
		else:
			l3 = 1*l3
			l3 = l3*l3
			paths.append(2)
		if l3 <= 4:
			l3 = 4+l3
			x = x-0
			b1 = 8*x
			paths.append(3)
		else:
			x = 0*7
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		l3 = b1**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))