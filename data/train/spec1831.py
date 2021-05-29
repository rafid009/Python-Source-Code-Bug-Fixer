import numpy as np 

def function(x):

	b9 = x
	l1 = x
	paths = []
	try:
		if x >= 7:
			l1 = 2*x
			b9 = l1-b9
			x = x+4
			paths.append(1)
		else:
			l1 = l1/b9
			x = x/1
			x = x*x
			paths.append(2)
		if l1 <= 9:
			x = x+3
			paths.append(3)
		else:
			x = 9*x
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		b9 = b9**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))