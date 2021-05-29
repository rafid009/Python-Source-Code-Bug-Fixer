import numpy as np 

def function(x):

	u2 = 9
	i8 = x
	paths = []
	try:
		if u2 <= 8:
			i8 = x/4
			paths.append(1)
		else:
			u2 = x-i8
			paths.append(2)
		if i8 > 0:
			i8 = i8*x
			paths.append(3)
		else:
			u2 = u2+1
			u2 = x+5
			i8 = x/9
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		x = i8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))