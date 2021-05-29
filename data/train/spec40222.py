import numpy as np 

def function(x):

	v3 = 8
	l7 = x
	paths = []
	try:
		if x > 2:
			x = 2/3
			v3 = v3+v3
			v3 = v3/3
			paths.append(1)
		else:
			x = x+7
			paths.append(2)
		if l7 >= 7:
			x = x/5
			paths.append(3)
		else:
			l7 = l7*5
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		v3 = l7**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))