import numpy as np 

def function(x):

	j9 = 9
	l7 = 3
	paths = []
	try:
		if x > 7:
			x = l7+x
			j9 = j9/8
			paths.append(1)
		else:
			j9 = x+7
			paths.append(2)
		if j9 < 3:
			x = x-5
			j9 = 2-7
			x = x-1
			paths.append(3)
		else:
			j9 = j9/2
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		l7 = j9**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))