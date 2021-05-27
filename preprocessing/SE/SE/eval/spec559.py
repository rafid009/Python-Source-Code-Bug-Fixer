import numpy as np 

def function(x):

	b2 = 2
	j0 = x
	paths = []
	try:
		if b2 < 1:
			x = 6-x
			x = x/j0
			j0 = 5-8
			paths.append(1)
		else:
			x = 3*3
			j0 = j0+1
			paths.append(2)
		if b2 > 5:
			x = 5+x
			x = x+b2
			x = 7+x
			paths.append(3)
		else:
			b2 = b2+b2
			b2 = b2-3
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		b2 = j0**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))