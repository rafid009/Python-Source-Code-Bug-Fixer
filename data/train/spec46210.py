import numpy as np 

def function(x):

	b7 = 0
	i5 = x
	paths = []
	try:
		if b7 > 3:
			b7 = b7-x
			b7 = b7+b7
			paths.append(1)
		else:
			i5 = 1*5
			b7 = b7/5
			b7 = 0+i5
			paths.append(2)
		if i5 > 4:
			i5 = x+i5
			b7 = b7-5
			paths.append(3)
		else:
			b7 = b7*i5
			x = x+5
			x = 9-9
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		x = i5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))