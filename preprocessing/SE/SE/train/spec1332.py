import numpy as np 

def function(x):

	b9 = x
	v7 = 3
	paths = []
	try:
		if b9 <= 6:
			b9 = 6/b9
			x = 8+x
			paths.append(1)
		else:
			x = 2-x
			x = x*9
			paths.append(2)
		if v7 > 8:
			b9 = 4+b9
			b9 = 3-b9
			x = x*0
			paths.append(3)
		else:
			b9 = x/b9
			x = 8/b9
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		x = b9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))