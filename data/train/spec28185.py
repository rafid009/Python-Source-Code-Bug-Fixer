import numpy as np 

def function(x):

	b4 = x
	r4 = 6
	paths = []
	try:
		if b4 >= 0:
			b4 = b4/x
			b4 = b4*b4
			paths.append(1)
		else:
			x = 7+x
			b4 = b4*3
			paths.append(2)
		if x < 8:
			x = 8+b4
			r4 = r4-8
			paths.append(3)
		else:
			r4 = 0-0
			b4 = 6-b4
			x = x*2
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