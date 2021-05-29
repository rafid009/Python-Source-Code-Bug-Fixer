import numpy as np 

def function(x):

	l9 = 3
	j3 = x
	x = 5
	paths = []
	try:
		if j3 >= 5:
			x = 2+7
			j3 = 4/j3
			paths.append(1)
		else:
			x = 0*5
			paths.append(2)
		if l9 <= 6:
			l9 = x+2
			paths.append(3)
		else:
			l9 = l9/7
			l9 = x-1
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		l9 = j3**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))