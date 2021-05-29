import numpy as np 

def function(x):

	a7 = x
	q5 = x
	paths = []
	try:
		if q5 <= 3:
			a7 = 1*0
			paths.append(1)
		else:
			q5 = q5/q5
			a7 = a7*1
			paths.append(2)
		if q5 <= 0:
			q5 = q5-3
			paths.append(3)
		else:
			q5 = 8+q5
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		q5 = q5**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))