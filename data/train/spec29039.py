import numpy as np 

def function(x):

	l8 = x
	j2 = 1
	paths = []
	try:
		if x > 5:
			x = 6-2
			l8 = x*l8
			j2 = 8-j2
			paths.append(1)
		else:
			x = l8+x
			paths.append(2)
		if l8 >= 0:
			x = x+0
			x = x/9
			x = 5*x
			paths.append(3)
		else:
			l8 = l8/l8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j2 = x**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))