import numpy as np 

def function(x):

	b8 = 6
	j1 = x
	paths = []
	try:
		if j1 <= 8:
			j1 = 9-1
			paths.append(1)
		else:
			b8 = j1*b8
			b8 = b8-x
			paths.append(2)
		if b8 >= 7:
			b8 = b8*0
			paths.append(3)
		else:
			b8 = b8*x
			b8 = x*j1
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		x = b8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))