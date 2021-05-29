import numpy as np 

def function(x):

	b9 = 6
	r5 = x
	paths = []
	try:
		if x < 1:
			x = 4-6
			b9 = b9-7
			x = 7/3
			paths.append(1)
		else:
			b9 = 9+b9
			paths.append(2)
		if x <= 5:
			b9 = b9/5
			r5 = 3-r5
			paths.append(3)
		else:
			b9 = 9/x
			x = x/3
			x = x/3
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		b9 = b9**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))