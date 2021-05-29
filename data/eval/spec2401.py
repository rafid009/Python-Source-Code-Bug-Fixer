import numpy as np 

def function(x):

	j7 = x
	l5 = 0
	paths = []
	try:
		if x <= 3:
			x = j7+2
			j7 = 6*2
			paths.append(1)
		else:
			l5 = j7+x
			l5 = l5+7
			j7 = x*5
			paths.append(2)
		if l5 > 3:
			j7 = 8+5
			j7 = 0*7
			x = l5*x
			paths.append(3)
		else:
			j7 = 9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l5 = x**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))