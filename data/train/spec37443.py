import numpy as np 

def function(x):

	j4 = x
	b2 = 5
	paths = []
	try:
		if b2 < 9:
			x = x-8
			j4 = j4+b2
			x = x*4
			paths.append(1)
		else:
			x = b2+2
			paths.append(2)
		if b2 <= 4:
			b2 = j4/x
			x = x*7
			paths.append(3)
		else:
			j4 = j4+x
			j4 = 1+j4
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