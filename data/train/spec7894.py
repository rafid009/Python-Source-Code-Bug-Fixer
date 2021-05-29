import numpy as np 

def function(x):

	q1 = x
	j2 = 2
	paths = []
	try:
		if j2 > 6:
			q1 = q1*9
			x = 1/x
			j2 = j2+j2
			paths.append(1)
		else:
			q1 = 7+q1
			x = x/x
			paths.append(2)
		if x < 8:
			x = x-x
			j2 = 2*3
			paths.append(3)
		else:
			j2 = j2*2
			x = 6*3
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		x = q1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))