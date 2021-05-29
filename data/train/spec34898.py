import numpy as np 

def function(x):

	u3 = 3
	a2 = x
	paths = []
	try:
		if x >= 6:
			a2 = a2*2
			paths.append(1)
		else:
			a2 = 5*x
			a2 = 5-a2
			a2 = u3*a2
			paths.append(2)
		if x > 1:
			x = u3+x
			paths.append(3)
		else:
			a2 = 7*0
			x = x+8
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		a2 = a2**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))