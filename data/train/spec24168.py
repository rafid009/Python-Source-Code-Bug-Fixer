import numpy as np 

def function(x):

	b6 = x
	a4 = x
	paths = []
	try:
		if b6 > 6:
			a4 = 0*a4
			b6 = 3*b6
			b6 = 4/7
			paths.append(1)
		else:
			a4 = b6+b6
			paths.append(2)
		if b6 < 1:
			a4 = 3+a4
			a4 = 8+a4
			x = 9/1
			paths.append(3)
		else:
			b6 = 1*b6
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		b6 = a4**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))