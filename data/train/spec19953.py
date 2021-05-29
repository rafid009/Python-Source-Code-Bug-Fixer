import numpy as np 

def function(x):

	b0 = 8
	i5 = x
	paths = []
	try:
		if i5 <= 2:
			i5 = i5*9
			i5 = i5*1
			paths.append(1)
		else:
			i5 = 9+9
			paths.append(2)
		if b0 >= 7:
			i5 = 7*1
			b0 = x-6
			i5 = i5*5
			paths.append(3)
		else:
			i5 = i5/3
			i5 = i5-4
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		x = b0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))