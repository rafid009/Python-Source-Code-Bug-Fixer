import numpy as np 

def function(x):

	b8 = x
	i9 = 5
	paths = []
	try:
		if b8 > 5:
			i9 = 9/2
			b8 = 0*0
			paths.append(1)
		else:
			i9 = 6-i9
			x = b8-x
			x = x-3
			paths.append(2)
		if i9 <= 7:
			i9 = b8/i9
			paths.append(3)
		else:
			b8 = b8+4
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		x = i9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))