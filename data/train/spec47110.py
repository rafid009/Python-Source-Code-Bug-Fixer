import numpy as np 

def function(x):

	b5 = x
	y5 = 3
	paths = []
	try:
		if y5 > 4:
			x = 9/1
			b5 = b5*b5
			paths.append(1)
		else:
			x = 9+x
			b5 = b5+8
			paths.append(2)
		if x > 9:
			y5 = b5+x
			paths.append(3)
		else:
			y5 = 5+9
			y5 = y5-9
			b5 = b5*2
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		b5 = b5**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))