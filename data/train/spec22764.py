import numpy as np 

def function(x):

	q9 = 8
	l3 = x
	paths = []
	try:
		if x <= 5:
			q9 = 7/4
			paths.append(1)
		else:
			x = 4-x
			x = 8/x
			paths.append(2)
		if x < 5:
			l3 = 7+3
			l3 = x+q9
			paths.append(3)
		else:
			l3 = l3+8
			q9 = l3-q9
			l3 = x*0
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