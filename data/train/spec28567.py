import numpy as np 

def function(x):

	v6 = 6
	l8 = x
	paths = []
	try:
		if v6 <= 5:
			l8 = l8/1
			v6 = v6/l8
			x = x*v6
			paths.append(1)
		else:
			x = 9*6
			paths.append(2)
		if v6 > 8:
			x = 3+x
			x = 8*x
			x = x*9
			paths.append(3)
		else:
			x = 2+x
			v6 = v6-v6
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		v6 = l8**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))