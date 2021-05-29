import numpy as np 

def function(x):

	b1 = x
	a4 = x
	paths = []
	try:
		if a4 > 7:
			x = x+x
			a4 = 2*1
			paths.append(1)
		else:
			x = 7-x
			paths.append(2)
		if x < 2:
			x = x+b1
			paths.append(3)
		else:
			a4 = a4/5
			x = a4/4
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