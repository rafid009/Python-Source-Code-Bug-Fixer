import numpy as np 

def function(x):

	j2 = 7
	b6 = x
	x = 0
	paths = []
	try:
		if x <= 6:
			x = b6/b6
			x = 1/4
			x = j2-8
			paths.append(1)
		else:
			x = 9*x
			paths.append(2)
		if b6 > 7:
			b6 = j2/1
			x = 4/x
			b6 = 3-b6
			paths.append(3)
		else:
			j2 = j2/8
			b6 = x*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))