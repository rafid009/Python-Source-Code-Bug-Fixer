import numpy as np 

def function(x):

	q1 = 3
	i1 = 5
	paths = []
	try:
		if x <= 2:
			x = x*3
			i1 = x-i1
			paths.append(1)
		else:
			i1 = i1+q1
			i1 = q1*3
			i1 = 6+i1
			paths.append(2)
		if q1 < 6:
			q1 = 1+7
			x = x*x
			q1 = q1+x
			paths.append(3)
		else:
			i1 = x*8
			i1 = 7*i1
			q1 = q1+q1
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		q1 = i1**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))