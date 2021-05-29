import numpy as np 

def function(x):

	b6 = x
	l7 = 0
	paths = []
	try:
		if b6 >= 4:
			b6 = l7+b6
			l7 = l7*0
			paths.append(1)
		else:
			b6 = b6*6
			b6 = x/b6
			x = x*9
			paths.append(2)
		if l7 > 3:
			b6 = x-b6
			paths.append(3)
		else:
			l7 = 0+l7
			x = x-4
			l7 = l7-x
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