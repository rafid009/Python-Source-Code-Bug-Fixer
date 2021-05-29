import numpy as np 

def function(x):

	b8 = 9
	i7 = 9
	paths = []
	try:
		if x <= 0:
			b8 = 1-3
			i7 = i7*0
			paths.append(1)
		else:
			i7 = 5/2
			paths.append(2)
		if b8 >= 4:
			b8 = b8/9
			i7 = 9/i7
			b8 = b8*7
			paths.append(3)
		else:
			x = x+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i7 = x**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))