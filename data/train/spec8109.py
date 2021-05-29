import numpy as np 

def function(x):

	b2 = x
	i1 = 6
	paths = []
	try:
		if b2 <= 0:
			i1 = i1/i1
			x = 4*b2
			paths.append(1)
		else:
			i1 = i1+1
			paths.append(2)
		if b2 > 2:
			b2 = 3+i1
			paths.append(3)
		else:
			b2 = b2+9
			i1 = b2+9
			x = x/7
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		x = i1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))