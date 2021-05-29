import numpy as np 

def function(x):

	a7 = 4
	l7 = x
	paths = []
	try:
		if x <= 3:
			a7 = x+1
			x = 0+x
			l7 = 3/l7
			paths.append(1)
		else:
			a7 = a7*0
			paths.append(2)
		if x > 7:
			a7 = 3-a7
			a7 = 0*1
			a7 = a7/5
			paths.append(3)
		else:
			l7 = 3/5
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		x = a7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))