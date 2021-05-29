import numpy as np 

def function(x):

	l9 = 2
	j9 = 7
	paths = []
	try:
		if j9 <= 5:
			l9 = x+7
			l9 = 5*0
			paths.append(1)
		else:
			l9 = 8-1
			paths.append(2)
		if x >= 2:
			j9 = x-j9
			j9 = j9/x
			paths.append(3)
		else:
			j9 = j9/j9
			l9 = 8*l9
			j9 = j9+j9
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		x = j9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))