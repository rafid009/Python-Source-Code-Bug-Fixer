import numpy as np 

def function(x):

	k9 = 3
	q3 = x
	paths = []
	try:
		if k9 >= 8:
			x = 3+q3
			x = q3+x
			x = x*5
			paths.append(1)
		else:
			q3 = x/q3
			q3 = q3/6
			paths.append(2)
		if k9 >= 7:
			x = k9-x
			x = 7/5
			paths.append(3)
		else:
			q3 = q3/7
			q3 = q3+7
			x = k9/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k9 = x**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))