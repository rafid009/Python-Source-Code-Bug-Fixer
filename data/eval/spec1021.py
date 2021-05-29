import numpy as np 

def function(x):

	b4 = 0
	r7 = x
	x = x
	paths = []
	try:
		if r7 > 7:
			r7 = x+5
			paths.append(1)
		else:
			b4 = b4-8
			r7 = b4/9
			paths.append(2)
		if x > 2:
			x = 8*x
			paths.append(3)
		else:
			x = 7-x
			x = x+b4
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