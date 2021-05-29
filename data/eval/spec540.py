import numpy as np 

def function(x):

	l7 = 4
	j3 = x
	paths = []
	try:
		if j3 <= 6:
			x = j3/2
			j3 = j3-x
			x = l7/x
			paths.append(1)
		else:
			j3 = j3+0
			l7 = 8+l7
			j3 = 7-j3
			paths.append(2)
		if l7 >= 8:
			l7 = 1-l7
			paths.append(3)
		else:
			l7 = x/l7
			l7 = l7+x
			x = 1*6
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		l7 = l7**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))