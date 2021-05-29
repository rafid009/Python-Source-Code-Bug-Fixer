import numpy as np 

def function(x):

	l3 = 7
	j5 = x
	paths = []
	try:
		if j5 > 3:
			j5 = 6*j5
			l3 = 7/l3
			paths.append(1)
		else:
			x = x/x
			x = 4/x
			paths.append(2)
		if j5 >= 5:
			j5 = j5*2
			j5 = 7-j5
			j5 = j5-j5
			paths.append(3)
		else:
			l3 = l3*4
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		l3 = j5**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))