import numpy as np 

def function(x):

	b1 = 2
	u0 = x
	paths = []
	try:
		if x <= 5:
			x = x/x
			b1 = u0+b1
			paths.append(1)
		else:
			x = x+1
			paths.append(2)
		if b1 < 2:
			u0 = 6-x
			x = 4/1
			u0 = 1+u0
			paths.append(3)
		else:
			u0 = u0+x
			x = x-u0
			x = x+6
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		b1 = b1**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))