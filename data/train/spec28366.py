import numpy as np 

def function(x):

	b2 = x
	j2 = 3
	paths = []
	try:
		if x <= 4:
			j2 = j2*b2
			j2 = 7-0
			b2 = b2-j2
			paths.append(1)
		else:
			x = j2+1
			j2 = x*j2
			paths.append(2)
		if x <= 2:
			x = 1/x
			x = b2+4
			paths.append(3)
		else:
			x = x+b2
			x = 3*6
			x = j2-x
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