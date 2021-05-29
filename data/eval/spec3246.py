import numpy as np 

def function(x):

	i6 = 6
	b6 = 8
	x = x
	paths = []
	try:
		if i6 >= 5:
			x = x*b6
			i6 = i6-i6
			paths.append(1)
		else:
			x = 8*9
			paths.append(2)
		if i6 <= 0:
			i6 = i6+x
			x = 2-x
			b6 = 5+b6
			paths.append(3)
		else:
			x = x+i6
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