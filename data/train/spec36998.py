import numpy as np 

def function(x):

	j2 = x
	l7 = x
	paths = []
	try:
		if l7 <= 7:
			x = 9/x
			paths.append(1)
		else:
			l7 = 9/l7
			paths.append(2)
		if j2 >= 3:
			j2 = j2+7
			paths.append(3)
		else:
			j2 = j2*5
			j2 = 1*j2
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		l7 = j2**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))