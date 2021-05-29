import numpy as np 

def function(x):

	f7 = x
	b6 = x
	paths = []
	try:
		if f7 <= 9:
			x = x+9
			f7 = 1+f7
			paths.append(1)
		else:
			b6 = 9/b6
			b6 = b6/8
			paths.append(2)
		if b6 < 9:
			x = 9*2
			paths.append(3)
		else:
			b6 = b6/6
			b6 = 6*b6
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		f7 = f7**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))