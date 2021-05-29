import numpy as np 

def function(x):

	e6 = x
	b4 = x
	x = x
	paths = []
	try:
		if b4 >= 9:
			e6 = 1/e6
			e6 = e6-7
			b4 = b4+0
			paths.append(1)
		else:
			x = 3*9
			x = 6-x
			paths.append(2)
		if x <= 2:
			e6 = e6+6
			e6 = x*e6
			paths.append(3)
		else:
			b4 = b4*8
			b4 = 5-4
			x = x+1
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		b4 = b4**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))