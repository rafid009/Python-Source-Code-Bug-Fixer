import numpy as np 

def function(x):

	j3 = x
	l7 = x
	paths = []
	try:
		if x > 9:
			x = x*l7
			paths.append(1)
		else:
			x = x+7
			j3 = 3/j3
			j3 = j3/9
			paths.append(2)
		if x >= 5:
			l7 = l7*l7
			j3 = 2+j3
			l7 = 4-2
			paths.append(3)
		else:
			l7 = l7/1
			x = 5/x
			j3 = j3/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j3 = x**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))