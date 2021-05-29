import numpy as np 

def function(x):

	j5 = x
	l2 = x
	paths = []
	try:
		if l2 >= 0:
			l2 = l2+l2
			j5 = j5+5
			j5 = 6+j5
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if j5 > 0:
			l2 = 5-l2
			l2 = j5/9
			j5 = l2*j5
			paths.append(3)
		else:
			x = x*2
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		l2 = j5**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))