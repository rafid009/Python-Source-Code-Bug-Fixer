import numpy as np 

def function(x):

	b6 = 4
	r3 = 7
	paths = []
	try:
		if x > 7:
			b6 = 1*b6
			paths.append(1)
		else:
			b6 = b6+x
			paths.append(2)
		if b6 >= 7:
			b6 = b6-4
			paths.append(3)
		else:
			b6 = 3/x
			r3 = r3+8
			b6 = 3-x
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		r3 = b6**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))