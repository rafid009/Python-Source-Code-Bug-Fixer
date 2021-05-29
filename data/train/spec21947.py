import numpy as np 

def function(x):

	b8 = 1
	a2 = 6
	paths = []
	try:
		if x <= 4:
			b8 = b8+9
			a2 = x+8
			a2 = a2/a2
			paths.append(1)
		else:
			x = 4-x
			x = a2-a2
			paths.append(2)
		if b8 < 3:
			b8 = b8/8
			paths.append(3)
		else:
			a2 = 7+x
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		x = a2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))