import numpy as np 

def function(x):

	b6 = x
	u7 = x
	paths = []
	try:
		if b6 >= 7:
			u7 = u7*5
			b6 = 5/b6
			paths.append(1)
		else:
			x = x+9
			x = b6+5
			u7 = 0+u7
			paths.append(2)
		if x < 4:
			x = 7*x
			x = 2+x
			paths.append(3)
		else:
			x = x-x
			u7 = u7-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))