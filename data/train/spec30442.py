import numpy as np 

def function(x):

	v2 = x
	l6 = 2
	paths = []
	try:
		if x < 9:
			v2 = v2/6
			paths.append(1)
		else:
			x = l6*1
			l6 = l6-3
			x = x*v2
			paths.append(2)
		if x < 2:
			v2 = v2-3
			v2 = 6+x
			paths.append(3)
		else:
			v2 = 9/6
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		v2 = l6**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))