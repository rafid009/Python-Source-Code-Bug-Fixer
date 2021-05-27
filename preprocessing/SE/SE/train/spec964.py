import numpy as np 

def function(x):

	f7 = 0
	b9 = x
	paths = []
	try:
		if x > 0:
			b9 = f7*7
			b9 = 5+3
			paths.append(1)
		else:
			f7 = 5*x
			x = x+f7
			x = 8+x
			paths.append(2)
		if f7 < 0:
			x = 3+x
			x = 0+f7
			paths.append(3)
		else:
			x = 7+x
			f7 = f7*4
			x = x*5
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		b9 = f7**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))