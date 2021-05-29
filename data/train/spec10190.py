import numpy as np 

def function(x):

	b6 = x
	u7 = 7
	paths = []
	try:
		if b6 > 6:
			x = x+2
			paths.append(1)
		else:
			b6 = 8+x
			paths.append(2)
		if x < 1:
			u7 = u7*0
			u7 = 0*u7
			paths.append(3)
		else:
			x = b6-0
			x = x-x
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		x = b6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))