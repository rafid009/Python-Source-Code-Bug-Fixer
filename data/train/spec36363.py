import numpy as np 

def function(x):

	q5 = x
	x3 = x
	paths = []
	try:
		if x > 9:
			q5 = q5+0
			x = x/3
			paths.append(1)
		else:
			q5 = q5+5
			paths.append(2)
		if x3 <= 7:
			q5 = q5-5
			x = 9+x
			paths.append(3)
		else:
			q5 = 0+q5
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x = x3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))