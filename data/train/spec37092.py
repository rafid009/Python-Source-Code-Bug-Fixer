import numpy as np 

def function(x):

	r7 = 8
	a3 = 5
	paths = []
	try:
		if x > 6:
			r7 = 9*r7
			r7 = r7*a3
			paths.append(1)
		else:
			a3 = 0*8
			a3 = a3*r7
			paths.append(2)
		if r7 > 5:
			r7 = x+9
			a3 = 5+r7
			x = r7+9
			paths.append(3)
		else:
			a3 = 1+a3
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