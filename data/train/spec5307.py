import numpy as np 

def function(x):

	b7 = 5
	j2 = x
	paths = []
	try:
		if b7 > 7:
			x = x*5
			b7 = b7/b7
			b7 = b7+b7
			paths.append(1)
		else:
			b7 = b7+8
			b7 = b7/x
			paths.append(2)
		if x > 5:
			j2 = 3/j2
			b7 = 7*1
			b7 = j2-j2
			paths.append(3)
		else:
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		b7 = b7**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))