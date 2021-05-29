import numpy as np 

def function(x):

	b7 = x
	x6 = x
	x = x
	paths = []
	try:
		if b7 <= 7:
			b7 = b7*6
			x = 4+x
			paths.append(1)
		else:
			x = x/x
			x6 = 0-x6
			paths.append(2)
		if x < 4:
			b7 = b7-5
			x = 3*x
			paths.append(3)
		else:
			x6 = x6/9
			b7 = 7+5
			b7 = 5+b7
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		b7 = x6**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))