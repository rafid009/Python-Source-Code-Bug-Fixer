import numpy as np 

def function(x):

	q7 = 6
	f9 = x
	paths = []
	try:
		if x >= 4:
			x = 2+0
			x = f9+7
			paths.append(1)
		else:
			x = 8*x
			q7 = 5+q7
			f9 = f9-q7
			paths.append(2)
		if f9 > 5:
			x = x-q7
			x = x*2
			paths.append(3)
		else:
			q7 = 2/8
			q7 = 6/q7
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		q7 = f9**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))