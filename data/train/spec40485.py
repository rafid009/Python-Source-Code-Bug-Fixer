import numpy as np 

def function(x):

	b9 = 6
	u7 = 7
	paths = []
	try:
		if x <= 9:
			u7 = u7-8
			paths.append(1)
		else:
			b9 = 2/b9
			u7 = u7+7
			u7 = x-6
			paths.append(2)
		if b9 < 4:
			b9 = 5-2
			x = 0+x
			paths.append(3)
		else:
			b9 = b9*x
			x = x+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b9 = x**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))