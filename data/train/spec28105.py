import numpy as np 

def function(x):

	i5 = 7
	b5 = x
	paths = []
	try:
		if x > 3:
			i5 = i5+3
			paths.append(1)
		else:
			b5 = b5+4
			i5 = 0+i5
			paths.append(2)
		if b5 >= 8:
			b5 = b5/3
			x = x*2
			paths.append(3)
		else:
			x = i5/b5
			b5 = 3/x
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		b5 = b5**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))