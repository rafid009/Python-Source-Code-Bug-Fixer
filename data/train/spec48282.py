import numpy as np 

def function(x):

	q5 = 2
	i4 = x
	paths = []
	try:
		if i4 < 0:
			i4 = i4+0
			i4 = 4+i4
			i4 = i4*x
			paths.append(1)
		else:
			q5 = q5-7
			x = x/8
			paths.append(2)
		if q5 > 3:
			i4 = 0/3
			q5 = q5+6
			paths.append(3)
		else:
			i4 = i4+3
			i4 = 1-q5
			q5 = 6+1
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		i4 = i4**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))