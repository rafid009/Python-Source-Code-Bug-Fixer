import numpy as np 

def function(x):

	u9 = 0
	b5 = x
	x = 2
	paths = []
	try:
		if u9 >= 6:
			u9 = 5/1
			u9 = 1+6
			paths.append(1)
		else:
			u9 = 1/x
			x = 4+3
			paths.append(2)
		if x > 5:
			b5 = 3+b5
			paths.append(3)
		else:
			x = x+9
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