import numpy as np 

def function(x):

	j2 = 9
	b5 = 7
	paths = []
	try:
		if j2 < 8:
			b5 = b5/9
			x = x+x
			paths.append(1)
		else:
			j2 = j2-8
			b5 = b5+j2
			j2 = j2-j2
			paths.append(2)
		if j2 > 2:
			x = 5-x
			b5 = 6/b5
			x = 3*6
			paths.append(3)
		else:
			j2 = 1+4
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