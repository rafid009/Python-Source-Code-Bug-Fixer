import numpy as np 

def function(x):

	l7 = 5
	v7 = 2
	paths = []
	try:
		if v7 > 7:
			l7 = l7*6
			x = v7+x
			paths.append(1)
		else:
			x = x/l7
			paths.append(2)
		if x < 0:
			l7 = v7+v7
			v7 = x+0
			paths.append(3)
		else:
			l7 = 9*3
			v7 = v7-9
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		v7 = v7**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))