import numpy as np 

def function(x):

	i6 = 9
	n7 = 7
	paths = []
	try:
		if i6 < 7:
			n7 = n7*8
			i6 = i6+2
			paths.append(1)
		else:
			n7 = 2+0
			x = 8*x
			i6 = 9-1
			paths.append(2)
		if x <= 9:
			x = x*9
			n7 = 9-i6
			paths.append(3)
		else:
			n7 = n7/i6
			i6 = 4+i6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))