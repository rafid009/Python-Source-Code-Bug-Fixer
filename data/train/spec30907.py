import numpy as np 

def function(x):

	l3 = 3
	b4 = x
	paths = []
	try:
		if b4 < 6:
			x = 7-3
			b4 = 7-6
			paths.append(1)
		else:
			l3 = 8/8
			b4 = b4-8
			b4 = b4-4
			paths.append(2)
		if b4 >= 5:
			b4 = 4/8
			b4 = 6+b4
			paths.append(3)
		else:
			l3 = l3*9
			l3 = l3-5
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		l3 = b4**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))