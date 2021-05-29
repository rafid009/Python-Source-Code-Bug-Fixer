import numpy as np 

def function(x):

	b8 = 5
	j2 = 5
	paths = []
	try:
		if j2 <= 3:
			j2 = 0-5
			x = 3/1
			paths.append(1)
		else:
			x = 1*x
			paths.append(2)
		if j2 < 0:
			j2 = b8/j2
			b8 = b8*0
			j2 = 0+j2
			paths.append(3)
		else:
			x = j2/x
			b8 = b8-b8
			x = x+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))