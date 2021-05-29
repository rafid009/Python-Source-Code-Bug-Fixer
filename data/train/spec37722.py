import numpy as np 

def function(x):

	u9 = x
	b1 = x
	x = 3
	paths = []
	try:
		if x <= 9:
			x = x*7
			x = u9*3
			u9 = b1+u9
			paths.append(1)
		else:
			b1 = b1*b1
			paths.append(2)
		if b1 <= 9:
			b1 = b1/x
			b1 = x*x
			b1 = b1+7
			paths.append(3)
		else:
			u9 = x/b1
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		x = u9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))