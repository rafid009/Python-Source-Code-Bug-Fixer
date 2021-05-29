import numpy as np 

def function(x):

	b4 = x
	u3 = x
	paths = []
	try:
		if b4 <= 7:
			b4 = b4*u3
			paths.append(1)
		else:
			u3 = 6-u3
			x = x/6
			paths.append(2)
		if b4 < 7:
			x = 9-u3
			x = b4+7
			paths.append(3)
		else:
			b4 = x/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b4 = x**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))