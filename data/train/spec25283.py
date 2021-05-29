import numpy as np 

def function(x):

	q5 = x
	l9 = 1
	paths = []
	try:
		if l9 <= 9:
			x = x*5
			l9 = q5-8
			x = x*3
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if q5 > 5:
			q5 = x/x
			x = x/x
			paths.append(3)
		else:
			l9 = l9*7
			l9 = 2+x
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		q5 = l9**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))