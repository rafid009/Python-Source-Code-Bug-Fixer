import numpy as np 

def function(x):

	r1 = 1
	b3 = x
	paths = []
	try:
		if r1 <= 8:
			b3 = b3-8
			x = 9/x
			paths.append(1)
		else:
			x = x/3
			r1 = r1+4
			paths.append(2)
		if b3 < 0:
			r1 = r1-5
			paths.append(3)
		else:
			r1 = 3/6
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