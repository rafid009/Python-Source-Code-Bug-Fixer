import numpy as np 

def function(x):

	i8 = x
	l7 = x
	paths = []
	try:
		if l7 <= 1:
			i8 = 5*i8
			i8 = i8/5
			paths.append(1)
		else:
			x = 5-l7
			i8 = i8/4
			i8 = 1-i8
			paths.append(2)
		if l7 <= 5:
			l7 = l7+i8
			x = x/7
			paths.append(3)
		else:
			x = x/4
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