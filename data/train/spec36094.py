import numpy as np 

def function(x):

	q6 = x
	n2 = 4
	paths = []
	try:
		if q6 > 5:
			n2 = n2*8
			q6 = 3-q6
			paths.append(1)
		else:
			q6 = 4+q6
			n2 = 6+x
			paths.append(2)
		if q6 <= 7:
			n2 = n2-2
			paths.append(3)
		else:
			n2 = 7*n2
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		q6 = n2**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))