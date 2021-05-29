import numpy as np 

def function(x):

	l9 = 8
	j2 = x
	paths = []
	try:
		if l9 >= 3:
			j2 = j2/7
			l9 = 6-7
			l9 = l9/x
			paths.append(1)
		else:
			x = x-7
			x = x/9
			x = 0/x
			paths.append(2)
		if l9 < 1:
			x = 1-x
			l9 = 1+l9
			paths.append(3)
		else:
			j2 = 1*9
			l9 = 9-1
			l9 = 8*l9
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		l9 = l9**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))