import numpy as np 

def function(x):

	a1 = x
	x1 = 8
	paths = []
	try:
		if x1 < 3:
			x = x1-0
			x1 = x1-8
			x1 = 6+x1
			paths.append(1)
		else:
			x1 = 2*8
			x1 = 7*0
			paths.append(2)
		if x1 <= 5:
			x = x*x1
			paths.append(3)
		else:
			x1 = 5*x1
			a1 = a1*7
			x = x+x1
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		a1 = a1**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))