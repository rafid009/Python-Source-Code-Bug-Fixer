import numpy as np 

def function(x):

	q3 = x
	q5 = x
	paths = []
	try:
		if q3 >= 3:
			q3 = 1+2
			q5 = q5-2
			paths.append(1)
		else:
			q5 = 4+q5
			paths.append(2)
		if q3 > 9:
			q3 = q3*0
			paths.append(3)
		else:
			q3 = q3-x
			x = 6+5
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		x = q3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))