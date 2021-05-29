import numpy as np 

def function(x):

	y3 = 9
	b2 = x
	x = x
	paths = []
	try:
		if x > 5:
			b2 = x+b2
			b2 = x/b2
			paths.append(1)
		else:
			y3 = 6-y3
			paths.append(2)
		if y3 <= 6:
			b2 = b2-4
			paths.append(3)
		else:
			y3 = y3+4
			b2 = b2+8
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		y3 = b2**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))