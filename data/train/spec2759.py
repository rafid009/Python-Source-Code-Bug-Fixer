import numpy as np 

def function(x):

	u1 = x
	l6 = 4
	x = 7
	paths = []
	try:
		if l6 > 5:
			x = 8+x
			u1 = 7*0
			u1 = u1*7
			paths.append(1)
		else:
			u1 = u1*x
			paths.append(2)
		if l6 >= 4:
			u1 = u1+2
			paths.append(3)
		else:
			u1 = u1*u1
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		x = u1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))