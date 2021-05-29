import numpy as np 

def function(x):

	b3 = x
	r3 = 7
	paths = []
	try:
		if b3 >= 4:
			b3 = b3/8
			paths.append(1)
		else:
			r3 = 0/r3
			r3 = 7-6
			x = 4/x
			paths.append(2)
		if r3 > 0:
			b3 = b3*5
			x = b3-x
			paths.append(3)
		else:
			r3 = r3/1
			r3 = 3*r3
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