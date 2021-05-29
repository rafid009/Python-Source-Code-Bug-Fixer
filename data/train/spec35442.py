import numpy as np 

def function(x):

	b8 = 4
	j3 = 7
	paths = []
	try:
		if b8 >= 4:
			b8 = 0-b8
			j3 = j3*1
			paths.append(1)
		else:
			b8 = b8*7
			paths.append(2)
		if b8 >= 1:
			j3 = j3+4
			b8 = 5+b8
			b8 = b8-b8
			paths.append(3)
		else:
			j3 = b8/8
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		b8 = b8**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))