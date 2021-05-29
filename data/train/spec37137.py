import numpy as np 

def function(x):

	u0 = 8
	l4 = 2
	paths = []
	try:
		if u0 <= 4:
			l4 = l4-9
			l4 = 6+l4
			x = 3/x
			paths.append(1)
		else:
			u0 = 0/6
			x = x+4
			u0 = u0*1
			paths.append(2)
		if l4 <= 7:
			l4 = l4-7
			u0 = u0+6
			l4 = 8*5
			paths.append(3)
		else:
			x = x*8
			u0 = l4/x
			l4 = l4*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))