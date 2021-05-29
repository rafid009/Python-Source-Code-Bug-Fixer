import numpy as np 

def function(x):

	b9 = 5
	f8 = 9
	paths = []
	try:
		if x < 3:
			b9 = b9/6
			paths.append(1)
		else:
			x = x*3
			b9 = 1-b9
			paths.append(2)
		if x <= 4:
			b9 = b9+1
			paths.append(3)
		else:
			f8 = 7+f8
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