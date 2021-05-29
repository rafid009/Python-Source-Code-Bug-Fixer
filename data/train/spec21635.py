import numpy as np 

def function(x):

	b3 = x
	x3 = 4
	paths = []
	try:
		if x3 >= 3:
			x = 4-x
			paths.append(1)
		else:
			x = x/7
			x3 = x3*0
			paths.append(2)
		if x >= 4:
			x3 = x3*4
			b3 = b3+8
			b3 = b3-0
			paths.append(3)
		else:
			b3 = b3+8
			x = 2+x
			x3 = 3-x3
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		b3 = b3**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))