import numpy as np 

def function(x):

	l1 = x
	a3 = x
	paths = []
	try:
		if a3 < 1:
			a3 = a3+1
			l1 = a3*0
			paths.append(1)
		else:
			a3 = 8/a3
			a3 = a3/2
			x = x+x
			paths.append(2)
		if l1 > 6:
			l1 = 2-a3
			a3 = a3*a3
			paths.append(3)
		else:
			a3 = a3*8
			l1 = 1/1
			a3 = a3-x
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		a3 = a3**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))