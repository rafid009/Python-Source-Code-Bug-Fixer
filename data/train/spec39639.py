import numpy as np 

def function(x):

	b6 = x
	u9 = x
	x = 3
	paths = []
	try:
		if x <= 7:
			x = x-7
			x = 5*x
			x = 4+x
			paths.append(1)
		else:
			b6 = b6+7
			paths.append(2)
		if u9 <= 0:
			b6 = 5/b6
			b6 = b6+b6
			x = 5-x
			paths.append(3)
		else:
			u9 = b6*x
			u9 = u9/u9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b6 = x**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))