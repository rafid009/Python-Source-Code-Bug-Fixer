import numpy as np 

def function(x):

	y2 = 0
	b2 = 9
	paths = []
	try:
		if b2 < 2:
			b2 = b2+9
			y2 = 1*0
			y2 = 3*y2
			paths.append(1)
		else:
			b2 = 4+1
			paths.append(2)
		if x >= 2:
			x = x+3
			paths.append(3)
		else:
			y2 = b2/4
			b2 = b2+y2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b2 = x**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))