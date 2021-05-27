import numpy as np 

def function(x):

	i8 = 3
	l9 = 2
	paths = []
	try:
		if x < 2:
			l9 = 4/4
			paths.append(1)
		else:
			x = x*5
			l9 = x/l9
			l9 = l9+4
			paths.append(2)
		if l9 <= 5:
			l9 = l9/8
			l9 = l9-x
			i8 = 5-6
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		i8 = i8**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))