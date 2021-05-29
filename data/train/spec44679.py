import numpy as np 

def function(x):

	l6 = 4
	j3 = x
	paths = []
	try:
		if j3 > 1:
			l6 = l6-x
			l6 = 9/l6
			x = x+4
			paths.append(1)
		else:
			j3 = j3/1
			paths.append(2)
		if x >= 1:
			j3 = j3-j3
			j3 = 1+l6
			l6 = l6/2
			paths.append(3)
		else:
			l6 = x/l6
			x = x+5
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		l6 = l6**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))