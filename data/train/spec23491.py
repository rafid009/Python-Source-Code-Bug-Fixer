import numpy as np 

def function(x):

	l9 = x
	v2 = x
	paths = []
	try:
		if l9 <= 9:
			x = x+7
			v2 = 1/x
			l9 = 9-l9
			paths.append(1)
		else:
			v2 = 7+v2
			l9 = l9-7
			l9 = 3-x
			paths.append(2)
		if x < 9:
			v2 = l9*3
			paths.append(3)
		else:
			v2 = v2-8
			v2 = 3+v2
			v2 = v2/1
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