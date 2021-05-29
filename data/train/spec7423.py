import numpy as np 

def function(x):

	b8 = x
	p9 = x
	paths = []
	try:
		if x < 5:
			p9 = p9-7
			b8 = b8+0
			paths.append(1)
		else:
			b8 = b8/x
			b8 = b8/7
			p9 = 2/8
			paths.append(2)
		if x > 5:
			p9 = 3+p9
			b8 = 9+0
			paths.append(3)
		else:
			b8 = b8-4
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		b8 = b8**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))