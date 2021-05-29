import numpy as np 

def function(x):

	l3 = x
	v7 = 9
	paths = []
	try:
		if v7 <= 4:
			v7 = v7-9
			paths.append(1)
		else:
			x = x-5
			x = v7*x
			paths.append(2)
		if l3 <= 3:
			v7 = v7-2
			x = x/6
			paths.append(3)
		else:
			x = x+x
			l3 = 7+l3
			l3 = 5+l3
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		x = l3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))