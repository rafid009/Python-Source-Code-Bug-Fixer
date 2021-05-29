import numpy as np 

def function(x):

	l3 = 5
	i8 = x
	paths = []
	try:
		if i8 >= 0:
			x = 6+x
			i8 = 1-8
			paths.append(1)
		else:
			l3 = l3*2
			paths.append(2)
		if x <= 2:
			l3 = 3-l3
			x = 7-x
			i8 = 5-i8
			paths.append(3)
		else:
			x = x/1
			x = i8+8
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		l3 = l3**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))